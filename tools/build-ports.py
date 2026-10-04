#!/usr/bin/env python3
"""Build the Microsoft 365 Copilot and Google Gemini ports of MDEE.MD.

The canonical files are skills/<name>/SKILL.md. Everything this script writes is
generated from them plus ports/core.md, so a port never forks the method.

Usage, from the repository root:
    python3 tools/build-ports.py                       build into dist/ports/
    python3 tools/build-ports.py --check               validate only, write nothing
    python3 tools/build-ports.py --accept-house-rules  record that ports/core.md has
                                                       been reviewed against the
                                                       current house-rules, then build

Exit codes: 0 built or valid, 1 validation failed, 2 house-rules changed since the
last review of ports/core.md.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
PORTS = ROOT / "ports"
CORE = PORTS / "core.md"
REVIEWED = PORTS / "house-rules.reviewed"
OUT = ROOT / "dist" / "ports"

# Order follows the README capability table. `evaluation` is for maintainers and
# is deliberately left out of every port.
CAPABILITIES = [
    "problem", "stakeholders", "evidence", "options", "criteria",
    "outcomes", "trade-offs", "decide", "story",
]

SURFACES = {
    "copilot": {
        "label": "Microsoft 365 Copilot",
        "hard_limit": 8000,   # Agent Builder field and declarative agent manifest
        "max_files": 20,      # embedded files uploaded from a device
        "knowledge_how": (
            'Your knowledge holds "MDEE 00 house rules", the full version of these '
            'rules, and 1 file per capability, "MDEE 01 problem" to "MDEE 09 story". '
            "When the analytical job changes, search your knowledge for that "
            "capability's file and follow its moves."
        ),
    },
    "gemini": {
        "label": "Google Gemini",
        "hard_limit": None,   # Google publishes no limit for Gem instructions
        "max_files": 10,      # Gem knowledge files
        "knowledge_how": (
            'Your knowledge files are "MDEE 00 house rules", the full version of these '
            'rules, and 1 file per capability, "MDEE 01 problem" to "MDEE 09 story". '
            "When the analytical job changes, consult that capability's file and "
            "follow its moves."
        ),
    },
}

# Short Gem instructions for the case where a Gem will not save the full block.
# The full house rules then come from knowledge file 00. Keep in step with core.md.
GEMINI_FALLBACK = (
    "You are MDEE.MD, an alpha toolkit for working through a public policy problem. "
    'Before every reply, apply the knowledge file "MDEE 00 house rules" in full; it '
    "binds everything you do. Its 2 hardest rules: invent nothing, marking each gap as "
    "[NEEDED: what, and where it would come from], and let the user decide between "
    "real alternatives. Reply in the chat, ask 1 question at a time, and label anything "
    "you add from your own knowledge. When the analytical job changes, consult that "
    'capability\'s file, "MDEE 01 problem" to "MDEE 09 story".\n'
)

LOAD_PARAGRAPH = re.compile(
    r"Load `house-rules` before anything else here.*?\n[ \t]*\n", re.DOTALL
)
PORT_LOAD_PARAGRAPH = (
    "The house rules in your instructions are already in force and bind everything "
    "below. Their 2 hardest rules hold throughout: invent nothing, and the user "
    "decides. Where this file says skill, read capability.\n\n"
)
HTML_COMMENT = re.compile(r"<!--.*?-->\s*", re.DOTALL)
PLACEHOLDER = re.compile(r"\{\{[A-Z_]+\}\}")
KEY_LINE = re.compile(r"^([A-Za-z_][\w-]*):[ \t]*(.*)$")
FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)  # stable zips, so rebuilds diff cleanly


class BuildError(Exception):
    """A problem that must be fixed before the ports are usable."""


def short_hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def _closed_double_quote(value: str) -> bool:
    value = value.rstrip()
    if len(value) < 2 or not value.endswith('"'):
        return False
    inner = value[:-1]
    backslashes = len(inner) - len(inner.rstrip("\\"))
    return backslashes % 2 == 0


def parse_top_level(lines: list[str]) -> dict[str, str]:
    """Read top-level scalar keys from simple YAML frontmatter.

    Handles double-quoted, single-quoted, plain and block scalars, which covers
    every SKILL.md in this repository. Nested keys (metadata.status) are skipped.
    """
    fields: dict[str, str] = {}
    i = 0
    while i < len(lines):
        match = KEY_LINE.match(lines[i].rstrip("\n"))
        if not match:
            i += 1
            continue
        key, raw = match.group(1), match.group(2).strip()
        if raw[:1] in ("|", ">"):
            block, i = [], i + 1
            while i < len(lines) and (lines[i][:1] in (" ", "\t") or not lines[i].strip()):
                block.append(lines[i].strip())
                i += 1
            fields[key] = ("\n" if raw.startswith("|") else " ").join(block).strip()
            continue
        if raw.startswith('"'):
            while not _closed_double_quote(raw) and i + 1 < len(lines):
                i += 1
                raw += " " + lines[i].strip()
            try:
                fields[key] = json.loads(raw)
            except json.JSONDecodeError:
                fields[key] = raw.strip('"')
        elif raw.startswith("'") and raw.endswith("'") and len(raw) > 1:
            fields[key] = raw[1:-1].replace("''", "'")
        else:
            fields[key] = raw
        i += 1
    return fields


def read_skill(name: str) -> tuple[dict[str, str], str, str]:
    path = SKILLS / name / "SKILL.md"
    if not path.is_file():
        raise BuildError(f"missing {path.relative_to(ROOT)}")
    raw = path.read_bytes()
    lines = raw.decode("utf-8").replace("\r\n", "\n").splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise BuildError(f"{path.relative_to(ROOT)}: no frontmatter")
    for end in range(1, len(lines)):
        if lines[end].strip() == "---":
            break
    else:
        raise BuildError(f"{path.relative_to(ROOT)}: frontmatter is not closed")
    fields = parse_top_level(lines[1:end])
    if fields.get("name") != name:
        raise BuildError(f"{path.relative_to(ROOT)}: name is {fields.get('name')!r}, expected {name!r}")
    return fields, "".join(lines[end + 1:]), short_hash(raw)


def knowledge_file(name: str, fields: dict[str, str], body: str, sha: str,
                   surface_label: str, build_date: str) -> str:
    body = HTML_COMMENT.sub("", body).strip() + "\n"
    if name == "house-rules":
        use = "Use: always. Your instructions carry the core of these rules; this file holds the full text."
    else:
        body, replaced = LOAD_PARAGRAPH.subn(PORT_LOAD_PARAGRAPH, body, count=1)
        if replaced != 1:
            raise BuildError(
                f"skills/{name}/SKILL.md: the house-rules loading paragraph was not found. "
                "Update LOAD_PARAGRAPH in this script to match the new wording."
            )
        description = " ".join(fields.get("description", "").split())
        use = description if description.lower().startswith("use when") else "Use when: " + description
    header = (
        f"MDEE.MD knowledge file: {name}\n{use}\n"
        f"Built {build_date} for {surface_label} from skills/{name}/SKILL.md ({sha}).\n\n"
    )
    return header + body


def instructions(core: str, surface: str, house_sha: str, build_date: str) -> str:
    spec = SURFACES[surface]
    text = (core.replace("{{SURFACE}}", spec["label"])
                .replace("{{BUILD_DATE}}", build_date)
                .replace("{{HOUSE_RULES_SHA}}", house_sha)
                .replace("{{KNOWLEDGE_HOW}}", spec["knowledge_how"]))
    leftover = sorted(set(PLACEHOLDER.findall(text)))
    if leftover:
        raise BuildError(f"ports/core.md: unfilled placeholders {', '.join(leftover)}")
    return text.strip() + "\n"


def lint(label: str, text: str) -> list[str]:
    """Style checks that would otherwise only surface in a tester's transcript."""
    notes = []
    if "\u2014" in text:
        notes.append(f"{label}: contains an em dash, which the house rules ban")
    odd = sorted({ch for ch in text if ord(ch) > 126})
    if odd:
        notes.append(f"{label}: non-ASCII characters {''.join(odd)!r} may count differently when pasted")
    return notes


def git_commit() -> str | None:
    try:
        result = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT,
                                capture_output=True, text=True, check=True)
        return result.stdout.strip() or None
    except (OSError, subprocess.CalledProcessError):
        return None


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def write_zip(path: Path, files: dict[str, str]) -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for arcname in sorted(files):
            info = zipfile.ZipInfo(arcname, date_time=FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, files[arcname].encode("utf-8"))


def build(check_only: bool, accept_house_rules: bool) -> int:
    house_fields, house_body, house_sha = read_skill("house-rules")

    reviewed = REVIEWED.read_text(encoding="utf-8").strip() if REVIEWED.exists() else None
    if accept_house_rules and not check_only:
        write_text(REVIEWED, house_sha + "\n")
        reviewed = house_sha
    if reviewed != house_sha:
        print(
            f"house-rules is now {house_sha}; ports/core.md was last reviewed against "
            f"{reviewed or 'nothing'}.\nRead the house-rules change, update ports/core.md "
            "to match, then run with --accept-house-rules.",
            file=sys.stderr,
        )
        return 2

    if not CORE.is_file():
        raise BuildError("missing ports/core.md")
    core = CORE.read_text(encoding="utf-8").replace("\r\n", "\n")
    build_date = dt.date.today().isoformat()
    skills = {"house-rules": (house_fields, house_body, house_sha)}
    for name in CAPABILITIES:
        skills[name] = read_skill(name)

    problems: list[str] = []
    notes: list[str] = []
    outputs: dict[str, dict[str, str]] = {}
    manifest = {"built": build_date, "commit": git_commit(), "house_rules": house_sha,
                "surfaces": {}}

    for surface, spec in SURFACES.items():
        files: dict[str, str] = {}
        text = instructions(core, surface, house_sha, build_date)
        files["instructions.txt"] = text
        limit = spec["hard_limit"]
        if limit and len(text) > limit:
            problems.append(f"{surface}: instructions are {len(text)} characters; the limit is {limit}")
        elif limit and len(text) > 0.95 * limit:
            notes.append(f"{surface}: instructions are within 5% of the {limit}-character limit")
        if limit is None:
            notes.append(f"{surface}: no published instruction limit; confirm the full "
                         f"{len(text)} characters save intact, else paste instructions-fallback.txt")
            files["instructions-fallback.txt"] = GEMINI_FALLBACK
        notes.extend(lint(f"{surface} instructions", text))

        knowledge = []
        for index, name in enumerate(["house-rules"] + CAPABILITIES):
            fields, body, sha = skills[name]
            title = "house rules" if name == "house-rules" else name
            filename = f"MDEE {index:02d} {title}.txt"
            content = knowledge_file(name, fields, body, sha, spec["label"], build_date)
            files[f"knowledge/{filename}"] = content
            knowledge.append({"file": filename, "source": f"skills/{name}/SKILL.md",
                              "sha": sha, "chars": len(content)})
        if len(knowledge) > spec["max_files"]:
            problems.append(f"{surface}: {len(knowledge)} knowledge files; the limit is {spec['max_files']}")

        outputs[surface] = files
        manifest["surfaces"][surface] = {
            "label": spec["label"],
            "instructions_chars": len(text),
            "instructions_limit": limit,
            "knowledge_files": knowledge,
            "knowledge_limit": spec["max_files"],
        }

    for line in notes:
        print(f"note: {line}")
    if problems:
        for line in problems:
            print(f"error: {line}", file=sys.stderr)
        return 1

    for surface, info in manifest["surfaces"].items():
        limit = info["instructions_limit"] or "unpublished"
        print(f"{surface:8} instructions {info['instructions_chars']:>5} / {limit}   "
              f"knowledge {len(info['knowledge_files'])} / {info['knowledge_limit']} files")
    if check_only:
        print("check passed; nothing written")
        return 0

    if OUT.exists():
        shutil.rmtree(OUT)
    for surface, files in outputs.items():
        for relative, content in files.items():
            write_text(OUT / surface / relative, content)
        write_zip(OUT / f"mdee-{surface}-port.zip", files)
    write_text(OUT / "manifest.json", json.dumps(manifest, indent=2) + "\n")
    print(f"wrote {OUT.relative_to(ROOT)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="validate only; write nothing")
    parser.add_argument("--accept-house-rules", action="store_true",
                        help="record that ports/core.md matches the current house-rules")
    args = parser.parse_args()
    try:
        return build(args.check, args.accept_house_rules)
    except BuildError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Build the Claude zips in dist/ from skills/ and marketplace.json.

    dist/skills/<skill>.zip               one per skill, for the Claude Free plan
                                          (Customize > Skills). The skill folder is the zip root
    dist/download/policymemo-ai-claude.zip the whole plugin, behind the Download button on
                                          policymemo.ai (Customize > Plugins > Add > Upload
                                          local plugin). Carries both licence files

The download keeps the marketplace's plugin name, mdee, so every install
route produces the same plugin.

First it stamps the release version from marketplace.json into every
skill's frontmatter (metadata.version), so a loaded skill can say which
version it is. That is the only edit this script makes to skills/. Regenerate after any change to skills/,
marketplace.json or the licences, and commit the result:

    python3 tools/build-zips.py

Zips are written with a fixed timestamp so an unchanged source produces a
byte-identical zip and does not churn in git.
"""
import json
import pathlib
import re
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
SKILLS_OUT = ROOT / "dist" / "skills"
DOWNLOAD_OUT = ROOT / "dist" / "download"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
LICENCES = ("LICENSE", "LICENSE-CONTENT.md")

# Which marketplace entry each download is built from, and any manifest
# fields that differ from it.
DOWNLOADS = {
    "policymemo-ai-claude": {
        "source": "mdee",
        "folder": "policymemo-ai",
        "manifest": {"homepage": "https://policymemo.ai"},
    },
}

MANIFEST_FIELDS = (
    "name", "displayName", "description", "version",
    "author", "homepage", "repository", "license", "keywords", "skills",
)


def add(z: zipfile.ZipFile, arcname: str, data: bytes) -> None:
    info = zipfile.ZipInfo(arcname, date_time=FIXED_TIME)
    info.external_attr = 0o644 << 16
    info.compress_type = zipfile.ZIP_DEFLATED
    z.writestr(info, data)


def add_folder(z: zipfile.ZipFile, prefix: str, folder: pathlib.Path) -> int:
    files = sorted(f for f in folder.rglob("*") if f.is_file())
    for f in files:
        add(z, f"{prefix}/{f.relative_to(folder).as_posix()}", f.read_bytes())
    return len(files)


VERSION_LINE = re.compile(r"^(metadata:\n)(  version: .*\n)?", re.M)


def stamp_versions() -> None:
    """Write the marketplace version into each SKILL.md's metadata.version."""
    entries = json.loads(MARKETPLACE.read_text())["plugins"]
    version = next(p["version"] for p in entries if p["name"] == DOWNLOADS["policymemo-ai-claude"]["source"])
    for path in sorted(SKILLS.glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        front_end = text.index("\n---", 3)
        front, rest = text[:front_end + 1], text[front_end + 1:]
        if not VERSION_LINE.search(front):
            raise SystemExit(f"{path.relative_to(ROOT)}: frontmatter has no metadata block")
        stamped = VERSION_LINE.sub(lambda m: f"{m.group(1)}  version: {version}\n", front, count=1)
        if stamped != front:
            path.write_text(stamped + rest, encoding="utf-8")
            print(f"stamped {path.relative_to(ROOT)} with {version}")


def remove_stale(out: pathlib.Path, keep: set) -> None:
    for p in out.glob("*.zip"):
        if p.stem not in keep:
            p.unlink()
            print(f"removed stale {p.relative_to(ROOT)}")


def build_skills() -> None:
    SKILLS_OUT.mkdir(parents=True, exist_ok=True)
    names = []
    for skill in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        with zipfile.ZipFile(SKILLS_OUT / f"{skill.name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
            count = add_folder(z, skill.name, skill)
        names.append(skill.name)
        print(f"skills/{skill.name}.zip ({count} file{'s' if count != 1 else ''})")
    remove_stale(SKILLS_OUT, set(names))


def build_downloads() -> None:
    DOWNLOAD_OUT.mkdir(parents=True, exist_ok=True)
    catalog = {p["name"]: p for p in json.loads(MARKETPLACE.read_text())["plugins"]}
    for zip_name, spec in DOWNLOADS.items():
        entry = catalog[spec["source"]]
        manifest = {k: entry[k] for k in MANIFEST_FIELDS if k in entry}
        manifest.update(spec["manifest"])
        folder = spec["folder"]
        with zipfile.ZipFile(DOWNLOAD_OUT / f"{zip_name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
            add(z, f"{folder}/.claude-plugin/plugin.json",
                (json.dumps(manifest, indent=2) + "\n").encode())
            count = 1
            for name in LICENCES:
                add(z, f"{folder}/{name}", (ROOT / name).read_bytes())
                count += 1
            for skill_path in entry["skills"]:
                skill_name = skill_path.lstrip("./")
                count += add_folder(z, f"{folder}/{skill_name}", SKILLS / skill_name)
        print(f"download/{zip_name}.zip ({count} files)")
    remove_stale(DOWNLOAD_OUT, set(DOWNLOADS))


if __name__ == "__main__":
    stamp_versions()
    build_skills()
    build_downloads()

#!/usr/bin/env python3
"""Build the zip behind the Download button on policymemo.ai.

One zip per platform, written to dist/download/. Today that is Claude only;
Copilot gets its own entry in PLATFORMS when it exists.

The Claude zip is the same plugin as dist/plugin/mdee.zip, with both
licence files inside so it carries its terms with it. It keeps the
marketplace's plugin name, mdee, so every install route produces the same
plugin. It installs through claude.ai's Customize > Plugins > Add > Upload
local plugin. Regenerate after any change to skills/, marketplace.json or
the licences and commit the result:

    python3 tools/build-download-zips.py

Zips are written with a fixed timestamp so an unchanged source produces a
byte-identical zip and does not churn in git.
"""
import json
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
OUT = ROOT / "dist" / "download"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
LICENCES = ("LICENSE", "LICENSE-CONTENT.md")

# Which marketplace entry each download is built from, and any manifest
# fields that differ from it.
PLATFORMS = {
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


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    catalog = {p["name"]: p for p in json.loads(MARKETPLACE.read_text())["plugins"]}
    built = []

    for zip_name, spec in PLATFORMS.items():
        entry = catalog[spec["source"]]
        manifest = {k: entry[k] for k in MANIFEST_FIELDS if k in entry}
        manifest.update(spec["manifest"])
        folder = spec["folder"]

        target = OUT / f"{zip_name}.zip"
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
            add(z, f"{folder}/.claude-plugin/plugin.json",
                (json.dumps(manifest, indent=2) + "\n").encode())
            count = 1
            for name in LICENCES:
                add(z, f"{folder}/{name}", (ROOT / name).read_bytes())
                count += 1
            for skill_path in entry["skills"]:
                skill_name = skill_path.lstrip("./")
                skill_dir = SKILLS / skill_name
                for f in sorted(p for p in skill_dir.rglob("*") if p.is_file()):
                    add(z, f"{folder}/{skill_name}/{f.relative_to(skill_dir).as_posix()}",
                        f.read_bytes())
                    count += 1
        built.append((zip_name, count))

    for p in OUT.glob("*.zip"):
        if p.stem not in PLATFORMS:
            p.unlink()
            print(f"removed stale {p.name}")

    for name, count in built:
        print(f"{name}.zip ({count} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

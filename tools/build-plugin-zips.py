#!/usr/bin/env python3
"""Build one self-contained zip per plugin entry, for claude.ai's
Customize > Plugins > Add > Upload local plugin.

The marketplace route installs a plugin by fetching its files live; this
zip carries the same plugin with its own .claude-plugin/plugin.json
manifest, so it installs from a local file instead. Output goes to
dist/plugin/. Regenerate after any change to skills/ or
.claude-plugin/marketplace.json and commit the result:

    python3 tools/build-plugin-zips.py

Zips are written with a fixed timestamp so an unchanged plugin produces a
byte-identical zip and does not churn in git.
"""
import json
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
OUT = ROOT / "dist" / "plugin"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)

# plugin.json accepts these; marketplace.json also carries source/category/
# strict/relevance, which describe how the marketplace hosts the plugin
# rather than what the plugin is, so they don't belong in its own manifest.
MANIFEST_FIELDS = (
    "name", "displayName", "description", "version",
    "author", "homepage", "repository", "keywords", "skills",
)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    catalog = json.loads(MARKETPLACE.read_text())
    built = []

    for entry in catalog["plugins"]:
        name = entry["name"]
        manifest = {k: entry[k] for k in MANIFEST_FIELDS if k in entry}
        manifest_bytes = (json.dumps(manifest, indent=2) + "\n").encode()

        target = OUT / f"{name}.zip"
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
            info = zipfile.ZipInfo(f"{name}/.claude-plugin/plugin.json", date_time=FIXED_TIME)
            info.external_attr = 0o644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, manifest_bytes)

            file_count = 1
            for skill_path in entry["skills"]:
                skill_name = skill_path.lstrip("./")
                skill_dir = SKILLS / skill_name
                for f in sorted(p for p in skill_dir.rglob("*") if p.is_file()):
                    arcname = f"{name}/{skill_name}/{f.relative_to(skill_dir).as_posix()}"
                    info = zipfile.ZipInfo(arcname, date_time=FIXED_TIME)
                    info.external_attr = 0o644 << 16
                    info.compress_type = zipfile.ZIP_DEFLATED
                    z.writestr(info, f.read_bytes())
                    file_count += 1
        built.append((name, file_count))

    stale = [p for p in OUT.glob("*.zip")
             if p.stem not in {name for name, _ in built}]
    for p in stale:
        p.unlink()
        print(f"removed stale {p.name}")

    for name, count in built:
        print(f"{name}.zip ({count} file{'s' if count != 1 else ''})")
    print(f"\n{len(built)} plugin zips in {OUT.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

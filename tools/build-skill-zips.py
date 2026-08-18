#!/usr/bin/env python3
"""Build one zip per skill for upload to claude.ai (Customize > Skills).

Each zip contains the skill folder as its root, which is what claude.ai
expects. Output goes to dist/skills/. Regenerate after any change to
skills/ and commit the result:

    python3 tools/build-skill-zips.py

Zips are written with a fixed timestamp so an unchanged skill produces a
byte-identical zip and does not churn in git.
"""
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "skills"
OUT = ROOT / "dist" / "skills"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    built = []
    for skill in sorted(p for p in SRC.iterdir() if p.is_dir()):
        target = OUT / f"{skill.name}.zip"
        files = sorted(f for f in skill.rglob("*") if f.is_file())
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
            for f in files:
                arcname = f"{skill.name}/{f.relative_to(skill).as_posix()}"
                info = zipfile.ZipInfo(arcname, date_time=FIXED_TIME)
                info.external_attr = 0o644 << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, f.read_bytes())
        built.append((skill.name, len(files)))

    stale = [p for p in OUT.glob("*.zip")
             if p.stem not in {name for name, _ in built}]
    for p in stale:
        p.unlink()
        print(f"removed stale {p.name}")

    for name, count in built:
        print(f"{name}.zip ({count} file{'s' if count != 1 else ''})")
    print(f"\n{len(built)} skill zips in {OUT.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

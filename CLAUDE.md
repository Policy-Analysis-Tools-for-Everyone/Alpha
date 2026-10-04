# policymemo.ai

Policy-analysis skills for Claude. Read `CONTRIBUTING.md` for the map; this file is the rules.

- `skills/<name>/SKILL.md` is the only copy of each skill. `reference/AUTHORING.md` is how to write one.
- Never hand-edit `dist/` or the generated pages in `docs/`. Edit the source, then rebuild:
  `python3 tools/build-zips.py`, `python3 tools/build-ports.py`, `python3 tools/build-site.py`.
- The version lives in `.claude-plugin/marketplace.json` (both entries). Bump it for every release.
- `evals/README.md` says how to add a tester report and re-mine `evals/wiki/`.
  Nothing from `evals/` ever goes into a skill, a Project or memory used in a test session.
- Never delete anything under `reference/domain/` or `reference/sources/` without the owner saying so.

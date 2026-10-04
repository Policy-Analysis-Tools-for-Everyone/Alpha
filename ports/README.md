# Ports

Generated Microsoft 365 Copilot and Google Gemini versions of MDEE.MD.

- `core.md` is the only hand-written port text: the house rules compressed to fit Copilot's 8,000-character instructions field, plus a 1-line router per capability. Placeholders in double braces are filled at build time.
- `house-rules.reviewed` records the house-rules hash that `core.md` was last checked against.
- Everything else comes from `skills/` through `python3 tools/build-ports.py` and lands in `dist/ports/`.

When house-rules changes, the build stops with exit code 2. Read the change, update `core.md` to match, then run:

    python3 tools/build-ports.py --accept-house-rules

Set-up steps, settings and the test plan are in the porting handoff.

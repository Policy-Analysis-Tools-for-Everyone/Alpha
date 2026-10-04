# Ports

Microsoft 365 Copilot and Google Gemini versions of policymemo.ai, generated from the
Claude version. `skills/` is the only source of the method. Nothing here edits it, and
a port never forks it.

| File | What it is |
|---|---|
| `core.md` | The only hand-written port text: the house rules compressed to fit Copilot's 8,000-character instructions field, and 1 line per capability. Placeholders in double braces are filled at build time |
| `house-rules.reviewed` | The house-rules hash that `core.md` was last checked against |
| `setup-copilot.md`, `setup-gemini.md` | Set-up guides, copied into each port as `SETUP.md` |
| `testing.md` | The test plan. Nothing has been run on either surface yet |

## Building

    python3 tools/build-ports.py           build into dist/ports/
    python3 tools/build-ports.py --check   validate only, write nothing

Each surface gets `instructions.txt`, 10 knowledge files and `SETUP.md`, zipped as
`dist/ports/mdee-<surface>-port.zip`. Each knowledge file is a skill's `SKILL.md`
with its provenance comments removed and its house-rules loading paragraph replaced,
followed by any other Markdown in that skill's folder (today, `story/writing.md`).
Gemini also gets `instructions-fallback.txt`, for a Gem that won't save the full
instructions.

The build fails if the Copilot instructions exceed 8,000 characters, or if either
surface would need more knowledge files than it allows (Copilot 20, Gemini 10).
Inputs are dated by their last commit, so an unchanged source rebuilds identically.

## When house-rules changes

The build stops with exit code 2. Read the house-rules change, update `core.md` to
match, then run:

    python3 tools/build-ports.py --accept-house-rules

Only `house-rules` is gated, because `core.md` compresses it. Changes to a capability
skill flow into its knowledge file on the next build with nothing to review, unless
the skill's description changes enough that its 1-line entry under Capabilities in
`core.md` no longer fits.

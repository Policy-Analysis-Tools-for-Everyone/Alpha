# Ports

Microsoft 365 Copilot and Google Gemini versions of policymemo.ai, generated from the
Claude version. `skills/` is the only source of the method. Nothing here edits it, and
a port never forks it.

| File | What it is |
|---|---|
| `core.md` | The only hand-written port text: the house rules compressed to fit Copilot's 8,000-character instructions field, and 1 line per capability. Placeholders in double braces are filled at build time |
| `house-rules.reviewed` | The house-rules hash that `core.md` was last checked against |
| `testing.md` | The test plan. Nothing has been run on either surface yet |

## Building

    python3 tools/build-ports.py           build into dist/ports/
    python3 tools/build-ports.py --check   validate only, write nothing

Set-up steps for people installing a port live on the install page, `install/body.html`,
which is the only copy. Each zip, `dist/ports/policymemo-ai-<surface>.zip`, opens to files
named for what to do with them, because many people will not read anything else:

    0 Read me first.txt                  short steps, and a link to the install page
    1 Paste into Instructions.txt
    2 Upload these 8 skills/             Copilot only: policymemo-problem.zip to policymemo-story.zip
    3 No Skills option - upload these as knowledge instead/       Copilot's knowledge fallback
    2 Upload these 10 files/             Gemini: policymemo 00 house rules.txt to policymemo 09 story.txt
    If the instructions get cut short, paste this instead.txt     Gemini only

**Copilot skills.** Agent Builder accepts SKILL.md skill zips, the same format as
the Claude skills. It allows at most 8 skills per agent, each SKILL.md under 20,000
characters with a description of at most 1,024. Each skill is the capability's
SKILL.md with provenance stripped and house-rules loading replaced, named
`policymemo-<capability>`, with its supporting files beside it. There are 9
capabilities, so `trade-offs` travels inside `policymemo-decide` as `trade-offs.md`,
with a line in decide's body and description pointing to it (`HOSTED` in the
script). The build fails if any of those limits is broken.

The zip has no folder inside it. Windows Extract All and the Mac's Archive Utility each
make one named after the zip, so an inner folder would nest a second copy. The knowledge
file prefix, `policymemo`, is what the instructions search for, so renaming the files
breaks the link between them.

Each knowledge file is a skill's `SKILL.md` with its provenance comments removed and its house-rules loading paragraph replaced,
followed by any other Markdown in that skill's folder (today, `story/writing.md`).

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

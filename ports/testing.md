# Testing the ports

Nothing in this folder has been run on either surface yet. Until it has, the ports are
untested in the strict sense: the rules are the same as the Claude version, and
there's no evidence about whether either surface follows them.

## What the ports can't inherit

The Claude evidence in `evals/` doesn't transfer. Every session there ran on Claude
with the skills loaded as skills. A port changes 3 things at once: the model, the
instructions (compressed into `core.md`), and how capability text arrives (searched
knowledge files, not loaded skills). A failure on a port can come from any of the 3.

## Order

Run these in order. Each stage is cheap and stops a wasted run at the next.

1. **Install check.** Follow `setup-copilot.md` or `setup-gemini.md` exactly. Record
   whether the instructions saved whole, and whether knowledge upload was available.
   On Gemini, record whether the full instructions held or the fallback was needed.
2. **Smoke test.** Open with each of the 3 README openings, in fresh chats. Check the
   things the instructions carry directly: 1 question at a time, no document as a
   routine reply, no invented figure, no framework named, UK spelling, no em dashes.
3. **Knowledge reach.** The core rules are in the instructions, so the smoke test
   can't show whether the files are used. Use cases whose pass depends on a move
   that only a knowledge file holds:
   - `evals/wiki/prompts/system-map-trigger.md` (the `problem` file)
   - a request for a one-page PPC memo from a finished analysis. The section
     structure under "PPC memo mode" exists only in the `story` file. Don't use
     W4 or W5 for this: `core.md` now carries their rules too
   - `evals/wiki/prompts/stakeholder-sequencing.md` (the `stakeholders` file)

   Run each twice: with the knowledge files, and on an agent built from the
   instructions alone. If the 2 runs don't differ, the files aren't being reached.
   That is the most important single result for the free Copilot tier, where
   uploads may be unavailable.
4. **Regression.** Run `evals/tests/regression-problem-first-session.md` and
   `evals/tests/regression-writing-and-transfer.md` as written, changing only the
   surface.
5. **Real use.** Sessions from real work, reported through the session report.

## Recording

Record port runs in `evals/sessions/` like any other session, with these fields added
to the header: surface (Copilot or Gemini), the build date and house-rules hash from
the first lines of `instructions.txt`, whether knowledge files were present, and on
Gemini whether the fallback instructions were used.

A finding that reproduces on Claude belongs to the skills. A finding that appears only
on a port belongs to `ports/core.md` or the build, and is fixed there, never by
editing `skills/` to suit a port.

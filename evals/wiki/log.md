# Log

Append-only, newest at the bottom. One entry per ingest, re-mine, lint or skill change
that the evidence drove. Say what changed in the wiki, not what the report said.

    ## YYYY-MM-DD · ingest | mine | lint | change · one line
    What moved: which findings gained or lost a sighting, which prompt was opened or closed.

---

## 2026-08 · ingest · alpha sessions

T001–T004 ran 17 sessions on plugin `0.1.1`, written up in `raw/alpha/`. Nine are
transcripts, three are debriefs of those, one is T003's report on six sessions, one is T004's note.

## 2026-09-22 · mine · findings F1–F13

First mining of all 17 sessions into `findings.md`.

## 2026-09-29 · change · round 1, plugin `0.1.1` → `0.1.2`

Skills edited 2026-09-29, plugin `0.1.1` → `0.1.2`. Every session above tested `0.1.1`, so
**nothing here is evidence about what ships now.**

| Finding | Change | Where |
|---|---|---|
| F1 | The one-line rule on background knowledge replaced with four categories and an in-sentence label, plus an explicit over-correction warning | `house-rules`, Evidence discipline |
| F1 | Self-check line 1 rewritten. It demanded that nothing in a reply came from the agent, which is unachievable, so it was read as "I invented nothing" and could never fail | `house-rules`, Self-check |
| F13 | Lead with the deliverable; under a constraint, choose and say what you dropped | `house-rules`, Chat is the whole experience |
| F1, F13 | Two matching entries added so the failure list agrees with the rules | `house-rules`, Failure modes |
| F7 | System map moved out of move 9 and onto the hierarchy standing instruction, which does fire: *if you say hierarchy, draw it* | `problem` |

**The gate was not run.** T003 named C-9 — useful background, direct answer needed — as
mandatory before and after the F1 change, and `prompts/sound-work.md` records that nothing in
the corpus tests whether the agent accepts sound work. The changes were made on the evidence
without it. The risk is specific and already has a precedent in this repository: a ban on
naming frameworks, read too broadly, produced evasive answers on the first recorded test. The
F1 edit carries an explicit over-correction paragraph for that reason, and that paragraph is
untested.

**Least evidenced change here:** the constraint rule under F13. No session in the corpus was
run against a deadline or a length limit, so it is written from two reports of the symptom and
none of the condition.

**What it left to do next, in order.** The three gates are now written up as **C17**, **C18** and
**C19** in `../tests/capability-pack.md` Part 3, and none has been run. They cannot be
run here: policymemo.ai is not installed in the maintainer's working session, and the author of a
change cannot behaviourally test it — `../README.md` says a same-session self-test catches
structure, not behaviour. They need a fresh chat on `0.1.2`, ideally not the author's.

Then replay both `problem` transcripts against the new map trigger, and take a cold session on
`0.1.2`.

Not changed, and why: F6 has one clear instance still blocked on a lost user turn. F12 has one
tester and no transcript. F2 is a packaging problem, not a skill one.

## 2026-10-03 · change · writing and transfer to documents

`house-rules` and `story` revised. F6 and F11 drove the changes that carry a flag in
conversation into the document and settle contested framing plus an artefact request.
Cases W1–W5 in `../tests/regression-writing-and-transfer.md`. Not run.

## 2026-10-04 · lint · alpha closed, ready for the beta

`sessions/` became `raw/alpha/` and is now frozen; beta reports go in `raw/beta/`.
`testers.md` moved into the wiki with Phase and Route columns, alpha rows closed.
`findings.md` now keeps counts per version, with the beta's first runs at the top.
The capability pack lost "alpha" from its name. The beta ships as `0.2.0`, with the same
skills as `0.1.2`.

Alpha files still cite the old paths: `sessions/` is `raw/alpha/`, `testers.md` is
`wiki/testers.md`, `tests/capability-alpha-pack.md` is `tests/capability-pack.md`.

## 2026-10-04 · lint · alpha consent, and the spec follows the skills

Consent to publish confirmed by the maintainer for all four alpha testers. `testers.md` and
the `t004-note.md` header record it.

`reference/BEHAVIOUR_SPEC.md` brought into line with `house-rules` and `problem` as they
stand after round 1 and the writing revision, and now says the skills are canonical.
`ports/core.md` already matched `house-rules`.

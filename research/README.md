# Research

The study of what happens to students' policy reasoning when they use policymemo.ai.
Start at [`design.md`](design.md).

| | Asks | About |
|---|---|---|
| `evals/` | What does policymemo.ai do, and how should it change? | The agent |
| `research/` | What happens to policy reasoning when students use it? | The student |

The same conversation can be evidence for both. The two are never analysed as one.
`design.md` section 13 says how findings move between them.

## Rules

1. **No participant data in this folder, or anywhere in this repository.** The
   repository is public. Transcripts, artefacts, change notes, questionnaires, interview
   recordings, consent records and the key linking codes to people are held on UCL
   systems, as the approved protocol says. What lives here is design, instruments,
   codebooks, analysis plans, synthetic examples and aggregated findings.
2. **Nothing from `research/` reaches policymemo.ai.** No instrument, codebook, moment
   design or participant material goes into a skill, a Project, a system prompt or
   memory. The agent must not know a student is in the study. This extends the `evals/`
   rule.
3. **Research findings never edit a skill directly.** A finding with a product
   implication becomes a prompt in `evals/wiki/prompts/` and follows the evals loop.
4. **Research IDs are not evals IDs.** No crosswalk between them is committed.
5. **The analysis plan is committed before data arrives.** Deviations are logged.
6. **When a skill changes, `prompt-footprint.md` changes in the same commit.**

## What is here now

| File | What it is |
|---|---|
| `design.md` | The research design: questions, conceptual model, moments, evidence, analysis, validity, ethics, relation to the product. Draft 1 |
| `prompt-footprint.md` | What each skill prompts students to do, and the trace it leaves. Separates prompted moves from independent ones |
| `open-questions.md` | Information and decisions the design is waiting on |
| `ethics/consent-form-draft.docx` | Draft consent form on the IIPP LREC template. Placeholders in square brackets |

## Proposed layout, added as each part is needed

Folders are created when they have something in them, not before.

```text
research/
  README.md              this file: the rules and the map
  design.md              the design; revised as decisions are made
  prompt-footprint.md    per version, kept current with skills/
  open-questions.md      deleted row by row as answered
  log.md                 append-only: design decisions, approvals, deviations
  ethics/                protocol, information sheets and consent forms as submitted;
                         approval references. No signed forms
  instruments/           the change-note form, questionnaires, anchor vignettes,
                         tutor note template, interview guide
  moments/               one file per research moment: the seminar activity, timing,
                         sequence arms, what is collected
  codebook/              dimensions D1-D8, X1-X2, J1-J6, uptake and arrival codes,
                         each tagged prompted and taught; worked synthetic examples
  analysis/              the pre-committed plan; scripts that run on data held
                         elsewhere; deviation log
  sites/                 ucl.md, and one file per naturalistic site: context
                         descriptor, governance status, contact role (not names)
  findings/              aggregated, de-identified results, counted as
                         n students / m episodes, with version, model and surface
```

## Status

| State | Now |
|---|---|
| Design drafted | Yes, 2026-10-04 |
| Questions agreed by the research team | No |
| UCL 2026-27 seminar sequence known | No: `design.md` uses the 2025-26 draft |
| Researcher's role | Confirmed: the seminar's PGTA, and the product author. See `design.md` 12.0 |
| Sponsor and consent holder | Agreed: the module lead; a second PGTA. See `design.md` 12.0 |
| Term starts | Thursday 2026-10-08 |
| Ethics submitted | No |
| Ethics approved | No |
| Any data collected | No |

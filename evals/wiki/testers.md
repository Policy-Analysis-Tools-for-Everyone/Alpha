# Testers

A pseudonymous register of everyone who has run policymemo.ai in a session that was
saved or reported. One row each, no session content.

**It exists to answer one question: how many independent people?** Without a stable
identifier, 2 testers both recorded as "policy adviser" can't be told apart from 1
person tested twice. `agent-evaluation-guidance.md` rule 25 requires the distinction.

The join is the `Tester` row in each report header. Reports stay in `../raw/`.
Privacy and counting rules are in `../README.md`, not repeated here.

## The register

| ID | Phase | Route | Role type | Policy experience | AI familiarity | Knows policymemo.ai | Sessions | First session | Consent to publish |
|---|---|---|---|---|---|---|---|---|---|
| T001 | alpha | — | Project owner and author | not recorded | high | authored it | 6 | 2026-08-17 | yes |
| T002 | alpha | — | not recorded | not recorded | high | yes, familiar before first session | 3 | 2026-08 | yes, anonymised |
| T003 | alpha | — | not recorded | not recorded | high | yes, wrote runs up against the evaluation method | 6 | 2026-08 | **not confirmed** |
| T004 | alpha | — | not recorded | not recorded | high | possibly not | 2 | not recorded | **not confirmed** |

**The alpha rows are closed.** Fields nobody recorded at the time say so rather than
being filled in from memory. Beta testers start at **T005**.

## What each field is for

Every field has to change how a finding is read, or it comes out.

| Field | What it lets you interpret |
|---|---|
| `ID` | The join key. The only reason this file exists |
| `Phase` | alpha or beta. Alpha testers were hand-picked, all highly AI-familiar, and mostly knew the skills |
| `Route` | Beta only: student or practitioner, as in the beta access list. Whether a finding is about the tool or about the job |
| `Role type` | Broad, such as "policy adviser, local government" |
| `Policy experience` | Whether "it challenged too hard" means the challenge was wrong or the tester is junior |
| `AI familiarity` | Low, medium or high. The largest confounder on any finding about interaction. Constant in the alpha; expected to vary in the beta |
| `Knows policymemo.ai` | Has read the skill files or used it before, or has not. Extends the warm and cold distinction to the person |
| `Sessions` | Count and first date. Longitudinal visibility without a second file |
| `Consent to publish` | Whether an anonymised transcript may be committed to this public repository |

**Cold or warm is a property of the session, not the person.** It belongs in the
report header. Everyone is cold on their first session and nobody is after that.

**Broad policy domain is deliberately absent.** At this sample size it approaches
identifying. Add it the day a domain-specific defect actually appears.

## What never goes in this file

- Names, employers, job titles, team names, locations, or any free text about a
  person.
- **The mapping from ID to person.** That is held privately by the maintainer and
  is never committed.
- Adjectives about the person. *T001 is impatient* is a personality claim.
  *T001 asked for a direct revision in 3 of 4 sessions* is an observation.
- Session content, or a summary of it.

## Per-tester learning records

None yet. Build one when a single tester reaches 3 saved sessions, or when the
first cross-user synthesis exists, whichever comes first. Only a per-person time
series can say whether a fourth session went better because policymemo.ai improved
or because the tester learned to drive it. Every line in one links to the session
supporting it.

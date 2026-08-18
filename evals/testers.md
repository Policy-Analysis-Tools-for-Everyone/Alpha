# Testers

A pseudonymous register of everyone who has run MDEE.MD in a session that was
saved. One row each, no directories, no session content.

**It exists to answer one question: how many independent people?** The method
requires that and the repository could not previously express it.
`agent-evaluation-guidance.md` rule 25 says to track sessions, users where known,
contexts, models and skill versions, and warns against counting correlated
observations as independent cases. Rule 11's frequency scale runs from a single
occurrence up to *repeated across users*. Without a stable identifier, 2 testers
both recorded as "policy adviser" cannot be told apart from 1 person tested twice.

The join is the `Tester` row in each transcript header, which carries the ID.
Sessions stay in `transcripts/`. Nothing here duplicates them.

## The register

| ID | Role type | Policy experience | AI familiarity | Knows MDEE | Sessions | First session | Consent to publish |
|---|---|---|---|---|---|---|---|
| T001 | Project owner and author | `[add]` | high | authored it | 1 | 2026-08-17 | yes |

## What each field is for

Every field has to change how a finding is read, or it comes out.

| Field | What it lets you interpret |
|---|---|
| `ID` | The join key. The only reason this file exists |
| `Role type` | Broad, such as "policy adviser, local government". Whether a finding is about the tool or about the job |
| `Policy experience` | Whether "it challenged too hard" means the challenge was wrong or the tester is junior |
| `AI familiarity` | Low, medium or high. The largest confounder on any finding about interaction |
| `Knows MDEE` | Has read the skill files, or has not. Extends the warm and cold distinction to the person |
| `Sessions` | Count and first date. Longitudinal visibility without a second file |
| `Consent to publish` | Whether an anonymised transcript may be committed to a public repository |

**Cold or longitudinal is a property of the session, not the person.** It belongs
in the transcript header. Everyone is cold on their first session and nobody is
after that.

**Broad policy domain is deliberately absent.** At this sample size it approaches
identifying, and no finding currently imaginable would be read differently because
someone works in housing rather than transport. Add it the day a domain-specific
defect actually appears.

## What never goes in this file

- Names, employers, job titles, team names, locations, or any free text about a
  person.
- **The mapping from ID to person.** That is held privately by the maintainer and
  is never committed. This one rule is most of the privacy design.
- Adjectives about the person. *T001 is impatient* is a personality claim.
  *T001 asked for a direct revision in 3 of 4 sessions* is an observation. The
  difference is that one can be checked against a transcript.
- Session content, or a summary of it.
- Anything the agent could read during a test session. See the cold-testing rule
  in `README.md`.

## Counting findings

Always report as **n testers / m sessions**. Never a percentage, never "most
users". At this sample size a proportion misleads.

A behaviour seen 4 times in one person's sessions is *1 tester (4 sessions)*,
never *4 occurrences*. That follows directly from rule 25 and it is the whole
defence against inventing significance from a tiny alpha sample.

## Per-tester learning records

There are none, and there should not be yet.

A record of what one person's repeated use teaches would own a real job that
nothing else covers: separating change in the user from change in the agent. A
cross-session synthesis groups by skill, version, model and use case, across
people on purpose. A transcript is one moment. Only a per-person time series can
say whether a fourth session went better because MDEE improved or because the
tester learned to drive it.

It needs input before it can say anything. **Build one when a single tester
reaches 3 saved sessions, or when the first cross-user synthesis exists,
whichever comes first.** Before that it would be a confident narrative about
somebody watched once, written at a smaller sample than the synthesis layer it
duplicates.

When one is written, every line carries a link to the session supporting it, and
observed behaviour, user-stated preference, evaluator interpretation and
hypothesis stay separately labelled.

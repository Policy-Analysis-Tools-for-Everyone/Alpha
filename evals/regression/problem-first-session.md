# Regression: fixes from the first real session

**Traceable to real behaviour.** These 4 cases exist because a real session found
4 defects and the capability was changed in response. That makes them the only
regression cases in this repository with evidence behind them.

| | |
|---|---|
| Skill | `problem` (then `01-problem`) |
| Source session | `../transcripts/problem/receipt-confirmation.md` |
| Defects found in | commit `bdd8640` |
| Fixed in | commit `b5fcae9` |
| Model that produced the failures | Claude Opus 5 |
| Run type | warm, and without shared house rules, which did not exist yet |
| Status | **never re-run.** Written from the session record, not from a replay |

**These have not been verified against the current `problem` skill.** The skill has
since been rewritten: renamed, resourced to the canonical method, and stripped of
material that now lives in `house-rules`. Re-running these 4 is the cheapest
worthwhile check available on this repository, and it has not been done.

## How to run

Fresh session, `house-rules` and `problem` available, nothing else loaded. Give the
input. Do not name the skill. Check the assertions.

---

## R1. Structured output, not a wall of prose

**Why this exists.** The original failure was not a document-shaped reply. It was
the opposite: roughly 700 words of continuous prose in which all 4 required parts
were present and none could be found. The no-documents rule had over-corrected.

**Input.** Paste a plan document containing a solution-shaped problem statement,
supporting bullets, some call-volume data and a list of assumptions. Then ask:
*"Provide a recommended adjustment to the problem statement with reasoning and
trade-offs."*

**Must:**

- return 4 findable parts in order: candidate statement, critique, revised
  statement, readout
- keep the critique short, with each failure as a claim rather than a paragraph
- keep the readout to 4 brief labelled lines including the key trade-off
- use the vocabulary of public value, operational capacity and political support
  directly

**Must not:**

- bury the 4 parts in continuous paragraphs with bolded lead-ins
- produce a document with a title, an executive summary or `##` headings
- avoid the working vocabulary out of caution about naming frameworks. **This was
  a real observed failure**: the agent read the framework ban as a ban on the terms
  and went evasive

## R2. Labelling fires early

**Why this exists.** Problem, mechanism, symptom and constraint were never
labelled, on material that ran all 4 together. The instruction was buried inside a
move and did not fire, which is why it is now a standing instruction rather than a
step.

**Input.** As R1.

**Must:** label the 4 things separately and early, before or within the first
substantive response.

**Must not:** silently re-sort the user's material into a cleaner account without
showing the distinction. The distinction is the finding.

## R3. The hierarchy decision is made out loud

**Why this exists.** The material was plainly a hierarchy with 2 candidate cores at
different levels, the applicant's uncertainty and the contact centre's load. Neither
the hierarchy nor the 2 candidates was named until the third turn. A compact problem
system map with 6 named parts came late and vaguely.

**Input.** As R1.

**Must:**

- say explicitly that this is a hierarchy rather than a single problem
- name both candidate cores and note they do not have the same answers
- produce a problem system map with its 6 parts named: core problem, evidence,
  sub-problems, mechanisms, constraints, missing metrics
- ask for a metric or observable indicator per sub-problem

**Must not:** define whichever level was written down most confidently and proceed.

**Counter-case, R3b.** Input: a genuinely single, well-scoped problem, such as
*"Roughly 4,000 eligible households a year fail to complete the renewal form after
starting it."* **Must not** force a hierarchy or a system map onto it. This pair
matters: R3 alone would teach the agent to find a hierarchy in everything.

## R4. The framing choice surfaces without being asked for

**Why this exists.** The competing framings, the harm to applicants against the cost
to the organisation, appeared only when the user requested a recommendation. This
was predicted before the test and happened anyway. Competing conditions are now
named at the first move and carried forward.

**Input.** As R1, but **stop after the first exchange** and do not ask for a
recommendation.

**Must:** name both candidate framings in the first substantive response, with what
each costs in value, deliverability and support.

**Must not:** wait to be asked, and must not resolve the choice on the user's
behalf.

---

## Two omissions also fixed, worth checking

**R5.** A metric is requested for each sub-problem. This was in the original agent's
instructions and was missing from the skill entirely.

**R6.** The self-check works as a scoring list. Input: *"Score this problem
statement."* **Must** return pass or fail against each criterion with a reason on
every fail, rather than prose commentary.

---

## What these cases cannot tell you

They came from a warm session run by the skill's own author, without shared house
rules, on one model. They catch structural regressions, which is what they were
built from. They say nothing about whether the capability is any good for someone
who did not write it.

The finding from that session is worth repeating: 2 of the 4 defects were not
predicted at all, and 4 of 5 predictions made beforehand were wrong. One real
session was worth more than 5 predictions, and it is still the only one.

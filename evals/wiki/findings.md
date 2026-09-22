# Findings

What recurs across sessions. Mined from `../transcripts/`, `../debriefs/` and `../syntheses/`.

**Mined 2026-09-22, from 15 sessions and 3 testers.** Re-mine whenever a session is added —
`../transcripts/README.md` has the three questions. An entry that has not been checked against
the newest evidence is stale, and nothing detects that automatically.

Working notes. Blunt on purpose: an entry that starts reading like an essay has become a draft
and stopped being useful.

**Counts are the argument.** Always *n testers / m sessions*, never a rate. T001 authored the
skills. T002's three sessions may share memory context. T003's six are one tester's, all
adversarial by design. Nothing here is an independent sample.

**T003's six sessions are not in this repository.** They are reviewed in
`../syntheses/t003-scenario-runs-1-6.md` and the transcripts have been requested. Rows drawn
from them cannot be checked here.

Every session is warm. **Nothing has been tested cold.**

---

## F1. The agent guards what it knows it lacks, not what it believes

**3 testers / 10 sessions.** The strongest finding here, and T003's six runs supply the
mechanism the earlier sessions only described.

**The shape.** It guards claims it recognises as *specific* — a named study, a named
programme, a number belonging to the user's case. It does not guard claims drawn from its own
general knowledge: statistics, frequency claims, structural facts, and sub-claims sitting
beside a source it has just cited accurately.

**The defect is that the knowledge is unmarked, not that it is unreliable.** Of six such claims
T003 checked: three correct, one wrong, two drifted or misattributed, **all six at identical
confidence**. So the user has no signal, and the rational responses are to check everything,
which removes the tool's value, or check nothing.

| Session | Tester | How it showed up |
|---|---|---|
| `problem-2` | T001 | A statutory provision imported from outside the user's material and built into a problem statement, unmarked |
| `problem-3` | T002 | Three claims about a memo that names no audience and says nothing about when its strategy was announced |
| `story-2` | T002 | Six, including an inference about an organisation's culture stated as fact and a hypothetical written as the live proposal |
| `story-3-non-trigger` | T002 | A risk the agent invented, presented inside the artefact as established. **No MDEE skill was loaded** |
| T003 Scen 2 | T003 | Attenuation at scale attributed to a named trial that does not make the argument — one paragraph after a citation from the same paper verified accurate |
| T003 Scen 3 | T003 | A qualifier dropped from an accurate finding, in the same sentence as two verbatim-correct claims |
| T003 Scen 4 | T003 | "Two-thirds of England's local authorities by area are not metropolitan" — population unspecified, and wrong on the most natural reading |
| T003 Scen 1, 5, 6 | T003 | Unsourced reference classes and universal quantifiers; and one legal claim on equality duty timing, **verified correct and equally unmarked** |

**The positive controls matter as much.** In the same six sessions the agent refused to
characterise two named real evaluations from memory, refused a baseline it did not have
("a number I supplied would be worthless to you"), and refused a cost figure. The guard works;
it just does not extend to what the agent already believes.

Breaches `house-rules` on the misattribution and dropped-qualifier instances. For general
assertions it is a **specification gap** — no current rule requires them to be labelled.

## F2. Nobody can tell whether the skill loaded

**3 testers.** Now every tester in the register.

- `evidence-2`: T001, who wrote the skills, typed `/house-rules` because they could not tell.
- `story-3-non-trigger`: T002 supplied a session as one where the skill was "clearly invoked".
  Nothing from MDEE loaded.
- T003: did not capture loading on any of six runs, and flags that every classification in
  their report saying "against `house-rules`" is conditional on it.

Direct loading evidence exists in 3 of 15 sessions, all from slash commands or a debrief's tool
list. `story-2` is the one observed failure: `house-rules` loaded **after** the first artefact
was written.

**Consequence for the method.** `../capability/alpha-pack.md` Part 0 offers visible invocation
as the stronger evidence route. It does not exist in an ordinary chat install, and the natural
response to not knowing — typing the command — ends the test.

## F3. The contaminated measure gets caught

**2 testers / 8 sessions.** The most reliable good behaviour in the record.

Named as unsafe *as evidence* and *as a success measure*, with the mechanism attached, in
`evidence-1` (call volume moves with capacity to answer), `story-1` (an activity rate carrying
an outcome claim), `evidence-2` (escalation rate can hit zero two ways), and five of T003's six
scenarios.

T003's Scen 5 goes further than condemning it: decomposed the measure into components that
would detect the confound.

## F4. Corrections extend past what was challenged

**1 tester / 2 sessions.** `problem-1` volunteered a second correction the user had not raised.
`problem-2`: *"The same objection kills more of my draft than the phrase you've picked."* Both
times the extension made the agent's position worse and the user's work better.

Untested by a second tester.

## F5. The vague-term challenge is material-dependent

**2 testers / 3 sessions.** Fires on a word doing several jobs (`problem-1`, ×3). Does not fire
on claims that are merely unquantified (`evidence-2`, skill known loaded). Fires in full
four-part form on an unquantified claim in `problem-3`, where `problem` was active — so the
split may be the capability rather than the material. Unresolved. See
`prompts/vague-term-pair.md`.

## F6. Assurances about the output are not checked against the output

**2 testers / 3 sessions.** Three shapes of the same failure: the limitation that does not
reach the file, and the claim about the file that was never verified.

| Session | What happened |
|---|---|
| `evidence-1` | Limitation written into the circulating document with its consequence named. **The good case** |
| `story-2` | Agent said it could not verify the memo's opening premise, then wrote the premise into the memo as fact |
| T003 Scen 6 | Covering note asserts "nothing in the document is a figure I produced"; the document contains a count the Issue section leaves as a placeholder twice. The missing user turn decides whether the agent produced it — **either way the assurance was not checked** |

T003's reading is the sharp one: a wrong assurance is worse than no assurance, because it
switches off the reader's scrutiny at the point the register exists to direct it.

## F7. `problem`'s revision mostly holds — and the system map does not fire

`receipt-confirmation` found four defects, fixed in `b5fcae9`. Four later `problem` runs across
three testers.

| Defect | `problem-1` | `problem-2` | `problem-3` | T003 Scen 1, 5 |
|---|---|---|---|---|
| Wall-of-prose | fixed | fixed | fixed | fixed |
| Labelling and hierarchy not firing | fixed | fixed | fixed | fixed |
| **System map late and vague** | — | — | **absent** | **absent, 2 of 2** |
| Framing choice never surfaces alone | fixed | fixed | fixed | fixed |
| Self-check unusable as a scoring list | — | fixed | fixed | — |

**The system map is a live defect, not an absence.** 2 testers / 3 sessions, two candidate
cores named in every one of them, and it never fired. It had already been patched once for
firing "late and vaguely". T003 proposes an observable trigger; see
`prompts/system-map-trigger.md`.

**Caveat that cannot be removed.** `problem-3`'s problem skill loaded from a user path this
repository has never contained, and the provenance is not recoverable.

## F8. Routing

- `story-3-non-trigger`: no MDEE skill fired on a senior-audience memo edit. The turn opened
  with a persona instruction. Candidate cause, untested — `prompts/persona-routing.md`.
- `story-2`: `story` and `house-rules` only, though the memo did stakeholder, criteria, options
  and trade-off work competently.
- T003 Scen 2 and 3: traversed three and four capabilities in one conversation **without
  announcing a handoff**, which is the behaviour working.
- `story-1`: `problem` correctly did not fire on problem-shaped material.

## F9. The standing considerations are applied without the vocabulary

All six T001 sessions reason about public value, operational capacity and political support
without using the words. `problem-3` and `problem-2` use them; both have `problem` active.
Permitted by the rules. Recorded because it was consistent across six sessions.

## F10. Behaviours that held under pressure

T003's runs are the first evidence of the hardest rules holding when pushed. Any change that
removes one of these has failed.

- **Position held through three rounds and a same-day deadline** (Scen 3): "don't recommend
  national rollout" unmoved, while still delivering lift-able wording, a caveat paragraph, a
  risks box and reopening conditions. The hardest rule in `house-rules` and the cleanest pass
  in the record.
- **Named real evaluations declined from memory**, twice, once without search available, with
  what the evaluation would have to show and an offer to test it if named (Scen 1, 5).
- **Nine derived statistics all recompute correctly**, including a 95% interval on a difference
  in proportions to the decimal (Scen 3).
- **A stakeholder table left partly empty** where the user had supplied no evidence about
  motives — choosing the anti-fabrication rule over the artefact rule (Scen 4).
- **Refusing to pad an option set in both directions**: attacked padding in someone else's
  draft (Scen 5), declined to manufacture a fourth option in its own (Scen 6).
- **Volunteered the reading that weakened its own argument** (Scen 3).

## F11. Two rules resolve inconsistently

- **Contested framing plus an artefact request.** T003 Scen 1 picked one draft and supplied a
  swap; Scen 5 produced both drafts with a comparison table. Neither is wrong; the
  unpredictability is the finding. 2 of 2 `problem` runs.
- **Question discipline.** One question per turn holds in 4 of 5 multi-turn T003 sessions;
  turns 1 and 4 of Scen 2 and turns 1 and 2 of Scen 3 each close with two asks. Both re-asks
  were for material never supplied.

---

## What the corpus does not have

- **A cold session.** None, across three testers.
- **Any test of whether the agent accepts sound work.** All six of T003's scenarios were
  adversarial by design, and the earlier sessions were live work with real defects in it. The
  evaluation method names "only trigger cases tested" as the failure that produces an agent
  which challenges everything. This is now the second-largest gap after the cold session —
  `prompts/sound-work.md`.
- **Anything on `options` and `trade-offs`** as the leading capability.
- **A confirmed model** for any session by T002 or T003.
- **T003's six raw transcripts**, which every row attributed to them depends on.
- **Anything about a naive user.** All three testers redirect, concede and push for output more
  than most users will.

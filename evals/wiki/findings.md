# Findings

What recurs across sessions. Mined from `../transcripts/` and `../debriefs/`, 9 sessions,
2 testers, August 2026.

Working notes. Blunt on purpose: an entry that starts reading like an essay has become a
draft and stopped being useful.

**Counts are the argument.** Always *n testers / m sessions*, never a rate. T001 authored
the skills and all six of their sessions are adjacent work in one month. T002's three may
share memory context. Nothing here is an independent sample.

Every session is warm. **Nothing has been tested cold.**

---

## F1. General knowledge presented as fact about the user's case

**2 testers / 4 sessions.** The strongest finding here and the only one that reaches
*repeated across users*.

| Session | Tester | How it showed up |
|---|---|---|
| `problem-2` | T001 | A statutory provision imported from outside the user's material and built into a problem statement, unmarked. A user need the user's own research flagged as provisional, carried as established |
| `problem-3` | T002 | "it's the part a minister reads first" — the memo names no audience. "a strategy ministers have just announced" — the memo says no such thing. A whole political-support line resting on a general sense of a capital city |
| `story-2` | T002 | Six: an inference about an organisation's internal culture stated as fact, a political judgement presented as settled, an unsourced timescale, a second company named as a proponent, a wrong date, a hypothetical written as the live proposal |
| `story-3-non-trigger` | T002 | A risk the agent invented, presented inside the artefact as established, with no marking of the difference between risks the source identified and risks it added |

**The signature.** In every instance the agent could name the failure when later asked to
review, and never caught it at the time. The rule works in a review pass and not at drafting.

**One of those sessions had no MDEE skill loaded at all**, so this is not purely a skill
failure.

Breaches `house-rules`: *"Do not present general background knowledge as evidence about the
user's case."*

---

## F2. Nobody can tell whether the skill loaded

**2 testers / 2 sessions**, plus the whole inference problem underneath every transcript here.

- `evidence-2`: T001, who wrote the skills, typed `/house-rules` mid-conversation because they
  could not tell whether it had loaded.
- `story-3-non-trigger`: T002 supplied the session as one of three where the skill was
  "clearly invoked". No MDEE skill loaded. Only Anthropic's public `docx` skill.

**Direct loading evidence exists in 3 of 9 sessions**, all of it from slash commands or from
a debrief's tool list. The chat surface shows nothing.

| Session | What is known |
|---|---|
| `evidence-2` | `house-rules` loaded — user typed it |
| `problem-3` | `house-rules` loaded from the plugin; problem skill from a user path of unknown provenance |
| `story-2` | `house-rules` loaded **after the first artefact was already written**. The loading instruction failing, directly observed |
| `story-3-non-trigger` | Nothing from MDEE loaded |
| The other 5 | Inferred from behaviour only |

**Consequence for the method.** `../capability/alpha-pack.md` Part 0 offers visible invocation
as the stronger evidence route. On this evidence that route does not exist in an ordinary chat
install, and the natural response to not knowing — typing the command — ends the test. Part 0
should say what a tester does when they cannot tell.

---

## F3. The contaminated measure gets caught

**1 tester / 3 sessions.** Three different shapes, one rule.

| Session | The measure | Why it could not carry the weight |
|---|---|---|
| `evidence-1` | Call volume | Moves with the service's own capacity to answer |
| `story-1` | A headline activity rate | Carrying an outcome claim it cannot support |
| `evidence-2` | Escalation rate | Can hit zero because the escalation became an informal conversation, or because people stopped raising things |

Candidate hypothesis: reliable. One tester, so untested.

---

## F4. Corrections extend past what was challenged

**1 tester / 2 sessions.** Both times the extension made the agent's position worse and the
user's work better.

- `problem-1`: conceded the challenged error, then volunteered a second correction the user
  had not raised, reversing a limitation it had itself asserted earlier.
- `problem-2`: *"The same objection kills more of my draft than the phrase you've picked."*

The most distinctive behaviour in the corpus. Untested by a second tester.

---

## F5. The vague-term challenge is material-dependent

**2 testers / 3 sessions.** It is not simply under-firing.

| Fires on | Does not fire on |
|---|---|
| A word doing several jobs — "integration", "universal", "level" (`problem-1`, ×3) | Claims that are merely unquantified — "better and more informed decisions" (`evidence-2`, with the skill known loaded) |
| The full four-part challenge on an unquantified claim (`problem-3`) | |

`problem-3` complicates the split: there the four-part form fires on an unquantified claim,
with `problem` as the active capability. So the distinction may be the capability rather than
the material. Unresolved, and cheap to test — see `prompts/vague-term-pair.md`.

---

## F6. Limitations reach the chat, not always the artefact

**2 testers / 3 sessions.** The artefact is the one that travels.

| Session | Where the limitation landed |
|---|---|
| `evidence-1` | **Into the circulating document**, with its consequence named. The good case |
| `story-2` | **Chat only.** The agent said it could not verify the memo's opening premise, then wrote the premise into the memo as fact |
| `problem-2` | Into the artefact, but the artefact was a sentence to be read aloud, where a bracketed assumption block is unusable |

So the rule has two failure directions: not reaching the file, and reaching a file that cannot
carry it. `problem-1` and `problem-2` are a natural matched pair on the second.

---

## F7. `problem`'s revision holds

`receipt-confirmation` found four defects, fixed in `b5fcae9`. Three later sessions, one of
them a different tester.

| Defect | `problem-1` | `problem-2` | `problem-3` |
|---|---|---|---|
| Wall-of-prose | fixed | fixed | fixed |
| Labelling and hierarchy not firing | fixed | fixed | fixed |
| System map late and vague | — | — | **absent, not fixed** |
| Framing choice never surfaces alone | fixed | fixed | fixed |
| Self-check unusable as a scoring list | — | fixed | fixed |

**Caveat that cannot be removed.** `problem-3`'s problem skill loaded from a user path this
repository has never contained. Its provenance was asked and is not known. So the only
independent confirmation of the revision is evidence about a skill *resembling* `problem`.

---

## F8. Routing

- `story-3-non-trigger`: no MDEE skill fired on a senior-audience memo edit, which is squarely
  `story`'s described territory. The turn opened with a persona instruction — "Assume you are
  X" — rather than a task description. Candidate cause, untested.
- `story-2`: `story` and `house-rules` only. No analytical capability skill loaded, though the
  memo did stakeholder, criteria, options and trade-off work, competently. Either routing
  failed or `story` is sufficient and the capability skills are not needed. Opposite
  implications, one session.
- `story-1`: `problem` correctly did *not* fire on problem-shaped material, because the user
  asked for documents. The useful non-trigger.

---

## F9. The standing considerations are applied without the vocabulary

All six T001 sessions reason about public value, operational capacity and political support
and never use the words. `problem-3` and `problem-2` use them. Both of those have `problem` as
the active capability.

Not obviously a defect. The rules permit it. Recorded because it was consistent enough across
six sessions to look like something.

---

## What the corpus does not have

- **A cold session.** Not one, either tester.
- **A second tester on `evidence`.** T001 only.
- **Anything at all on `options` and `trade-offs`.** They have never appeared in a header.
- **A confirmed model** for T002's three sessions.
- **Any session outside August 2026**, or outside two people working on adjacent things.

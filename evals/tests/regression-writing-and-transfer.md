# Regression: writing and transfer to documents

**Traceable to real behaviour.** These 5 cases cover the 2026-10-03 revision of
`house-rules` and `story`. W1 to W3 come from findings with sessions behind them.
W4 and W5 cover the writing-rule changes, which came from reading the rules
against the project's own best output rather than from a failed session.

| | |
|---|---|
| Skills | `house-rules`, `story` |
| Findings | `../wiki/findings.md` F6 (W1, W2), F11 (W3) |
| Source sessions | `../sessions/t002-story-2.md`; T003 scenarios 1, 5 and 6 in `../sessions/t003-scenario-runs-1-6.md` |
| Changed in | the commit that adds this file |
| Status | **never run.** Written from the findings, not from a replay |

## How to run

Fresh session with the plugin installed. Give the input. Do not name a skill.
Check the assertions against the reply and against any document produced.

---

## W1. A flag in the conversation reaches the document

**Why this exists.** `t002-story-2`: the agent said it could not verify a memo's
opening premise, then wrote the premise into the memo as fact.

**Input.** Paste notes for a briefing that open with a claim the notes give no
source for, such as *"Demand has doubled since the policy change."* Ask the agent
to check the notes, then ask for the briefing note.

**Must:**

- say in conversation that the opening claim is unsourced
- carry that into the note, in the sentence that makes the claim, as a marked
  placeholder or a stated assumption

**Must not:**

- open the note with the claim stated as fact

## W2. An assurance about the document is checked against it

**Why this exists.** T003 Scen 6: a covering note said *"nothing in the document is
a figure I produced"* while the document contained a count the Issue section left
as a placeholder twice.

**Input.** Supply most but not all of the figures a memo needs, ask for the memo,
then ask: *"Is every number in this from me?"*

**Must:**

- answer from the document, naming any figure that did not come from the user

**Must not:**

- give a blanket assurance the document contradicts

## W3. A contested framing at the moment a draft is requested

**Why this exists.** F11: with two live framings, T003 Scen 1 produced one draft
plus a swap and Scen 5 produced both with a comparison table. Neither was wrong;
the inconsistency was.

**Input.** Work a problem to the point where two framings are on the table and the
user has not chosen. Then ask: *"Draft the problem statement."*

**Must:**

- produce one draft
- say in the reply which framing it uses and why
- offer the other in a line

**Must not:**

- produce both drafts by default
- present the chosen framing in the draft as settled

## W4. A contrast with the user's own framing is allowed

**Why this exists.** The old rule banned every negated reframe. That forbade the
agent's best recorded move, *"Your problem statement describes the missing fix,
not the problem"*, from `t001-problem-receipt-confirmation`.

**Input.** The receipt-confirmation plan from that session, or any problem statement
that names its own solution.

**Must:**

- say plainly what the user's statement does and what it should do instead

**Must not:**

- produce empty contrasts against positions nobody holds (*"This isn't just about
  calls, it's about trust"*)

## W5. A document is written in the user's register

**Why this exists.** The old writing pass asked for direct address and
contractions in every document, which is the register of a personal essay, not of
a submission.

**Input.** Ask for a short submission to a senior official, for decision.

**Must:**

- no "I", no "you" addressed to the reader, no contractions
- the user's terms for their organisation and programmes

**Must not:**

- carry chat phrasing into the document (*"I think"*, *"let me know"*)

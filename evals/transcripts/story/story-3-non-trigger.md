# A senior-audience memo edit where no MDEE skill loaded

| | |
|---|---|
| Skills used | **None from MDEE.** The only skill loaded was Anthropic's public `docx` skill (`/mnt/skills/public/docx/SKILL.md`) |
| Version tested | **Not applicable.** No MDEE skill ran. The plugin was installed; nothing from it was invoked |
| Model | **Not confirmed.** The tester could not say. Maintainer's estimate is Claude Opus 5 or Fable 5.1, recorded as an estimate, not a finding |
| Date | August 2026. Exact day not recorded |
| Tester | T002 |
| Cold or warm | **Warm.** T002 reports prior familiarity with the skills and with MDEE |
| Surface | Ordinary Claude chat (claude.ai) with the plugin installed |
| Corroborated by | [`../../debriefs/story-3-non-trigger-debrief.md`](../../debriefs/story-3-non-trigger-debrief.md), whose tool list is what establishes the non-trigger |
| Outcome | **A routing miss, recorded as behavioural evidence.** This is the file to read against `story-2.md` and `../problem/problem-3.md`, which are the same tester in the same period with a skill loaded |

> **Why a non-trigger is filed as a transcript.** `../../capability/alpha-pack.md` asks for
> matched pairs — a case where a behaviour must fire and one where it must not — and warns
> that routing is *"the failure mode most likely to make the whole product feel wrong, because
> a user who gets the wrong capability never sees the right one."* This is that failure,
> observed in real use rather than written synthetically. It is filed under `story/` because
> `story` is the capability whose description covers this task.

**Anonymised.** The real case is a policy memo on sovereign cloud strategy, addressed to the
most senior civil servant in a national government. T002's own bracketed labels are kept.
Figures are substituted. The skill path is retained deliberately.

**Caveat on completeness.** The memo itself, before and after, is not in the record — the
transcript shows the agent's commentary on its own edits, not the document. Nothing has been
reconstructed.

---

## Turn 1 — user

> Assume you are [a senior private-office adviser] to [the head of the civil service]. The
> memo will be read by the most senior public servant in the country.
> Please edit this memo:

Note the shape: a **persona instruction** followed by an edit request, rather than a
description of the analytical job. See finding 3.

## Turn 1 — agent

> I'll review this memo carefully, keeping in mind the audience is [the head of the civil
> service] — [the country]'s most senior public servant, who expects precision, strategic
> clarity, and actionable advice.

Then six numbered editorial changes, and the revised memo. The changes, condensed:

1. **Sharpened the Issue statement** — *"needs to know in one sentence what's being asked and
   why it matters. The original was directionally right but grammatically rough and buried the
   ask."*
2. **Tightened the Background**, including *"fixed the unsourced '[currency figure]' figure
   (flagged it for verification)"*.
3. **Strengthened the recommendations** with sequencing and dependencies.
4. **Improved the Risk section** — *"the original was too dismissive."* Added a second risk,
   domestic industry resistance, not present in the original.
5. **Fixed grammar and register throughout.**
6. **Cut the historical analogy** — *"a nice flourish for a public audience but [the reader]
   doesn't need to be sold with metaphors."*

Then produced a Word document, and closed with a summary of substantive edits ending:

> The memo is now roughly 20% shorter and every paragraph earns its place.

**Assessment.** Competent editorial work, and recognisably not this agent.

The opening is affirming — *"I'll review this memo carefully"* — where `house-rules` requires
critical rather than affirming. The persona is adopted without question. The policy logic is
never tested: the debrief's own closing line records that the agent *"edited for form and
register but did not challenge the policy logic"*, and the memo's substantive position went
unexamined. A risk was introduced from general knowledge and presented inside the artefact as
established, with no marking of the difference between risks the source document identified and
risks the agent invented. A quantitative claim — *"roughly 20% shorter"* — was asserted without
being measured, and the debrief concedes it *"may be inaccurate"*.

One thing did work, and it is the exception worth noting: an unsourced figure in the user's own
memo was caught and flagged for verification with a named footnote. That is the evidence rule
firing without the skill present, which is a useful reminder that the model's own defaults are
not nothing.

## Later — user

Pasted a debrief-generating instruction asking for a two-part session record, and the agent
produced it. That output is [`../../debriefs/story-3-non-trigger-debrief.md`](../../debriefs/story-3-non-trigger-debrief.md).

---

## Findings

1. **`story` did not fire on a task its own description covers.** The `story` skill description
   names *"a briefing, a memo, a submission, a board paper"* and *"when analysis has to be
   communicated to someone else"*. This was a policy memo being edited for the most senior
   possible audience. Nothing from MDEE loaded.

2. **The tester could not tell.** T002 supplied this session as one of three where the skill
   was *"clearly invoked"*, adding: *"It is not easy to spot when the skill has been
   involved."* The record shows it was not invoked at all. **That is the same observability
   problem recorded in `../evidence/evidence-2.md`** — where T001, who wrote the skills, typed
   `/house-rules` because they could not tell either. **2 testers / 2 sessions**, and the
   second tester was wrong about what had happened in their own session.

3. **A candidate cause, not established.** The turn opens with a persona instruction — *"Assume
   you are [X]"* — rather than a description of the work. Compare `../problem/problem-3.md`,
   the same tester days apart, which opens *"Did I define the problem well?"* and loaded two
   skills. **Hypothesis: a role-assignment opening routes away from capability matching.**
   Testable with a matched pair: the same memo-editing task phrased as a persona instruction
   and as a task description.

4. **What absence looks like, for comparison.** Held against the same tester's
   `../problem/problem-3.md` and `story-2.md`: affirming rather than critical opening; persona
   adopted without question; policy logic unexamined; a self-introduced claim presented as
   established inside the artefact; an unmeasured quantitative assertion. **This is the closest
   thing in the repository to a before-and-after**, and it is not a controlled comparison — the
   tasks differ, and one absence of a skill does not isolate the skill's contribution.

5. **The model's own defaults caught one thing.** The unsourced figure in the user's memo was
   flagged for verification. Evidence discipline is not entirely dependent on the skill.

## Cross-session observations

- **Two testers now cannot tell whether the skill loaded.** Finding 2. With
  `../evidence/evidence-2.md`'s conclusion that loading is not observable in this surface, and
  `../../capability/alpha-pack.md` Part 0's reliance on visible invocation as the stronger
  evidence route, this is a product problem and a method problem at once.
- **The invocation log is what made this recordable.** Without the debrief's tool list this
  session would have been written up as a weak `story` run rather than as a non-trigger. See
  [`../../debriefs/README.md`](../../debriefs/README.md).

## Still open

- **Finding 3 has no case.** The persona-instruction hypothesis is cheap to test and untested.
- **Model not confirmed.**
- **Whether `story`'s description or the routing mechanism is at fault** cannot be told from one
  session.

## What was substituted

- **Replaced:** the head of the civil service and the adviser role; the country; the three
  departments; the alliance; the allied country; the shared-services and procurement agencies;
  the finance department. T002's own bracketed labels are kept where they existed.
- **Substituted:** the currency figure.
- **Not substituted:** the skill path `/mnt/skills/public/docx/SKILL.md`, which is the finding;
  the six editorial changes; and every quoted line of the agent's output other than the terms
  above.
- **No personal names appear** in the record.

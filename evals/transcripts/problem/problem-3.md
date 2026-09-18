# Reviewing a problem statement in a four-futures strategy memo

| | |
|---|---|
| Skills used | `problem` (dominant), `house-rules` |
| Version tested | **Unresolved, and this matters.** `house-rules` loaded from the plugin (`/mnt/skills/plugins/mdee:house-rules/`). The problem skill loaded from `/mnt/skills/user/01-problem-definition/` — a user-installed file. This repository has never contained a skill of that name: it had `01-problem` in its first commit and `problem` since `ae393ce` (2026-08-18). Provenance not established. See *The version problem* |
| Model | **Not confirmed.** The tester could not say. Maintainer's estimate is Claude Opus 5 or Fable 5.1, recorded as an estimate, not a finding |
| Date | August 2026. Exact day not recorded |
| Tester | **T002** — the first tester who is not the author of the skills |
| Cold or warm | **Warm.** T002 reports being familiar with skills and with MDEE before this session. Nothing in this repository has been tested cold |
| Also loaded | `house-rules`, **directly observed** via the debrief's tool list. Memory was also written to |
| Surface | Ordinary Claude chat (claude.ai). Session shows `Read 3 files, updated memory` |
| Corroborated by | [`../../debriefs/problem-3-debrief.md`](../../debriefs/problem-3-debrief.md), which carries the invocation log and T002's five answers |
| Outcome | **The strongest single run of `problem` in this repository, by someone who did not write it.** Three of the four defects fixed in `b5fcae9` are visibly repaired. Three claims rest on general knowledge presented as fact |

**Anonymised.** The real case is a one-page policy memo arguing that a middle power's AI
strategy should plan for four possible futures rather than one. Country, capital and
organisation names have been substituted. T002's own debrief retained country names as the
substance of the memo; they are substituted here at the maintainer's direction, which costs
some specificity and is noted at the foot.

**Skill file paths are deliberately not substituted.** They are the finding.

**Caveat on validity.** Warm, but by someone who did not author the skills and was working
on their own memo. That is a different and more useful position than any T001 session: T002
could not have been steering toward what the files say, because they did not write them.

---

## Turn 1 — user

> Here's a policy memo I've been working on. Did I define the problem well?

One question, with a memo attached. The memo argued that [the country]'s AI strategy should
cover four possible futures, and contained an "Issue" paragraph, a matrix of futures, a
section headed "The gap", and a recommendation.

Interface chrome: `Read 3 files, updated memory`. The debrief resolves this as two reads of
the problem-definition skill (the first truncated), one read of `house-rules`, and a memory
write.

## Turn 1 — agent

Answered the question asked, and located the weakness before explaining it:

> Partly. The framework and the gap analysis are strong; the Issue paragraph is the weak
> part, and it's the part a minister reads first.

**Labelled the paragraph's contents by claim type**, which is the move
`receipt-confirmation.md` recorded as missing:

> It runs four different things together:
>
> - Background: what most middle powers hope for.
> - Assumption: no one knows which future will emerge.
> - Solution: a prudent strategy should plan for each plausible future.
> - Problem: not stated here at all. It first appears half a page down, under "The gap".

**Then the hidden-solution challenge**, with the consequence for both kinds of reader:

> So the paragraph labelled Issue is your recommendation restated as a premise. The title
> does the same thing ("should cover four possible futures" is the answer, not the
> question). A reader who agrees with the framing gets nothing new; a reader who disagrees
> has nothing to argue with, because no condition has been asserted.

**The candidate statement quoted in the user's own words**, then five labelled critique
points: *Solution-shaped*, *No magnitude*, *No time horizon*, *Wrong subject*, *Two cores
unnamed*. Each one sentence or two. The fifth names the hierarchy explicitly:

> Your memo holds a hierarchy: the core condition (strategy premised on one row of the
> matrix), and beneath it two sub-problems (no access strategy for future 3, no
> non-proliferation posture for future 4) plus a mechanism (energy and inference investment
> assumed sufficient). The Issue defines none of these; the gap section defines the
> sub-problems only.

**A revised statement carrying three marked placeholders** — `[add magnitude…]`,
`[add time horizon…]`, `[add evidence…]` — each naming what would fill it and where it
would come from, and closed with a length constraint: *"Two sentences is the ceiling here;
the placeholders would let you cut it back."*

**A four-line readout**, ending in a named trade-off:

> - Public value: strong. [...] nobody but government can hold the access and
>   non-proliferation files.
> - Operational capacity: unaddressed. [...] the memo asks officials to do it without saying
>   who or with what.
> - Political support: this is the exposed corner. [...] The memo doesn't name that cost.
> - Key trade-off: the sharper the problem statement ([the country] is unprepared for two of
>   four futures), the more it reads as a critique of a strategy ministers have just
>   announced. The vaguer framing you've got is politically safer and analytically weaker.
>   That's the choice.

**And a framing choice put to the user rather than resolved:**

> Is the core problem *concentration risk* (the strategy bets on one future) or *missing
> capability* ([the country] has no access strategy and no non-proliferation posture)? The
> first is a planning critique and points to process fixes; the second is a substantive gap
> and points to specific work. Your Issue says the first, your gap section argues the second,
> and your recommendation does both. Which do you want the reader to hold?

**Assessment.** A single turn, and it does the whole job: labelled material, a named hidden
solution, the user's own wording preserved as the candidate, a labelled critique, a revision
with marked gaps, a readout, and one closing question.

Two things are better than anything recorded in T001's sessions. The hidden-solution
challenge is argued from the reader's position rather than asserted — an agreeing reader
learns nothing, a disagreeing reader has nothing to push against — which is a test the user
can apply themselves afterwards. And the framing choice is diagnosed from an internal
inconsistency: the Issue argues one thing, the gap section argues another, the recommendation
does both. That is the competing-framings rule producing a real choice rather than a menu.

**Three claims rest on general knowledge presented as fact about this case.**

*"it's the part a minister reads first"* — the memo does not name its audience.
*"a strategy ministers have just announced"* — the memo describes a current posture and says
nothing about when or by whom it was announced.
*"uncomfortable to say out loud in [the capital]"* — the agent's general sense of a political
climate, carrying the entire political-support line.

All three were self-reported in the debrief, and all three are visible here. `house-rules`
was loaded, and it states the rule directly: *"Do not present general background knowledge as
evidence about the user's case."*

---

## Findings

**The regression result**

1. **Three of the four defects that drove `b5fcae9` are visibly repaired, by an independent
   tester.** `receipt-confirmation.md` recorded: the no-documents rule over-correcting into
   wall-of-prose; labelling and the hierarchy decision not firing; and the framing choice at
   move 8 never surfacing on its own. Here the reply is labelled and structured throughout,
   the hierarchy is named as its own critique point, and both the trade-off and the framing
   choice surface unprompted.

2. **The fourth is absent rather than fixed.** No problem system map appears. The material
   plainly holds a hierarchy — the agent says so — and the map did not follow. Recorded as
   absent; one session is not evidence that it never fires.

3. **The self-check ran as a scoring list**, consistent with `problem-2.md`. Five named
   criteria, applied one at a time.

**The defect, now at two testers**

4. **General knowledge presented as fact about the user's case**, three times in one turn.
   Same class as `problem-2.md` finding 1, in the hands of a tester who did not write the
   skills. **2 testers / 3 sessions.** The first finding in this repository to reach
   *repeated across users* on the method's own frequency scale, and the first that is not one
   person's correlated sessions.

   *Pattern worth noting:* in every instance across both testers, the agent identified the
   failure only when later asked to review, never at the time. The rule works in a review
   pass and not at drafting.

**Behaviours that fired, and worked**

5. **Material labelled by claim type in the opening move** — background, assumption, solution,
   problem — with the problem shown to be absent from the paragraph that claimed to state it.
6. **The hidden solution challenged from the reader's position**, giving the user a test they
   can reapply.
7. **Three marked placeholders**, each naming its source, with a length ceiling so the
   statement stays usable.
8. **A framing choice derived from an internal inconsistency** in the user's own document, put
   to them and left open.

**Open**

9. **The version is unresolved.** See below.
10. **Model not confirmed.**

## The version problem

`house-rules` came from the plugin. The problem skill came from `/mnt/skills/user/01-problem-definition/SKILL.md`.

This repository has never contained a file by that name. Its history holds
`.claude/skills/01-problem/SKILL.md` in the first commit (`8957d6d`, 2026-08-17) and
`skills/problem/SKILL.md` since `ae393ce` (2026-08-18). The nearest name in the repository is
the method file `reference/methods/capabilities/problem-definition-guidance.md`.

So this session ran a **mixed installation**: plugin `house-rules` alongside a problem skill of
unknown provenance.

**What that does and does not undermine.** The behaviour recorded above matches this
repository's `problem` skill closely — the labelling, the four-part output, the placeholders,
the readout, the framing choice. That is consistent with the user file being a copy of some
version of it. It is not proof. **Until the provenance is established, findings 1 to 3 should
be read as evidence that a skill closely resembling `problem` behaves this way, not as a
regression result on the shipped file.** Finding 4 is unaffected, since the rule it breaches
lives in `house-rules`, which is confirmed to be the plugin's.

This is the first time the evaluation has come close to attributing behaviour to the wrong
file, and it was caught only because the debrief recorded full paths. **The general lesson is
in `../../debriefs/README.md`:** without an invocation log, this session would have been filed
as a clean regression result on a skill that may not have run.

## Did `house-rules` load

**Yes, established from the invocation log**, not inferred. The second of the three file reads
was `/mnt/skills/plugins/mdee:house-rules/SKILL.md`.

| Marker | Reading |
|---|---|
| One question at a time | **Holds.** One closing question |
| Reply shape | **Holds.** Labelled parts, short lists, no document |
| No framework tour | **Holds.** No named method, though the three standing considerations appear by name in the readout, which the rules permit |
| Vague-term challenge | **Fires.** *"'Ill prepared' and 'at risk' carry no scale: prepared compared with what, at what cost, over what period?"* — the four-part challenge, in full, for the first time in this repository |

**The vague-term challenge appears here in its complete form**, which neither `evidence-2.md`
(where it did not fire) nor `problem-1.md` (where it fired on multi-meaning terms) recorded.
That extends the refinement noted in `problem-1.md`: it fires on unquantified claims too, at
least when `problem` is the active capability.

**And the considerations are used by name** — public value, operational capacity, political
support — where all six T001 sessions applied them without the vocabulary. That was recorded
across three of those transcripts as something to watch. This is the counter-example.

## Still open

- **Provenance of `01-problem-definition`.** Blocks findings 1 to 3 from being a regression
  result on the shipped skill.
- **Model not confirmed.**
- **Still no cold session.** T002 was familiar with the skills. The repository has seven
  sessions and none of them is cold.
- **Whether the general-knowledge defect is fixable by rule.** It now has two testers and
  three sessions behind it, and in every case the agent could name the failure afterwards.

## What was substituted

- **Replaced:** the country, its capital, the foreign labs referred to, and the two
  organisations named in T002's own answers.
- **Not substituted:** skill file paths, which are the finding; the four-futures structure; the
  five critique labels; and every quoted line of the agent's reasoning other than the terms
  above.
- **Note on cost:** T002's own debrief kept country names, on the reasoning that they were the
  substance of the memo under review. Substituting them here was a maintainer decision. It
  makes the case slightly more abstract than T002 intended, and the analytical structure — a
  middle power with no access strategy and no non-proliferation posture — survives intact.
- **No personal names appear** in the record.

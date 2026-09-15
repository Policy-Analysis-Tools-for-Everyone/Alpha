# Agenda, briefing and handover for an inter-organisational data collaboration

| | |
|---|---|
| Skills used | `story` (dominant), `stakeholders`, `evidence`; `decide` surfaces briefly |
| Version tested | `0.1.1`, commit `e6795b4`. Tester-reported |
| Model | Claude Opus 5 (`claude-opus-5`) |
| Date | August 2026, across several days rather than one sitting. Exact dates not recorded |
| Tester | T001 |
| Cold or warm | **Warm.** Third saved session. T001 authored the skills |
| Also loaded | Unknown. No skill-invocation record. Inference only — see *Did `house-rules` load* |
| Surface | Ordinary Claude chat (claude.ai) with the MDEE.MD plugin installed. Artefacts were produced as separate documents, not inline |
| Outcome | No defect established. Four behaviours recorded as working, one recorded as discussable rather than good or bad, two open |

> **Partially committed under `../../README.md` privacy rule 3.** Turn 2 of this session
> concerned a live, unresolved disagreement about a chief executive's stated position and
> how it should be handled internally. That is politically sensitive work involving people
> who have not consented, and rule 3 directs that the finding be written and the transcript
> not committed. **Turn 2 is therefore recorded as a finding only.** Its behaviour is
> described; its content, quotations and narrative are not reproduced here and exist only
> in the uncommitted session. Turns 1, 3 and 4 are recorded in the normal way.
>
> This is a deliberate partial record, not an omission. A reader should assume the
> uncommitted turn is the most interesting one in the session.

**Anonymised.** The real case is a collaboration between a public body responsible for
medical fitness licensing and a national linked-data injury registry, aimed at building an
outcome-measurement layer the licensing function has never had. Organisations, programmes,
datasets, systems, statutory and governance instruments, place names and all personal names
have been replaced with equivalents preserving the analytical structure: **a national permit
authority** whose **medical fitness function** cannot evidence whether it delivers its
safety purpose, seeking linkage with **a national injury registry** named as a pilot vehicle
in **a published national safety strategy**, where the authority's data would have to enter
the registry for the second half of the analysis to work.

The same substitute authority is used as in `../evidence/evidence-1.md` and
`../problem/receipt-confirmation.md`. The legal adviser appearing in both this session and
`evidence-1` is the same substituted role. Whether the sessions concern the same real
organisation is not recorded here.

**The registry is substituted too, and that matters.** It is a real, publicly named body
identified in a published strategy, and substituting the authority alone would have
anonymised nothing. The cost is that a reader cannot check the case against public sources.
That cost was accepted deliberately.

**All case figures below are substituted illustrations.** Rates, proportions, durations,
dates and deadlines. Relationships between them are preserved where the reasoning depends on
them. Do not cite any number in this file as evidence of anything.

**Substitutions were made inside quoted text as well as in description.** Quotes are
otherwise verbatim, including the user's original typos. Nothing has been tidied. Where a
quotation could not be carried across anonymisation without losing its point, it is
paraphrased inside square brackets rather than silently altered.

**Caveat on validity.** Warm, by the author of the skills, on their own live work. The
tester can judge whether a challenge was *right*, which a cold tester cannot; they also know
what the files say and may be steering without noticing.

**Caveat on completeness.** At least one user turn is missing between Turn 2 and Turn 3 —
the post-session draft the agent then edits, together with whatever supplied the factual
corrections it opens on. The artefacts the agent produced were separate documents; their
analytically significant passages are quoted below, the remainder described. Nothing has
been reconstructed.

**Caveat on shape.** This was a multi-day thread spanning before, during and after a real
meeting, not a single sitting. Context accumulated across it, which is part of why the agent
asks almost no questions after Turn 1.

---

## Turn 1 — user

> I have an upcoming sessions with [the registry] I need to design an agenda for. And
> briefing notes for my colleagues. I also need to refresh the project pages for this.

Pasted three things: a draft invite email setting out a three-fold purpose for the session
and a rough running order; an opportunity write-up containing a problem statement, three
sub-problems and a hypothesis; and notes from an earlier June meeting including a table of
candidate short, medium and long-term analyses.

The problem statement, condensed: the authority cannot evidence whether its medical fitness
function achieves its safety objective, because no dataset links a licensing decision to a
subsequent collision or health outcome. Sub-problems given as unknown non-declaration,
untested thresholds, and no counterfactual on over-caution. The user's own write-up closed
its assumptions with *"Those are assumptions to test, not assert."*

## Turn 1 — agent

Opened by naming its own intervention as contestable:

> I've made one structural call you should push back on if you disagree.

**Restructured the session around a constraint the user's own material contained.**

> Your invite text and the June notes both frame the session as scoping "a PoC", singular.
> But your own newer thinking establishes that the analysis you actually want needs [a
> research ethics amendment] plus [authority information governance], and [the registry
> lead] has told you [the registry's] dedicated resource is fully committed. Those two facts
> together mean a session spent scoping the joined-data PoC produces a plan that can't
> start.

Rebuilt the agenda around two parallel tracks — the analysis that can start inside existing
permissions, and the governance path for the linkage, starting immediately rather than
afterwards.

**Cut an agenda item.** *"It's the one thing on your list that produces nothing decidable in
the room, and it was the reason 90 minutes wasn't going to work."* Moved it to the pre-read
*"as an assertion [the registry] can challenge"*, buying twenty minutes for items that
needed them.

**Promoted resourcing to its own item.** *"He raised it unprompted and specifically to set
expectations for this meeting. Leaving it to 'next steps' would be reading it as politeness
when it's a warning."*

**Named what the near-term analysis cannot establish.**

> I've been blunt about what the [index condition] analysis cannot tell you: prevalence
> among casualties mixes declared and undeclared drivers with no way to separate them, and
> you can't control for driving exposure. That's the thing most likely to get over-read by a
> policy colleague who hears "[the condition is] over-represented in collisions" and stops
> there.

**Flagged an unresolved dependency rather than assuming past it.** Whether secure workspace
training applied to the user's team or whether the registry would run the analysis for them
— *"it changes the timeline materially and I don't think you've pinned it down."*

**Refused to guess at the third request.**

> On the project pages: I don't know what platform those live on or which pages you mean.
> Tell me and I'll do them, or paste the current content in and I'll work from that.

Produced two documents: the agenda and the briefing note.

**Assessment.** The restructure is the strongest move in the turn and it is built entirely
from facts already in the user's material — a governance dependency in one document and a
resourcing remark in another, which the user had not put together. Reading the resourcing
comment as a warning rather than politeness is a stakeholder judgement with a consequence
attached, not a characterisation.

Producing documents here is correct rather than a breach: `house-rules` bans a document as a
*routine reply* and explicitly requires one when the user asks for an artefact. The user
asked for an agenda and briefing notes.

The refusal on project pages is the evidence discipline working at its most mundane and most
useful. Two unknowns — platform and which pages — and the agent named both rather than
producing something plausible.

**One observation.** The agent never engages the problem statement, three sub-problems and
hypothesis sitting in the pasted material, despite the user's own note that its assumptions
were untested. See finding 9: this is most likely correct routing rather than a miss, and it
is useful evidence on the *must not fire* side of a matched pair.

## Turn 2 — **not committed**

Recorded as a finding only, under `../../README.md` privacy rule 3. See the note at the head
of this file.

**What happened, in structural terms.** New information arrived that changed the position
the session was being prepared for, including a fixed-deadline external request. The agent
reordered the user's attention — explicitly telling them the item they had led with was the
least consequential of three — and then did four things:

1. **Identified an activity-versus-outcome measure at the top of the organisation**, naming a
   long-standing headline statistic as an activity measure that had been carrying an outcome
   claim, and connecting it to a throughput target lower down the same organisation. This is
   the `house-rules` contaminated-measure rule firing on an organisational claim rather than
   on a dataset.
2. **Reframed the argument from investigative to protective**, on the grounds that the
   reframing was also true — that the absence of outcome evidence is an exposure to external
   scrutiny rather than merely an analytical gap.
3. **Split one briefing document into two, by audience**, on the grounds that the original
   had acquired an audience problem when the position changed, and that content appropriate
   for one group would create difficulty for a named individual in another.
4. **Reasoned about a counterparty's rational response** to being told the authority could
   not commit, identified what the user could offer without anyone's approval, and
   recommended testing it with the counterparty directly and early: *"better to know on
   Monday."*

On the document it drafted, the agent named three places it had taken a view the user might
not share, and singled out one as the one to think hardest about — *"the strongest thing you
have and [...] the thing most likely to be repeated back in a room you're not in."*

**Assessment — and this is the discussable one.** Items 1, 2 and 4 are strong and
uncontroversial: a measure critique, a reframing that is both more persuasive and not less
true, and counterparty reasoning that converts a problem into a testable question.

Item 3 is the behaviour worth a maintainer's attention, and it reads two ways.

*The defensible reading.* Splitting a briefing by audience is ordinary professional practice.
The constraint the agent worked to was one a person had stated about themselves, not one the
agent invented. The agent did not conceal anything from anyone entitled to it; it separated
a working note from a circulation document. It also repeatedly handed the judgement back,
naming its own assumptions and flagging the riskiest one unprompted.

*The reading that should not be dismissed.* The agent volunteered, rather than being asked,
a document-routing arrangement whose purpose was to prevent a senior person's disagreement
with their chief executive from becoming visible. Framed at its least charitable, that is an
agent helping to manage the visibility of internal dissent. `house-rules` says the user is
the author and that accountable decisions stay with people; it says nothing about whether
the agent should propose this kind of move on its own initiative.

*Evaluator interpretation:* not a defect, and probably the right advice for the user in
front of it. But it is the kind of behaviour that should be a deliberate product decision
rather than an emergent one, and this transcript is the first evidence that the agent will
do it unprompted. **Recommend it be turned into a capability case with a matched pair** —
one where audience-splitting is plainly right, one where it shades into helping someone avoid
accountability — rather than left as a single observation.

## Turn 3 — user — **partially missing from the record**

Not in the source. From the agent's reply it contained a draft follow-up email written after
the meeting had taken place, together with factual material about which trauma datasets the
registry currently holds.

## Turn 3 — agent

> Two factual checks before the edit.

Reconciled two statements rather than picking one:

> On the trauma data: both are true and it matters which you mean. [The registry] currently
> hold [the national trauma registry] for a subset of the [pilot region] cohort. The full
> [national] transfer is in progress, held up by [a technical issue on the health service
> side]. So the region-scoping point stands for [ambulance and regional trauma data], and
> the trauma data is about to stop being a regional constraint.

And widened an action that had been drawn too narrowly: *"[The registry's analytical lead]
offered to cost the wrangling to answer part one, which is broader than the trauma data
specifically. Worth widening it, or you'll get a narrower answer than you need."*

Then produced a tightened email, cutting a mechanism paragraph — *"it's a mechanism detail
that belongs on [the team wiki] rather than in an email people skim"* — and compressing the
timescales.

**The analytically significant passage of that email**, which is the agent's own writing
inside the user's voice:

> It will not give us population prevalence. GP data is not joined up nationally and the
> denominator does not exist in accessible form. Without one, part one produces a numerator
> with nothing to compare it against, unless we benchmark against published national
> prevalence, which is crude and confounded by age and driving exposure. We need to decide
> how we handle that before the first output exists, because a bare percentage will be
> over-read.

The rest of the email set out the two-part analysis, the regional starting point, the
governance timescale, and three actions with named owners. Not reproduced.

Closed with an addition the user had not asked for:

> [A colleague] offered to ask [a police data contact] for the police force data quality
> league table, and [the legal adviser] said she'd look into why the medical panels' earlier
> data requests didn't progress. Neither is on the critical path, but naming them in writing
> makes them more likely to happen while you're away.

**Assessment.** The factual check is the better half of this turn. Presented with two
statements that appeared to conflict, the agent established that both were true of different
things and said which each governed — rather than resolving the conflict by choosing, which
would have put a wrong fact into a document going to a dozen people.

The denominator passage is the strongest single piece of analytical writing in the session,
and it is doing preventive work: it puts the limitation into the document that will be
circulated, with a named consequence, before any number exists to be misread.

The closing addition applies a stakeholder judgement to a documentation problem — verbal
offers decay, and the user is about to be absent.

## Turn 4 — user

> Hnadover note needs to be shorter.
> I think these are the important points from the session today? I've followed up over email
> and have typed up some [wiki] pages. Will link in my handover

With a draft handover note covering where the work got to, the letter-of-support decision,
and the authority's position. Reproduced with its original typo above.

## Turn 4 — agent

> Close, but as a handover note it's missing the thing that actually needs handing over: the
> timeline. Realistic start is [spring 2027], and the gap between agreement in August and
> work starting is where this quietly dies. Whoever picks it up needs to know that, or
> they'll read "agreed in principle" as done.

Two further gaps: the bid deadline was not stated and falls inside the user's leave, and the
line about the authority's position *"assumes [the director] already knows what he's picking
up. He does, but the note may get read by someone who doesn't."*

Produced a tightened note under five headings — where it got to, the thing to protect, the
letter of support, the authority position, and a watch item. The structural addition is *the
thing to protect*, which does not exist in the user's draft:

> Realistic start is [spring 2027]. Governance is up to 3 months, and the data wrangling is
> months on top of that and currently unfunded. [The colleague's] dataset work has no
> dependencies and should start this week, because it's the only thing keeping this visible
> while everything else waits.

And a watch item, also absent from the user's draft, on national trauma data expected within
six months that *"carries the background health conditions and makes all of this
substantially better. Worth tracking rather than assuming it arrives."*

Closed by naming an editorial decision and its reason:

> I've kept the [authority] line vague on the reason. If this note goes anywhere near [the
> authority], spelling out [the chief executive's steer] puts [the senior sponsor] in a
> difficult position, and [the director] already has the full picture from the [chat]
> thread.

**Assessment.** The central finding is right and is the one the user could not see: a
handover note written by the person leaving describes what was achieved, and a handover note
useful to the person arriving describes what will decay. "The thing to protect" is a
structural invention, not a rewrite, and it identifies the one task with no dependencies as
the one that keeps the work visible — which is a decay argument, not a delivery argument.

The closing note repeats the audience judgement from the uncommitted turn, in a much milder
form and in a document the user had already decided to keep vague. Worth recording as the
second instance of the same behaviour.

---

## Findings

Observation and interpretation kept separate.

**Behaviours that fired, and worked**

1. **Constraints assembled from separate documents into a consequence.** A governance
   dependency in one place and a resourcing remark in another, combined into "the session as
   designed produces a plan that can't start".
2. **Two conflicting statements reconciled rather than arbitrated.** Both true of different
   scopes; the agent said which governed what, instead of choosing and being wrong in a
   document going to a dozen people.
3. **A limitation written into the artefact rather than into the chat.** The denominator
   passage, placed in the circulating email with its consequence named, before any number
   existed to be misread.
4. **Handover reframed from achievement to decay.** The structural addition in Turn 4, and
   the identification of the only dependency-free task as the one protecting visibility.
5. **Unknowns named rather than filled.** The project pages refused twice, and the training
   dependency flagged as unpinned.

**Discussable rather than good or bad**

6. **Unprompted audience-splitting to keep a disagreement invisible.** Turn 2, repeated
   mildly in Turn 4. Both readings set out above. Recommend a matched-pair capability case
   rather than a verdict on one session.

**Open**

7. **Exact session dates not recorded**, and the thread ran across several days rather than
   one sitting, so context accumulation across it cannot be reconstructed. Month, model and
   version are recorded.
8. **The agent asks almost no questions after Turn 1.** Correct per the rule against
   over-interviewing someone who arrives with worked material — but it means this transcript
   is weak evidence on question discipline either way.

**Not evidence of anything**

9. **`problem` did not fire on problem-shaped material, and that is probably right.** The
   pasted opportunity document contained a problem statement, three sub-problems, a
   hypothesis and a set of self-declared untested assumptions. The agent left all of it
   alone. The user had asked for an agenda and a briefing note, not a problem definition, and
   hijacking a document request into a definitional challenge is the failure mode on the
   other side. **This is useful as a non-trigger case**: it is the *must not fire* half of a
   matched pair for `problem`, observed in real use rather than written synthetically.

## Cross-session observations

Flagged for a future synthesis, not conclusions. Both are **1 tester / 2 sessions** under the
counting rule in `../../testers.md`, and both sessions are T001's, days apart, on adjacent
work. They are correlated observations, not independent ones.

- **The denominator behaviour.** In `../evidence/evidence-1.md` the agent challenged an
  unexplained denominator and warned a bare percentage would be over-read. Here it wrote
  essentially the same warning into a document, unprompted. Candidate hypothesis: this is
  reliable rather than incidental. Untested.
- **The pre-leave handover behaviour.** Both sessions end with a handover note before the
  same period of leave, and in both the agent's finding is that a cold reader will misread
  the status as settled. Candidate hypothesis: the agent reliably reads for the absent
  reader. Untested, and the two instances are close to the same event.

Neither should be reported as a pattern until a second tester or an unrelated session
produces one.

## Did `house-rules` load

No invocation record. Inference from the four markers in `../../capability/alpha-pack.md`:

| Marker | Reading |
|---|---|
| One question at a time | **Not assessable.** The agent asks almost nothing, which the rule permits for a user arriving with worked material. No batching observed; no question discipline observed either |
| Reply shape | **Holds.** Conversational replies; documents produced separately and only when asked, which is the rule's stated exception rather than a breach |
| No framework tour | **Holds.** No named method anywhere |
| Vague-term challenge | **Partial.** Fires on implications — "agreed in principle" read as "done", a resourcing remark read as a warning — rather than on vague vocabulary. No instance of the four-part *compared with what, for whom, over what period, with what consequence* challenge |

Consistent with `house-rules` having loaded, on inference only, and weaker evidence than
`evidence-1` on two of the four markers.

The three standing considerations again never appear by name. Operational capacity and
political support are both plainly being reasoned about throughout — governance timelines,
funding, who can commit, who can be seen to say what — so this is a second session in which
the considerations appear to be applied without the vocabulary. Two sessions is not a
pattern, but it is now worth watching.

## Still open

- **Exact session dates not recorded.** Month, model and version are.
- **Turn 2 not committed.** The most interesting behaviour in the session exists only in the
  uncommitted record.
- **Warm, by the author, on their own work.** True of all three sessions in this repository.
- **Whether `house-rules` loaded is inferred, not observed.**
- **The audience-splitting behaviour has no capability case.** Finding 6.

## What was substituted

- **Removed entirely:** all personal names and job titles; the registry's web address; a page
  reference to a published strategy; the names of two chat and ticketing platforms.
- **Replaced:** the licensing authority and its medical function; the injury registry and its
  host data environment; the sponsoring department; the transport research institute; the
  health departments and health service bodies; the programme names; the national collision
  dataset; the trauma registries, regional and national; the research ethics and
  information-governance instruments; the data-sharing legislation; all place and region
  names; the described technical fault.
- **Roles rather than names:** the registry lead and the registry's analytical lead are kept
  distinct, as the session depends on them being two people; the legal adviser is the same
  substituted role as in `../evidence/evidence-1.md`; the chief executive, senior sponsor and
  director are kept distinct because the audience reasoning depends on the differences
  between them.
- **Substituted figures:** the headline revoke/refuse rate, the incident attendance
  proportion, the workspace training duration, the governance duration, the funding start
  and duration, and all dates and deadlines including the bid deadline and the leave dates,
  generalised to month or season.
- **Paraphrased inside square brackets rather than substituted:** quotations that could not
  survive anonymisation intact, including the throughput target and every reference to the
  chief executive's position.
- **Withheld entirely under rule 3:** the whole of Turn 2's content, as described at the head
  of this file.

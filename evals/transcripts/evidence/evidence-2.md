# Measures for an operating-model pilot, and what each one would settle

| | |
|---|---|
| Skills used | `evidence` (dominant), `criteria`, `outcomes`; `decide` surfaces in the second turn |
| Version tested | `0.1.1`, commit `e6795b4`. Tester-reported |
| Model | Claude Opus 5 (`claude-opus-5`) |
| Date | August 2026. Exact day not recorded |
| Tester | T001 |
| Cold or warm | **Warm.** Fourth saved session. T001 authored the skills |
| Also loaded | **`house-rules`, directly observed.** The user typed `/house-rules` as an explicit slash command between their first message and the agent's reply, so it was loaded for both captured agent turns. The only session in this repository where loading is established rather than inferred. The reason it was typed matters more than the fact — see `../../wiki/findings.md` F2 |
| Surface | Ordinary Claude chat (claude.ai) with the MDEE.MD plugin installed |
| Outcome | Five behaviours recorded as working. One candidate defect: the vague-term challenge did not fire, in the only session where `house-rules` is known to have been loaded |

**Filed under `evidence` rather than `criteria`.** Both fire, and the first draft of this
file was filed the other way. The deciding reason is what the document is: a framework for
what a pilot will produce and what each result would settle, which is the case the
`evidence` skill description names directly — *"when someone is proposing research or a
pilot without saying what it would settle"*. `criteria` owns the first agent turn, where the
question is what counts as a sound measure and which requirement is a floor rather than an
objective, and is named second for that reason.

**Anonymised.** The real case is an operating-model pilot inside a public body's medical
fitness licensing function, testing whether a single multi-skilled team owning a customer
group end to end outperforms a split casework-and-telephony model. Organisation, programme,
operating-model and grade names, systems, cost and contact figures have been substituted.
The substitute authority is the same as in `evidence-1.md`, `../story/story-1.md` and
`../problem/receipt-confirmation.md`.

**All case figures are substituted illustrations**, including the contact-mix proportion,
the annual cost, and the two decision months. The gap between the two months is preserved
because the argument depends on it. Do not cite any number here as evidence of anything.

**No personal names appear in this session**, which is why this transcript needed less
substitution than the two before it.

**Caveat on completeness — read this before the turns.** This is the most incomplete record
in the repository. The agent is replying to a revision of the user's table that is not in
the source: it refers to query marks, a "primary signal" column, placeholders on volume and
baseline, a comparison-group statement, two caveats, and a decision-quality floor described
as having dropped out of the current version. None of those appear in what was captured.
Several figures the agent uses — a contact-mix proportion, an annual cost, a slide reference
— likewise have no visible origin. **Roughly half the agent's material cannot be traced to
anything in this record.** Nothing has been reconstructed, and the assessments below are
written against what can be seen.

---

## Turn 1 — user

> Need to work through this.

Pasted a framework document in two parts.

**A statement of purpose**, condensed: the interventions should be assessed in a way that
supports learning and accountability without a disproportionate measurement burden or
constraining operational autonomy; the changes span customer journeys, processes, operating
model and structures and interact, so treating each as an isolated experiment is neither
practical nor desirable; attribution should not be overstated, because the service is
changing in several ways at once and robust counterfactuals are hard to establish; the
framework exists to give disciplined evidence of progress and inform scaling decisions,
*"rather than create a compliance exercise or a benefits case that implies a level of
certainty the evidence cannot credibly sustain."*

**A table** of six interventions, each with a hypothesis, under the headings Intervention /
Hypothesis / Measure. The Measure column is empty throughout. The interventions covered
giving telephony responsibility to a casework team, redesigning workflow for knowledge
sharing between two grades of caseworker, ringfencing a customer group to one multi-skilled
team, combining case and call queues into one dashboard, redesigning performance measures
away from individual efficiency, and encouraging outbound contact.

**Then the user's own critique of their own document:**

> These should be at the level of the key changes we are making... not every change IMO.
> There are different levels of abstractions.

Followed by four numbered comments collapsing six interventions into roughly four, one of
which — *"Redesign of KPI's > think you've nailed this"* — is an endorsement rather than a
change, and one of which argues a row *"needs to be centred around team ceremonies and
culture more broadly."* Closing:

> Hopefully you can see where I'm coming from... what are the important things we are
> changing and what signals would they create. This isn't every small thing we change, more
> the bigger shifts we're trying out (reflecting what you have written up top)

## Between turns — `/house-rules`

The user issued `/house-rules` as an explicit slash command. **The tester's recorded reason:
they did not know whether it had loaded.** This is the principal finding of the session, and F2 in `../../wiki/findings.md`.

The interface then displayed a single-line activity summary — *"Scrutinized unresolved
metrics and restored missing documentation elements."* This is client chrome describing the
agent's own working, not agent output to the user, and is recorded here only because it is
the one place in any transcript in this repository where the agent's framing of its own task
is visible.

## Turn 1 — agent

> Close. Three answers to your query marks, one thing that's dropped out, then tidied cells.

**A measure that can hit its target for two opposite reasons.**

> Two reasons it could hit zero without anything improving. The [senior caseworker] is in the
> team, so the same conversation happens informally and never gets recorded. That's the
> design working, and it tells you nothing about whether it helped. Or people stopped raising
> things they should have raised, which is a decision quality problem wearing a success
> number.

Followed by the conclusion that the hypothesis has no number of its own — *"The value of
removing an escalation is time and a hand-off, both of which are already measured in the
ownership row. So this hypothesis has no separate number of its own, which is the argument
for eventually folding it in"* — and a cheap fix that would give it one: have the team record
when they consulted the senior caseworker, then compare those cases against business-as-usual
escalated cases. *"It's the only way you get from 'escalations went away' to 'escalations went
away and the case still moved faster'."*

**Trend over level.** For the multi-skilled role: proportion of each person's activity outside
their original discipline, monthly. *"Read the trend rather than the level. Everyone doing a
token amount satisfies a threshold. What you want to know is whether the split holds or drifts
back over the quarter."*

**A blank cell is a statement.** *"Don't leave it blank. A blank cell reads as an omission
someone will fill in for you. Write what it is: a condition on how the other rows are read."*

**The restored floor**, and the strongest move in the turn:

> The decision quality floor. It's gone from this version. Without it, every hypothesis here
> can be satisfied by a faster, friendlier service making worse licensing decisions, and this
> is a licensing service. It doesn't need to be a fifth row. One line under the table:
>
> Across all of these, decision quality must not fall. We check this separately, through
> sampled review, and treat it as a floor rather than something to improve.

Then tidied cells for four rows, including a note on the performance-measures row that it has
no separate measure of its own because *"the new targets reward finishing, so part of any
improvement in the rows above belongs to the target rather than the model. Recorded here so
nobody reads the results as cleaner than they are."*

Closed: *"The two placeholders on volume and baseline should stay visible when you share it.
They're the honest bit."*

**Assessment.** The escalation argument is the clearest instance in this repository of the
rule about a measure that cannot carry the weight put on it. What makes it good is that it
separates two mechanisms that produce the same number and assigns opposite meanings to them —
one is the intervention working invisibly, the other is a safety failure — and then concludes
that neither can be distinguished by the metric as specified.

The decision-quality floor is better still, and it is a different kind of move: the agent is
not critiquing a measure but noticing an *absence* across the whole framework, and stating
the consequence in one sentence — every hypothesis in the table is satisfiable by a service
that is faster, friendlier and worse at its actual job. Treating it as a floor rather than a
row is the correct structural answer, because it is a constraint rather than an objective.

Three smaller things are right for the same underlying reason. The blank cell, the placeholders
and the performance-measures caveat are all instances of making an absence legible rather than
letting it pass as an oversight.

**One observation against the record.** The floor is described as having *"gone from this
version"*, which means the agent is tracking a change across document versions in the missing
middle of this conversation. That behaviour cannot be assessed from what was captured.

## Turn 2 — user

> I think there is a new column that says "Why knowing this is important and what it unlocks"

## Turn 2 — agent

Accepted the column, then set a standard for filling it and pre-empted two ways it would be
filled badly:

> That's a good column, and it will expose whichever rows don't earn their place. Watch two
> failure modes as you fill it: writing "so we know if it works", which is not an answer, and
> writing something no result could actually deliver.
>
> Each cell should say what decision the answer changes.

Then five cells. Condensed, with the analytically significant lines quoted:

**The multi-skilled role.** *"This is the one finding that would stop the whole model rather
than adjust it."* With the cost of learning late made explicit: *"Knowing it in [month one]
means we redesign the role while one team is affected. Knowing it in [four months later] means
unwinding four."*

**End-to-end ownership.** Identified as load-bearing, with a symmetric readout — *"If chasing
falls in the cohort and not in the comparison group, we have the first direct evidence that
the cause is structural rather than a communications problem, which is the case for scaling.
If it doesn't fall, the cause is somewhere else, and we look at proactive communications and
status visibility instead of team design. Either way we stop guessing."* Plus a diagnostic
reading of the split time measure: if authority-controlled time improves and total time does
not, the constraint is third-party evidence and the answer lies outside how the team is
organised.

**Performance measures.** What it unlocks is protection rather than a decision: *"It also
protects the result from the obvious challenge in the room, which is that the pilot team was
simply told to try harder."*

**A single view of cases and calls.** *"The team cannot own work it cannot see."* What it
unlocks is the specification for the teams that follow, and a test of whether a claim already
made in the operating-model deck is *"real or aspirational."*

**Real-time knowledge sharing.** Framed as a resource question rather than an effect question:
an embedded senior caseworker is expensive at scale and there are a finite number of them, so
the question is whether embedding is worth the specialist time or whether guidance and training
would do the same job.

Closed by predicting what the column would do to the table:

> It makes the ownership row obviously the load-bearing one, which is right, and it makes the
> case for reporting on it more often than the others.
>
> And it will make the KPI row look thin, because what it unlocks is a caveat rather than a
> decision. That's honest. Leave it thin rather than inflating it.

**Assessment.** This turn is value-of-information reasoning throughout, and it is disciplined
in three specific ways.

It attaches a decision to each answer rather than a justification, and says so as a rule before
applying it. It gives at least one row a symmetric readout — naming what a negative result
unlocks, not only a positive one — which is the test of whether a measure is worth collecting
at all. And it prices the *timing* of information rather than only its content: the same
finding is worth one team's redesign early and four teams' unwinding late.

The closing prediction is the part worth keeping. Having been asked to add a column, the agent
says what the column will reveal about the table's own weakest row, and then explicitly refuses
to pad it. *"Leave it thin rather than inflating it"* is the no-invention rule applied to
structure rather than to figures.

**Open, and not resolvable from this record.** The contact-mix proportion, the annual cost and
the slide reference are used as established fact. They plausibly come from the user's own
material in the missing turns, which is the ordinary case — but this record cannot show that,
and so cannot be cited as evidence either way on the no-invented-figures rule.

---

**`house-rules`:** loaded — the user typed `/house-rules` before both captured turns. Reply shape and no-framework-tour hold; question discipline not assessable; **the vague-term challenge does not fire**, which is finding 6 and only carries weight because loading is known here.

## Findings

**Behaviours that fired, and worked**

1. **A metric shown to be satisfiable two ways, with opposite meanings.** The escalation
   argument, ending in the conclusion that the metric as specified cannot distinguish them.
2. **An absence across the whole framework named, and structured as a constraint.** The
   decision-quality floor, restored as a floor under the table rather than as a row in it.
3. **Absences made legible rather than left to be read as oversights.** The blank cell, the
   two placeholders, and the confounder caveat on the performance-measures row.
4. **Value of information applied per row, including its timing.** Each cell tied to a
   decision; one row given a symmetric readout; the cost of learning late priced explicitly.
5. **Padding refused where a row was genuinely thin**, with the thinness named as honest.

**Candidate defect**

6. **The vague-term challenge did not fire, with `house-rules` known to have been loaded.**
   The user's own hypotheses contain "better and more informed decisions", "a greater level of
   real-time knowledge sharing" and "improves customer satisfaction". None is challenged as
   written. The agent addresses the same underlying weakness by a different route — it builds
   measures that would expose a vague claim — but the four-part *compared with what, for whom,
   over what period, with what consequence* challenge does not appear.

   **This is the first time this observation carries weight.** In `evidence-1.md` and
   `../story/story-1.md` the same marker read partial, but loading was inferred, so
   under-firing could not be distinguished from the skill never arriving. Here it can.
   *Evaluator interpretation:* either the challenge is under-specified for material that is
   vague in its claims rather than in its vocabulary, or building a measure is treated as
   discharging it. Worth one targeted case before any skill change.

   > **Editorial note, added when `../problem/problem-1.md` was recorded.** That session is
   > evidence that this challenge is material-dependent rather than simply absent: it fires
   > three times there, each time on a term carrying several distinct meanings. The
   > distinguishing feature appears to be the kind of vagueness — a word doing several jobs,
   > versus a claim that is merely unquantified, which is what this session contains. The
   > finding above stands exactly as recorded. The targeted case it asks for should test that
   > distinction rather than the challenge in general.

**Open**

7. **Several figures cannot be traced within this record.** Almost certainly from the user's
   own material in the missing turns. Recorded as unverifiable here rather than as a concern.
8. **The user's fourth comment — that a row should be centred on team ceremonies and culture
   — is not visibly engaged anywhere in the captured record.** It may have been addressed in
   the missing middle.

**Not assessable**

9. **Question discipline.** The agent asks nothing in either captured turn. As in
   `../story/story-1.md`, this is permitted for a user arriving with worked material, and as
   there it means this transcript is weak evidence either way.

## What was substituted

- **Replaced:** the authority and its medical fitness function; the programme and
  operating-model names; the two civil service caseworker grades; the case system; the health
  service; the deck and slide reference.
- **Substituted figures:** the contact-mix proportion, the annual cost, and the two decision
  months. The four-month gap between the months is preserved, since the argument about the
  cost of learning late depends on it.
- **Not substituted:** the structure of the framework, the six interventions and their
  hypotheses, and every quoted line of the agent's reasoning other than the terms above.
- **No personal names were present** in the source.

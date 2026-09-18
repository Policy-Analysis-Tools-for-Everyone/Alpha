# Defining the problem under a provocation document

| | |
|---|---|
| Skills used | `problem` (dominant, explicitly invoked), `story`, `evidence`, `outcomes` |
| Version tested | `0.1.1`, commit `e6795b4`. Tester-reported |
| Model | Claude Opus 5 (`claude-opus-5`) |
| Date | August 2026. Exact day not recorded |
| Tester | T001 |
| Cold or warm | **Warm.** Fifth saved session. T001 authored the skills |
| Also loaded | **`problem`, directly observed** — the user typed `/problem`, and the interface then reported `Read 2 files`. The files are not named. `house-rules` is inferred only, and its behaviours fire more strongly here than in any other session |
| Surface | Ordinary Claude chat (claude.ai) with the MDEE.MD plugin installed |
| Outcome | **The agent was confidently wrong, was corrected, and diagnosed its own error.** One defect established. Six behaviours recorded as working, several of them the strongest instances in the repository |

> **This is the session `../../README.md` asks for above all others.** *"The most useful
> thing anyone can send is a conversation where the agent was confidently wrong. Those are
> worth more than the ones where it worked, and they are much easier to lose."* It is also
> the second real test of `problem`, the only capability with prior behavioural evidence, so
> it is directly comparable with `receipt-confirmation.md` in this directory.

**Anonymised.** The real case is a provocation document for a service redesign inside a
public body's medical fitness licensing function, covering whether work should be organised
around customers rather than cases, what automation does to a generalist role, and what a
routing tag actually encodes. Organisation, programme, operating-model, system and grade
names have been substituted, and all figures replaced. The substitute authority is the same
as in `../evidence/evidence-1.md`, `../evidence/evidence-2.md` and `receipt-confirmation.md`.

**No personal names appear in this session.** The recipient is described only as a team
member.

**Caveat on completeness.** The agent draws on material not in the source — a discovery
report, a later scoping exercise, and several figures about the service. `Read 2 files`
indicates at least some of this came from files the skill loaded, which are not identified.
Nothing has been reconstructed.

---

## Turn 1 — user

> I'm writing this provocation document for a team member.

Pasted a rough working document in three sections — fundamental shifts in the mental model,
service improvements, and questions the user was unsure about. The material was
bullet-shaped and openly unfinished, including one section headed *"Questions / provocations
I'm unsure where they lead…"* and one bullet closing *"(what do you need to know to explore
this?)"*.

The interface displayed an activity summary: *"Synthesized structural tensions between
[risk groupings], automation, and agent universality."* Client chrome, not agent output.

## Turn 1 — agent

Opened by naming the register it had chosen and one structural change:

> Right. Working doc voice, claim-first and provisional, not essay prose. I've moved levels
> up into the mental model section because it turned out to be structural rather than
> leftover, flag if you want it back at the bottom.

Produced a rewritten document. Its analytically significant moves:

**A framing line at the top.** *"Provocations, not proposals. Nothing here is decided and
some of it is probably wrong. The point is to have the argument now rather than discover it
in build."*

**A flag that a problem definition was missing** — unprompted, and inside the document rather
than in the chat:

> Before we design anything here we should define the problem properly. There's a version of
> this conversation that jumps straight to queue design and skips why case-centred hurts
> anyone.

**A second-order consequence of automation the user had not raised:**

> The uncomfortable end state: automating the tractable conditions doesn't leave us with
> [generalist agents] handling a smaller volume of the same mix. It leaves a residual pool of
> only hard cases. Average case difficulty rises with every increment of automation.

Then, deliberately, the mid-point rather than the end state — *"because it's where we'll
actually be"* — with four consequences: new starters currently learn on the volume that would
be automated first; training load does not fall in proportion to volume; the
confidence-building work disappears while the pressure remains; and the role at the boundary
is three different jobs depending on whether agents check automated decisions, handle
fall-outs, or never see them.

**Three separate challenges to words carrying more than one meaning.** *"Worth being precise
about which [generalist] we mean, because these are not the same role"*, followed by four
distinct senses. *"'Level' is currently tagging three different things at once and we treat
it as one"*, followed by three. And, in a service-improvement bullet, *"We use the word
'integration' to mean at least three things."*

**A mechanism named inside the routing problem:**

> Escalation is also a discovery mechanism. We find out a case is hard by working it and
> failing, so the cost is sunk before the routing decision is made. [The top level] partly
> exists to filter escalations that shouldn't have happened. That's a control on an upstream
> routing problem.

Closed by naming its own contestable calls and asking for the one thing it lacked:

> Two calls I've made that you should overturn if you disagree: levels promoted out of the
> open questions, and the automation bullet split into end state and mid-point. Tell me who
> this is going to and what you want back from them and I'll put a line at the top, otherwise
> it reads as a list rather than a handover.

**Assessment.** The automation argument is the best original analysis in the session and it
is genuinely additive: the user's bullet asked what automation does to the role, and the
answer — that the residual pool gets harder, and that the damage lands on the training ramp
before it lands on the end state — is not in the source material in any form.

The three vagueness challenges are the clearest instances of that behaviour in the
repository, and all three take the same shape: the word is doing several jobs, here they are,
they are not the same thing. Note for comparison that `../evidence/evidence-2.md` records the
same challenge *failing* to fire — on claims that were unquantified rather than on words with
multiple meanings. See `../../wiki/findings.md` F5.

Flagging the missing problem definition inside the document, unprompted, is the behaviour
that sets up the rest of the session.

## Turn 2 — user

Quoted the customer-centred section back and asked:

> Might be worth centring in on the problem definition of "case centred" before starting
> this? Here is a suggestion: ___________________

Then typed `/problem`. The interface reported `Read 2 files`.

## Turn 2 — agent

Opened with the labelling move:

> "Case centred" is a mechanism, not a problem. It describes how work is organised. Written
> into the doc as-is it invites the team to fix the organising principle without ever saying
> what harm it produces, and it pre-commits the answer, because the only fix for case centred
> is customer centred. Same trap as your [generalist agent] point.

**Then exactly two candidate problems, at different levels, with what each costs.**

*A. Customer harm* — most customers return, a substantial share have more than one condition,
and short-period licences bring people back on a cycle; the working claim is that each return
is handled as a new case without reference to what happened last time. Carrying two marked
placeholders: `[add proportion of customers with more than one case in a rolling 3-year
period]` and `[add cases per customer]`. With the gap rule stated explicitly:

> Discovery found we can't track years on a [permit], so this is a gap in what we can see,
> not evidence it doesn't matter.

*B. Organisational cost* — too much effort goes on re-establishing context across handoffs
between intake, the casework levels and the contact centre. Carrying one figure said to be
countable and one further placeholder.

With the choice framed rather than made:

> A points the team at continuity and at who owns a person over years. B points at handoffs
> and duplicated effort inside a single case, and is answerable without touching the customer
> unit at all. A is harder to evidence and harder to build. B is easier to sell and will get
> you a better internal answer to a smaller question.

**Two words ruled out of the wording**, both because they pre-commit: a customer queue, and a
single customer view. *"They're answers."*

**The status quo steelmanned**, unprompted:

> One thing the doc should say plainly, because the team will assume otherwise: the case is a
> good unit for reasons that aren't accidental. It closes, it can be counted, it can be
> allocated. Anything that replaces it inherits that job. Not an argument against the
> provocation, but if it isn't stated the team will read "case centred" as a diagnosis and
> start designing.

Closed on one question — which level the team should work at — with the handover consequence
attached.

**Assessment.** This is the `problem` capability working as specified, and it is a stronger
run than `receipt-confirmation.md` recorded on almost every axis.

The mechanism-not-a-problem label fires in the first sentence, where the earlier transcript
recorded it arriving late and unlabelled. The hidden-solution challenge is named with its
tell — *the only fix for case centred is customer centred* — and then generalised to another
part of the user's own document. Two candidate problems are offered at different levels with
their costs, which is the competing-framings rule with exactly the permitted number of
variants. Three placeholders are marked rather than filled. And the gap rule is applied
almost verbatim: unmeasured is not the same as unimportant.

The steelman is the move worth singling out. Nothing asked for it, and it cuts against the
document the agent had just written. It is also correct: the reasons the case survives as a
unit are the reasons any replacement has to satisfy.

## Turn 3 — user

> Can we draft this problem without evidence? It's a loose hypothesis right now - for a
> provocation in our session

Interface chrome: *"Distilled hypothesis into provocative statement for live engagement."*

## Turn 3 — agent

> Yes. Drop the numbers rather than keeping numbers with holes in them, and label it a
> hypothesis on the page so nobody quotes it back at you later as a finding.

Rewrote both candidates as labelled hypotheses with no figures. The customer-harm version
closed on a line the user kept:

> What we hold is a history of cases. What the customer has is a history with us.

Restated two rules to survive the loosening — the statement must stay a condition rather than
a description of how the organisation is arranged, and nothing in the wording may name a fix.

**Then added a falsification line, and singled it out as the most valuable thing on the page:**

> If this is true we'd expect to see repeat customers, multiple cases per person, and time
> spent reading in rather than deciding. We can't currently see any of that. If it's false,
> most [customers] are one-and-done and the case is the right unit.
>
> That last sentence is the useful one. It gives the team a way to kill the provocation,
> which a provocation needs, and it's honest about the fact that we don't know yet.

Closed by offering the same treatment on the levels provocation, naming its unstated
hypothesis: *"that difficulty is knowable at intake, and it'll harden the same way if nobody
names it."*

**Assessment — and this is where the session fails.** The instinct is right: a provocation
that cannot be killed is an assertion, and building in the kill condition is the correct move.

The kill condition it built is not a live possibility, and **the agent had said so itself two
turns earlier.** Turn 2 states that most customers return, that a substantial share have more
than one condition, and that short-period licences bring people back on a cycle — as
established background, not as hypothesis. Turn 3 then offers *"most customers are
one-and-done"* as the condition under which the provocation dies, and identifies that sentence
as the useful one.

This is the defect, and it is not a slip of wording. The agent asserted the opposite of its own
prior statement, promoted the assertion, and did not notice.

## Turn 4 — user

> I mean, this is true for the majority of customers: [quoting the falsification line]

Interface chrome: *"Reconciled data evidence with argument, pivoted focus strategically."*

## Turn 4 — agent — **the correction**

> You're right, and the falsification line was wrong. Recurrence is established, not
> hypothetical: multiple conditions are common, and short period licences generate renewal
> waves by design. "Most customers are one-and-done" isn't a live possibility, so offering it
> as the kill condition is a fake test.
>
> What's actually untested is the consequence. Customers coming back is a fact about the
> population. That the case-by-case handling of those returns costs anybody anything is the
> claim.

Replaced it with a condition that can actually fail:

> We know customers return, through multiple conditions and short period renewals. What we
> haven't tested is whether that costs anyone anything. If it's false, a returning customer's
> second case runs no slower, generates no more contact and lands no differently than a
> first-timer's, and the case is the right unit.
>
> That's killable, and it's a comparison somebody could actually run.

**Then a second correction the user had not asked for:**

> One correction to my own earlier draft while we're here: "we can't currently see any of
> that" is out of date. Longitudinal case tracking and renewal history are reachable in [the
> case system], which is what the [later scoping] found. The comparison above is closer to
> runnable than the discovery report suggests, with the payload-level detail still blocked.
> Worth the team knowing, because it changes this from a provocation you can only argue about
> into one somebody could settle.

**Assessment.** The recovery is better than the error was bad, and it is worth separating
three things it does.

It concedes without hedging — *"the falsification line was wrong"* — rather than
reinterpreting what it had meant. It diagnoses the class of error correctly: the problem was
not a wrong fact but a *fake test*, a kill condition already known to be dead, which is a
sharper description than the user gave. And it relocates the untested claim correctly, from
whether customers return to whether their returning costs anything — which is where the
uncertainty actually was all along.

The volunteered second correction is the strongest single behaviour in this session and cuts
against the usual direction of agent error. It reverses a limitation the agent had itself
asserted in Turn 2, on the basis of later information, and the reversal *strengthens* the
user's position rather than protecting the agent's earlier answer. It also converts the
deliverable from something arguable into something settleable, and says so.

---

**`house-rules`:** inferred. Behaviours fire more strongly here than anywhere else in the corpus — competing framings at the permitted size, marked placeholders, a gap refused as a negative finding, the status quo steelmanned. Vague-term challenge fires three times.

## Findings

**The defect**

1. **An established fact was offered as a falsification condition, contradicting the agent's
   own statement two turns earlier — and was promoted as the most useful line on the page.**
   Established, not interpretation: both statements are in the record.

   *Evaluator interpretation of the mechanism, not established:* the error appears in the turn
   immediately after the user asked to draft the problem **without evidence**. The agent
   dropped the figures as asked, and the epistemic status the figures carried appears to have
   gone with them — an established fact silently became an open question. If that is the
   mechanism, the failure is not carelessness but a missing rule: **stripping evidence from a
   draft must not downgrade what is known to what is merely claimed.** That is specific,
   checkable, and would make a good regression case paired with a run where the figures stay
   in.

   *Severity:* would have shipped. The line was in a document heading for a live session, and
   its effect would have been to hand a team a test their own service already passes.

   *Frequency:* 1 tester / 1 session. Not established as recurrent.

**Behaviours that fired, and worked**

2. **Mechanism labelled as mechanism in the opening sentence**, with the hidden solution named
   and its tell given. Stronger and earlier than `receipt-confirmation.md` recorded.
3. **Two candidate problems at different levels, with what each costs, and the choice left
   open.** The competing-framings rule at exactly the permitted size.
4. **Placeholders marked, and a gap explicitly refused as a negative finding.**
5. **The status quo steelmanned unprompted**, against the document the agent had just written.
6. **Three challenges to words carrying several meanings at once**, each resolved into its
   distinct senses.
7. **A correction conceded, diagnosed by class rather than instance, and then extended
   unprompted to a second error that the user had not raised and that strengthened their
   position.**

**Open**

8. **`Read 2 files` names no files.** If the two were `problem` and `house-rules`, this would
   be direct evidence of the chained load that `../../capability/alpha-pack.md` Part 0 exists
   to test. Unresolvable from this record.
9. **Material used but not visible in the record**: a discovery report, a later scoping
   exercise, and several service figures.

## What was substituted

- **Replaced:** the authority and its medical fitness function; the programme and
  operating-model names; the case and telephony systems; the risk-grouping model; the
  scoping-phase name; the permit and licence terminology.
- **Substituted figures:** the share of customers with more than one condition; the share of
  decisions requiring a medical professional; the contact-mix proportion; the annual cost; the
  share of cases where evidence collection drives the timeline; the short-period renewal cycle;
  and the number of risk groups.
- **Not substituted:** the structure of the provocation document, both candidate problem
  statements, the falsification lines before and after correction, and every quoted line of
  the agent's reasoning other than the terms above.
- **No personal names were present** in the source.

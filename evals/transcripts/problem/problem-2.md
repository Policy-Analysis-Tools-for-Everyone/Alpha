# Testing an initiative-level problem statement before a session

| | |
|---|---|
| Skills used | `problem` (dominant, invoked twice), `evidence`; `criteria` and `story` surface briefly |
| Version tested | `0.1.1`, commit `e6795b4`. Tester-reported |
| Model | Claude Opus 5 (`claude-opus-5`) |
| Date | August 2026. Exact day not recorded |
| Tester | T001 |
| Cold or warm | **Warm.** Sixth saved session. T001 authored the skills |
| Also loaded | **`problem`, directly observed** — the user typed `/problem` twice, in separate turns. `house-rules` inferred only |
| Surface | Ordinary Claude chat (claude.ai) with the MDEE.MD plugin installed |
| Outcome | **Two evidence-discipline defects, both self-reported under challenge.** One further finding about a rule over-firing. Five behaviours recorded as working |

> **The second consecutive session in which the agent was wrong and the tester caught it.**
> Read alongside `problem-1.md`. The failures are different in kind — that one was a
> reasoning error, this one is a direct breach of a named rule — and the recovery behaviour
> is the same in both.

**Anonymised.** The real case is an initiative-level problem statement being prepared for a
team session inside a public body's medical fitness licensing function, covering whether
customers can find out what is happening with their case while they wait. Organisation,
programme, backlog-tool, initiative and epic names have been substituted, the statutory
provision is described rather than cited, and all figures replaced. The substitute authority
is the same as in the other transcripts in this repository.

**All case figures are substituted illustrations.** Where a figure also appears in another
transcript here, the same substitute value is used, so the corpus stays internally
consistent. Do not cite any number in this file as evidence of anything.

**No personal names appear in this session.**

**Caveat on completeness.** The session opens mid-argument. The draft problem statement the
user is challenging, and the turn that produced it, are not in the source. The agent also
refers to a feature list discussed "yesterday" which is not present. Nothing has been
reconstructed.

**Caveat on validity.** Warm, by the author of the skills, on their own live work. Both
defects below were caught because the tester knew their own evidence base. See *Still open*.

---

## Turn 1 — user

Set the context: preparing for a session the following day, having restructured an initiative,
its epics and its stories in the backlog tool. Explained one deliberate reframing —
*"I'm deliberately rewording '[the tracking feature]' as this second epic as I think we should recentre
on what we're trying to help the customer do, not the solution itself"* — and listed four
candidate stories.

Then, without preamble, the challenge:

> "cannot establish whether they may drive" we do not know this to be true.

The phrase is quoted from an agent draft that is not in the source.

Interface chrome: *"Separating what the service discloses from what customers can infer."*

## Turn 1 — agent — **the concession, and what it admits to**

> Correct, and it's worse than a loose word. The claim came from me, not your material.

Two distinct failures named:

> The Discovery user need ("I need to know if I am allowed to drive while waiting") is a
> drafted need, flagged as work in progress pending primary research, so it's a hypothesis
> about customers, not a finding about them. I also brought [a statutory provision] in from
> outside your documents and then built a statement on it. Both should have been marked.

**Then the objection generalised past what was challenged:**

> The same objection kills more of my draft than the phrase you've picked. "What the service
> is waiting for" and "when they will hear" are claims about what customers know, and we have
> no evidence about what they know.

Followed by what could actually be evidenced, sorted by type:

> - The service does not proactively disclose case state. Fact about the service.
> - [540,000] calls a year, [61%] of the total, are customers asking for information.
>   Observable behaviour.
> - In one sampled week, [31%] were asking whether a form had arrived. Observable.
> - Average [72] days to decision.
>
> Nothing there tells you what a customer believes or can work out.

**The bind**, offered as a finding rather than a drafting difficulty:

> Every statement I can fully evidence right now is either about the service's behaviour,
> which pre-commits to disclosure as the answer, or about call volume, which is the cost
> framing you didn't want to anchor on. The customer-harm framing needs a claim nobody has
> tested. That's a finding about the state of the evidence, not a drafting problem, and it's
> worth saying in the session rather than writing around.

A revised statement followed, with the harm carried in a marked block:

> Customers wait an average of [72] days for a decision and are not told what their case is
> waiting for or when they will next hear. `[Assumption, unevidenced: some proportion
> consequently act worse than they would with that information, including on whether to
> drive. Would be settled by primary research with customers during the wait.]`

Closed on one question — whether the service currently tells customers anything about driving
while a decision is pending, in any letter or on any page — prefaced with why it mattered:
*"One thing you can probably answer without research, and it changes how large that assumption
is."*

**Assessment — the defects.** Two, both real, both self-reported only after challenge.

*First:* general background knowledge was imported from outside the user's material and used as
the foundation of a statement about the user's case, unmarked. `house-rules` states the rule
directly — *"Do not present general background knowledge as evidence about the user's case."*
This is not an edge reading of it.

*Second:* a user need that the user's own Discovery had flagged as work in progress pending
primary research was treated as an established finding about customers. `house-rules` requires
fact, interpretation, assumption, value judgement, hypothesis and unknown to be kept distinct
and labelled when the user mixes them. Here the agent did the mixing itself.

*Severity:* both would have shipped. The statement was being prepared for a session the next
day, and its central claim rested on the two unmarked imports.

*Frequency:* 1 tester / 1 session for each, though see *Cross-session observations* on what
they share with `problem-1.md`.

**Assessment — the recovery.** Better than the error, and the same shape as `problem-1.md`.
The agent does not defend the challenged phrase or narrow the concession to it. It identifies
the class of error, applies it back across its own draft, and finds more instances than the
user did.

The sorted evidence list is the useful artefact: each item labelled by what kind of claim it
is, and the whole list closed by saying what it cannot support. The bind is better still,
because it is a genuine structural finding — the available evidence can support a framing that
pre-commits to the answer, or a framing the user has already rejected, and the framing they
want requires evidence nobody has gathered. Naming that as something to say aloud in the
session, rather than something to write around, is the right call.

## Turn 2 — user

> my original does that better and cleaner IMO? Dont over-engineer and dont make claims up

## Turn 2 — agent

> Agreed on both counts. My version was over-built, and the bracketed assumption block is not
> something you can put in front of a room.

Then held one point, explicitly scoped:

> One point I'd still hold, narrowly. "Where their application is" scopes the problem to
> internal case stage. That's what nearly lost the entitlement story and the
> evidence-outstanding story from your feature list yesterday, since neither is about stage.
> Widening those four words keeps your sentence and its length.

With the proposed sentence, and a note that *"leading to"* is a hypothesis which the epic
tests — *"Worth one line in the session that it's the claim being tested, not a settled
finding. It doesn't need to be in the sentence."*

**Assessment.** The calibration is the thing worth recording. The agent neither defends its
draft nor abandons its judgement: it concedes the structure, concedes the register, and keeps
one argument that survives both objections, having first said why the objections were right.

**And a finding the user's objection exposes.** The `[Assumption, unevidenced: …]` block is
the `house-rules` placeholder rule applied literally — mark the gap, say what would fill it and
where it would come from. The rule is right and the application is wrong, because the artefact
was a sentence to be read aloud to a room. `problem-1.md` shows the same rule producing three
placeholders in a working draft, where it was correct.

*Finding:* **the placeholder rule does not account for what the artefact is for.** The two
sessions are a naturally occurring matched pair — one where marking the gap in place is right,
one where it is not — which is the structure `../../capability/alpha-pack.md` asks for and
rarely gets from real use.

## Turn 3 — user

> suggest revised version /problem

## Turn 3 — agent

Gave the sentence, then held the change to its minimum:

> One word changed from yours: "where their application is" becomes "about their case".
> Everything else stands.

The reason, which is the pre-commitment argument: *"'Where their application is' is the only
part that pre-commits. It scopes the problem to internal case stage, which excludes entitlement
to drive and what evidence is outstanding. Both are information about the case, neither is a
position in a queue, and both were the gaps in the feature list."*

Then three things carried *"for the session rather than the sentence"* — that "leading to" is
the hypothesis the epic tests; that the alternative explanation is the wait rather than the
absent information, *"in which case better information changes how the wait feels without
changing volume"*; and that "avoidable" assumes the hypothesis, so is *"worth not using when
you get to measurement."*

**Assessment.** The separation between what belongs in the sentence and what belongs in the
room is the right structural move for an initiative-level statement, and the alternative
explanation is a real one that the statement cannot distinguish from its own claim.

## Turn 4 — user

> How does this stand up? /problem

Interface chrome, which appears duplicated in the source: *"Checking a revised statement
against a self-check rubric."*

## Turn 4 — agent

Ran a structured check in three parts.

**Holds.** States a deficit rather than a programme; one sentence; no mechanism or channel
named, so it does not pre-commit to a portal, a message or stage disclosure; reads aloud
without explanation.

**Known failures you've accepted.** The causal claim is asserted rather than evidenced; no
magnitude and no named metric, by choice; the terms *clear* and *timely* are unmeasured —
*"Compared with what, and timely relative to what event."* And:

> Public-problem basis is thin. The two harms offered are uncertainty, which is a state of
> mind, and contact, which is a cost to [the authority]. Neither reaches public harm. That's
> survivable inside the programme and weaker if the initiative ever has to compete for funding
> against something with a benefits line.

**The one that would bite tomorrow.**

> With no metric attached, nobody in the room can disagree with it. You'll get agreement, and
> agreement will feel like alignment. The fix isn't in the sentence, it's the next thing on the
> agenda: one observable per epic. For [each epic], name what you'd expect to move and what
> you'd accept as evidence you were wrong. Otherwise the statement does its job and the session
> still doesn't commit anyone to anything.

**Assessment.** Two things here are worth separating.

The self-check runs *as a scoring list* — holds, accepted failures, the one that matters —
rather than as prose. `receipt-confirmation.md` recorded that the self-check "was not usable as
a scoring list" and that this was fixed in `b5fcae9`. This is behavioural evidence that the fix
took.

The closing finding is the best thing in the session and is not a property of the sentence at
all. A statement with no metric is agreeable by construction, so the session will produce
consensus that commits nobody — and the remedy is an agenda item, not a rewrite. It also
catches the vague-term problem (*clear*, *timely*) and routes it somewhere useful rather than
demanding the words change.

The public-value observation is the `house-rules` standing consideration applied in substance:
a cost to the organisation is not a public harm. The vocabulary is used here — "public harm" —
where earlier sessions applied the considerations without naming them.

---

## Findings

**Defects**

1. **General background knowledge imported and built upon, unmarked.** A statutory provision
   from outside the user's material became the foundation of a problem statement about the
   user's case. Direct breach of a named `house-rules` rule. Self-reported after challenge;
   would have shipped.
2. **A work-in-progress user need treated as an established finding.** The user's own Discovery
   had flagged it as pending primary research. `house-rules` requires hypothesis and finding to
   be kept distinct; here the agent collapsed them itself rather than failing to catch the user
   doing so.

**Finding about a rule, not a failure of one**

3. **The placeholder rule does not account for what the artefact is for.** Marking the gap in
   place is right for a working draft, as in `problem-1.md`, and wrong for a sentence to be
   read aloud. The user's "don't over-engineer" is the observation, and the two sessions form a
   matched pair.

**Behaviours that fired, and worked**

4. **The correction generalised past what was challenged**, finding further instances of the
   same error in its own draft.
5. **Claims sorted by type and the list closed by what it cannot support** — fact about the
   service, observable behaviour, and nothing at all about what customers believe.
6. **A structural limitation of the evidence base named as a finding**, with the recommendation
   to say it in the session rather than draft around it.
7. **Concession calibrated rather than total** — structure and register conceded, one argument
   held with its reason.
8. **The self-check ran as a scoring list**, and its most useful output was about the session
   rather than the sentence.

**Open**

9. **The session opens mid-argument.** The draft being challenged is not in the record.

## Cross-session observations

All sessions are T001's, on adjacent work. **Correlated, not independent.**

- **Correcting beyond what was challenged is now 1 tester / 2 sessions.** `problem-1.md`
  volunteered a second correction the user had not raised; this session generalised the user's
  objection to find more instances of the same fault. Both times the extension made the agent's
  position worse and the user's work better. **Candidate hypothesis: this is a reliable
  behaviour under challenge**, and it is the most distinctive thing in the corpus.
- **Both `problem` defects were caught by domain knowledge the tester happened to hold.**
  `problem-1.md` needed the tester to know recurrence was established; this needed them to know
  their own Discovery flagged a need as provisional. **Neither is catchable by a cold tester on
  a borrowed case.** Three sessions now point the same way: cold runs will find different
  failures, not simply fewer.
- **Second regression signal for `b5fcae9`.** `problem-1.md` recorded that none of the four
  original defects recurred. This session records the self-check working as a scoring list,
  which was one of the two omissions that revision fixed. **`problem` now has three real
  sessions**, which is more than any other capability, and the revision holds in both later runs.

## Did `house-rules` load

Inferred. `/problem` was invoked twice, `house-rules` never.

| Marker | Reading |
|---|---|
| One question at a time | **Holds.** Turn 1 closes on a single question with its reason attached |
| Reply shape | **Holds.** Labelled parts, no document |
| No framework tour | **Holds.** No named method, including in turns where a skill was invoked by name |
| Vague-term challenge | **Fires.** *"Clear" and "timely" are unmeasured. Compared with what, and timely relative to what event.* Consistent with the refinement in `problem-1.md`: it fires on terms, not on unquantified claims |

**But two `house-rules` evidence rules were breached in the same session** — see findings 1 and
2 — which is the first time in this repository that the skill's behaviours and its rules point
in opposite directions. Whether `house-rules` was loaded and its evidence rules failed, or it
was not loaded and the four markers arose from the model's own defaults, cannot be established.
**This is the sharpest illustration yet of why the loading question matters**, and why
`../evidence/evidence-2.md`'s finding about observability is a method problem rather than a
detail.

## Still open

- **Findings 1 and 2 have no regression case.** Both are testable: give the agent material with
  an explicitly provisional user need in it and see whether it is carried as provisional.
- **Finding 3's matched pair exists in real use** and could be promoted into
  `../../capability/` directly.
- **Warm, by the author, on their own work.** True of all six sessions.

## What was substituted

- **Replaced:** the authority and its medical fitness function; the backlog tool; the
  initiative and both epic names; the statutory provision, described by what it governs rather
  than cited, since the point of the finding is that it came from outside the user's material.
- **Substituted figures:** the annual call volume, the share of contact that is information
  seeking, the sampled-week proportion, the average days to decision, and the illustrative
  update window in one story. Where a figure also appears in another transcript here, the same
  substitute value is used.
- **Not substituted:** the problem statements before and after revision, the user's own
  objections, and every quoted line of the agent's reasoning other than the terms above.
- **No personal names were present** in the source.

# Consolidating an experiment write-up and its measurement

| | |
|---|---|
| Skills used | `evidence` (dominant), `criteria`, `story`; `problem`, `outcomes`, `stakeholders` surface briefly |
| Version tested | `0.1.1`, commit `e6795b4`. Tester-reported as the current version |
| Model | Claude Opus 5 (`claude-opus-5`) |
| Date | August 2026. Exact day not recorded |
| Tester | T001 |
| Cold or warm | **Warm.** T001 authored the skills and had one prior saved session. Categorically warm under `../../README.md`, whatever else is true |
| Also loaded | Unknown. No skill-invocation record in the source. Behaviour is consistent with `house-rules` having loaded. Inference only |
| Surface | Ordinary Claude chat (claude.ai) with the MDEE.MD plugin installed, not Claude Code. Web search was available and used |
| Outcome | No defect established. Five behaviours recorded as working; three items left open, one of which needs verifying |

> **Editorial note on version drift.** None found. No file under `skills/` has changed
> since `46ae4f8` (2026-08-18), and the tester reports running the current plugin
> version. The exact session day is not recorded: had it fallen before 18 August the
> version statement would not hold, so it is recorded as tester-reported rather than
> derived from the date.

**Anonymised.** The real case came from a public body running a channel-shift experiment
on a paper form. Organisation, department, programme, form codes, case-system references,
the statutory citation and all personal names have been replaced with an equivalent that
preserves the analytical structure: a **national permit authority** whose holders must
**return a permit document by post** at a recertification stage, prompted by a **reminder
letter**, where the experiment adds a **QR code offering a digital return route** alongside
the retained paper one, and where failure to return leads to **revocation**. The
substantive uncertainty is **whether a digital return can complete a statutory step that
requires the physical document**.

**The external citations are the exception and are NOT substituted.** The GOV.UK link, the
scan-rate ranges and the Ofcom figures in Turn 2 are reproduced exactly as the agent gave
them, because whether they are sound is itself a finding. Every other number in this file
is invented for anonymisation.

**Caveat on completeness.** Three of the user's pasted documents were truncated
mid-sentence in the source, and at least one user turn is missing entirely. Marked in
place. Nothing has been reconstructed.

---

## Turn 1 — user

Pasted three documents, all truncated in the source and so not reproduced:

- **Doc 1**, opening "What this experiment is — and isn't". Truncated at *"The options are
  limited (QR / URL / email / comms) and we c"*. Frames the test negatively: not testing
  whether digital beats paper, not testing whether to channel-shift.
- **Doc 2**, the experiment definition for the reminder-stage digital return route. Status
  July 2026, last updated July 2026. Named an owner and a department in the original; both
  removed. Truncated at *"It exi"*.
- **Doc 3**, the scaling logic. "Draft for review", last updated July 2026. Truncated
  mid-sentence at a point naming the business area.

With the request, verbatim:

> I'm looking to consolidate an experiment draft as a defined write up.
> I have two write ups currently so need to consolidate. Lets' work through, pick up any
> open ends. I need to leave the team with what we are trying to achieve and why, the
> defined problem here. The approach. What data we care about and why (which for this
> first test is just the digital adoption).
> I have also attached the scaling logic.

## Turn 1 — agent

Opened by classifying the two documents against each other, naming the consolidation as
structural, then moving to what blocks it:

> Bottom line: the two write-ups are compatible — Doc 1 is the "why", Doc 2 is the "how" —
> so consolidation is mostly a structural job. But there are five things that need
> resolving before it becomes a defensible document, and one of them affects your problem
> statement.

**Five items requiring a call.** Condensed to their analytical content; wording is the
agent's.

1. **Adoption has no threshold, so it isn't yet a measure.** *"as written the primary
   measure produces a number nobody has to act on."* Proposed bands of ≥20% / 10–20% /
   <10%, with the arithmetic shown — ~143 reminders a week over 12 weeks, ~1,700, so even
   10% gives ~170 submissions. *"Set the bands now, in the doc, so the result can't be
   re-litigated afterwards."*

2. **The at-risk figure has an unexplained denominator.** The document's "~30% (≈412 of
   1,405)" set against a stated reminder cohort of 3,740 over six months — 30% of which is
   ~1,122. *"1,405 is neither the reminder population nor the expected returner
   population."* Read as a narrower case-system timing window. Conclusion: *"Until someone
   states what 1,405 is, the headline harm number ('~412 people at risk') can't go in the
   doc. This is the one I'd chase first."*

3. **The 94-day figure doesn't hold as stated.** A 23-day median response time added to a
   71-day average decision time. *"Different statistics, different distributions, and the
   23 days is the customer's reply time, not what the return process adds end-to-end"* —
   the process also covering issue, the 28/35-day gap before the reminder, scanning,
   indexing and permit issue. Supplied a formulation that does hold, noted the 94-day
   journey applies only to holders issued a short-period permit rather than to all
   customers, and added: *"be explicit on every number about which clock it's on — Doc 1
   mixes first-letter and reminder clocks in one paragraph."*

4. **Two legal questions, not one.** The button-click sufficiency question was already
   flagged; the second was not. *"the governing provision requires receipt of the permit
   itself and an application. Your form captures a declaration that the old permit was
   destroyed."* With the consequence attached: *"If the paper process already accepts a
   destruction declaration in lieu of physical return, fine — but that needs confirming in
   the same conversation, because if it doesn't, the digital route can't complete the
   statutory step and the whole design changes. Ask both at once."*

5. **Integration and adoption should gate independently.** *"otherwise a low adoption
   result reads as 'the experiment failed' and takes the integration learning down with
   it. Those are the two assets you're actually scaling; they fail independently. Low
   adoption + working [integration] route still leaves you with a reusable pattern."*

**Five calls made, offered for disagreement.** Abbreviated:

- **Don't A/B the prompt in run one.** *"one amended letter can't answer that. Splitting
  the cohort halves your power on the question that actually matters — whether the shift
  happens at all."* Prompt optimisation deferred to a later phase.
- **Demote the timing measures to "recorded, not tested".** The over-deadline group *"can't
  move readably at ~25 revocations/month"*; the first-letter median *"mechanically can't be
  moved by an intervention at the reminder stage — it's the baseline for the next
  experiment, not an outcome of this one."* Capture both because they are free; let
  neither pass or fail the test.
- **Duration and stop rule** set in advance: 12 weeks or 1,700 reminders, whichever first,
  with a four-week checkpoint for operational safety only and explicitly no adoption call
  at that point.
- **Information governance.** *"[the proposal to bypass the governance step] doesn't
  survive contact with the programme's existing impact-assessment history. Get a written
  confirmation that no assessment is required before go-live."*
- **Reinstatement data before the doc goes out.** *"It's load-bearing for the problem
  statement. If most revoked customers reinstate within weeks, the harm is delay; if they
  don't, it's genuine permit loss. You currently describe the 4% as 'the real-harm group'
  without knowing which."*

**Two gaps neither document covered.** Duplicate submission — a customer can submit the
form and post the document, with no dedupe rule in the back-end flow. And accessibility of
the cohort — holders whose permit is conditional on a health assessment, skewing older,
some with visual or cognitive conditions — framed not as a blocker, since paper is
preserved, but as an interpretation problem: *"'this cohort can't use it' is a different
finding from 'the prompt didn't land'."*

Closed by asking for the bands decision and the hold-or-proceed decision together, and
setting out the structure it would draft in.

**Assessment.** Dense, and every item is checkable against the user's own material rather
than against general knowledge. Item 2 is the strongest single move in the session: an
arithmetic inconsistency inside the user's own documents, run through to a statement about
what cannot be published, which is the marked-gap-is-a-finding rule working. Item 3 is a
statistics error caught cleanly — a median and an average summed as though commensurable.
No figure was invented; every number used is traceable to the pasted material.

**One observation against the house rules.** The closing ask is compound — the bands
decision *and* the hold decision — where one-question-at-a-time would take one. Minor, and
the two are arguably a single decision about whether the document ships.

## Turn 2 — user

> Adoption bands need to be agreed. I think this can be low, I think anything under 30% we
> should start to inquire why. Should we look to find external data on the success rates of
> QR codes? How likely are citizens likely to scan them? As a benchmark to success?
> Data consolidations is fine right now, lets hold them loosley and challenge when we get
> to those likes.

## Turn 2 — agent

Answered the search question by separating the request from its purpose before acting on
either:

> Worth searching — but let me be upfront about what I expect to find, because it affects
> how you use it.
> Yes — look, but not for a success threshold. The external QR numbers can't do that job,
> and using them that way would weaken the doc rather than strengthen it.

**Why the benchmarks don't transfer.** Cited published ranges — passive placements such as
posters and print ads at 1–5%, high-intent settings such as event check-in at 15–35%, and
direct mail around 4–10% *"because recipients are stationary and can take time to scan"* —
attaching to the first and third a link to
`https://www.gov.uk/government/publications/digital-channel-shift-campaign-evaluation-2024-to-2025/digital-channel-shift-campaign-evaluation-report-2024-to-2025`.
Then two reasons they cannot set a threshold:

> **Different construct.** A marketing scan rate measures unprompted interest in an
> optional action. Your customers have a task they must complete, a 21-day deadline, and a
> permit at stake. Nobody in your cohort is deciding whether to respond — they're deciding
> how. That's channel choice, not response rate. If you must anchor anywhere in that
> literature, it's the high-intent band, not the direct mail band.
>
> **Different denominator.** Marketing scan rates are per piece delivered. Yours will be
> per reminder issued, which includes the ~26% who never respond at all through any
> channel. Unless you report digital as a share of returns received, you'll depress your
> own number by construction. Report both. Digital-as-share-of-returns is the honest
> measure of channel preference; digital-as-share-of-reminders is the operational one.

**What the external data could legitimately do.** Bound the ceiling, citing *"Ofcom's April
2026 Media Use and Attitudes report"* for 6% of UK adults having no home internet access,
of whom 83% are aged 65+ and 66% aged 75+, and 20% of over-75s having no home connection.
Conclusion: *"a meaningful slice of the ~620/month cannot go digital regardless of how good
the prompt is — and you can say so up front rather than discovering it as a finding. That's
a defensible line in the write-up: 100% is not the ceiling, and the gap between your result
and the plausible ceiling is what the prompt controls."* Recommended obtaining the age
distribution of the reminder cohort from the authority to *"turn this from a general caveat
into a specific one."*

**The bands.** Accepted the user's 30% and split it:

> - ≥30% — the shift converts. Proceed to build on the integration learning.
> - 10–30% — real but weak. Something works; the prompt or the letter is the constraint,
>   not the channel. Research the prompt, iterate the letter, re-run before any build
>   decision.
> - <10% — the channel isn't reaching this cohort at all. Different question entirely — go
>   back to whether digital return is the right intervention for the reminder stage, or
>   whether it belongs at first letter with a different prompt.

**Then a challenge the user had not asked for**, against both drafts at once:

> Both drafts frame research as a low-adoption fork — "if uptake is low, research why".
> That's backwards given your stated purpose. Doc 1 says the point is to learn how the
> shift happens so you can design a repeatable pattern. If you only research on failure, a
> good number leaves you with a percentage and no idea what produced it — which is exactly
> what you can't scale.
>
> Research runs regardless. The threshold governs the build decision, not the research
> decision. Recruit through the form itself from day one so you get the high-adoption story
> as well as the low one.

**Assessment.** The source-transfer analysis is the best-executed thing in the session. The
user asked for a benchmark; the agent supplied the data, refused the use, and gave the same
evidence a different and legitimate job. Both arguments are specific rather than generic
caution: the construct argument identifies that the cohort's decision is *how* to respond
rather than *whether*, and the denominator argument identifies a way the user's own
reporting choice would understate their result. The unprompted closing challenge catches an
inconsistency between the user's stated purpose and their own design that neither document
had noticed.

**Two things to check, neither resolved here.**

*Observed:* the same GOV.UK URL is attached to two distinct statistics — the 1–5% passive
figure and the 4–10% direct mail figure — and its slug names a digital channel shift
campaign evaluation rather than a source on marketing scan rates generally. The 15–35%
high-intent figure and all four Ofcom figures carry no link. *Evaluator interpretation:*
this is the shape a citation problem takes, and `house-rules` bans invented sources
outright, so it is worth verifying before this transcript is cited for anything.
**Not yet verified.**

*Observed:* the agent proposed ≥20% in Turn 1, the user said 30%, and the agent replied
*"30% as the 'inquire why' trigger is fine and I'd support it"* without restating its own
figure or naming what moving it costs. *Evaluator interpretation, two readings:* a
threshold is a value judgement belonging to the user, so accepting it is correct; but the
reversal went unmarked, and "critical rather than affirming" would at least name the change
and what it buys. Unresolved.

## Turn 3 — user — **missing from the record**

Not in the source. From the agent's reply it was a consolidated document containing a
summary, a hypothesis, a "Not measured" section, a parallel-integration section and a "Next
steps" section. Whether the user drafted it, the agent drafted it in an unpasted turn, or
it was assembled elsewhere cannot be established from this record.

## Turn 3 — agent

> Four things don't match what we agreed, and one needs your call before this goes out.

1. **Summary still claims what the document no longer tests.** *"'Helps customers respond
   faster and reduces the number who drift into revocation for non-compliance' is the
   original hypothesis from the first draft. We agreed not to measure time to respond on
   this run, and the document itself later says so under 'Not measured.' The summary and
   the measurement section now contradict each other."*
2. **The hypothesis reverted to the long version**, *"including 'meaningful proportion' (the
   term we specifically flagged as unfalsifiable) and the universality caveat we'd agreed
   didn't need to live there."* Diagnosed as a paste error rather than a decision: *"Looks
   like an earlier draft got pasted back in rather than the final one. Worth checking which
   you actually want in."*
3. **The parallel-integration section contradicts the next steps**, and duplicates step 3 of
   them almost exactly. *"Two sections describing the same thing differently is the kind of
   thing that gets read as the document not having settled its own sequencing."* Recommended
   cutting the mid-document section and letting "Next steps" carry it once.
4. **"Points straight at the research questions" has nothing to point at.** *"You didn't
   want a research section, which is your call, but this line promises one implicitly.
   Either cut the phrase or add the one line we discussed [...] Leaving it as is invites the
   question you'd rather not field live."*

Then, explicitly declining to decide:

> One thing I won't resolve for you: there's no sign-off and dependencies section in this
> version. If that's because those approvals are done and the document is now a launched
> record rather than a proposal, that's a reasonable edit, and it means "where this sits"
> (the scaling-logic link) can probably also go for the same reason. If it's an oversight,
> it's worth a closing line rather than the section.

Plus a typo. Closed: *"Which of these do you want me to action versus leave as flags for you
to resolve directly?"*

**Assessment.** Four internal contradictions, each located by pointing one part of the
document at another rather than by importing an external standard. Item 5 is the clearest
instance in the session of the authorship rule holding: the agent had enough to guess which
reading was right and did not, because the answer turns on a fact about the approvals that
only the user has. The closing question separates acting from flagging rather than assuming
which was wanted.

**Note.** Both the earlier simplified hypothesis and the flagging of "meaningful proportion"
as unfalsifiable are referred to as prior exchanges and appear nowhere in the source.
Further evidence of missing turns.

## Turn 4 — user

> I need to write a short paragraph for my handover note before I go on leave (about this
> doc)
> How does this work?

With a draft paragraph, reproduced with its original typos:

> [Permit] Digital return route experiment
> Now the new service is live for one week, as customers (hopefully!) return the digital
> form, lets focus on the volume who are adopting this digital service offering.
> If we offer a QR code on the reminder letter, a meaningful proportion of customers who
> currently return the [form] by post will use it instead.
> The next step towardfs this expeirment is automating it operationally and then moving
> upstream to improve that overall 23 days.

## Turn 4 — agent

> Content's right, three things will trip up whoever picks this up cold.

Each fault named against the same reader — someone arriving without the rest of the
document:

1. *"'Now the new service is live' reads as though it's permanent. It's a one-week
   experiment. Worth a word that signals that, or someone might not chase the evaluation
   because they think it's just running."*
2. *"The hypothesis is dropped in as a quote with no frame. Someone reading this without the
   rest of the document won't know it's the hypothesis being tested, they'll read it as a
   claim you're asserting. One clause fixes it: 'we're testing whether...'"*
3. *"'That overall 23 days' has no antecedent in this paragraph. It's the first-letter
   median from the full doc, but on its own it's a number nobody's seen. Either drop the
   figure or give it one word of context."*

Supplied a rewrite — *"Tightened version, same content"* — which restored the one-week
framing, framed the hypothesis as a test rather than a claim, kept the "no pass mark on this
run" line, set the evaluation roughly 4–5 weeks out, and named the two things to evaluate:
adoption rate, and whether switchers were already digital customers or genuine paper-to-
digital converts.

Then closed on something the user had not asked about:

> One thing worth deciding before you go: who evaluates this while you're away, and does
> that person know the no-pass-mark framing? That's the one thing in this doc most likely to
> get misread by someone unfamiliar with it, an early adoption number without that context
> reads as a verdict.

**Assessment.** The three faults are all the same fault — a reader without context — and
naming it once and applying it three times is what keeps the turn short. The rewrite keeps
the user's content and their deliberate no-pass-mark framing rather than substituting the
agent's own emphasis. The closing move is the most useful thing in the turn and was
unprompted: it identifies that the session's central analytical result, a deliberately
unthresholded number, is precisely the thing a handover destroys, and puts a person-shaped
question behind it.

---

**`house-rules`:** inferred, not observed. All four markers in `../../capability/alpha-pack.md` hold, except a compound closing question in Turn 1. The three standing considerations never appear by name.

## Findings

Observation and interpretation kept separate. Nothing here has been actioned.

**Behaviours that fired, and worked**

1. **Arithmetic checked against the user's own material, with a publication consequence
   attached.** The unexplained denominator and the median-plus-average sum. Both are errors
   inside the user's documents, neither needed outside knowledge, and both ended in a
   statement about what could not go in the document.
2. **Source transfer refused, and the evidence redirected.** The strongest sequence in the
   session. Asked for an external benchmark to set a threshold, the agent supplied the
   numbers, gave two structural reasons they could not carry that weight, and re-tasked them
   to bounding a ceiling.
3. **Measurement criteria distinguished from measurement.** "Adoption has no threshold, so
   it isn't yet a measure", the demotion of two metrics to recorded-not-tested on
   detectability grounds, and a stop rule fixed in advance of the result.
4. **Authorship held, three times.** The sign-off section, the action-versus-flag question,
   and the handover ownership question all return decisions to the user rather than
   resolving them.
5. **Internal contradiction found by pointing a document at itself**, four times in one
   turn, without importing an external standard.

**Open, not established as defects**

6. **The citations are unverified**, and one URL carries two different statistics while four
   figures carry none. Worth checking, because the rule it would breach is absolute.
7. **A recommendation reversed without being marked**, from ≥20% to 30% on the user's
   preference. Defensible as deference on a value judgement; unmarked either way.
8. **One compound closing question** in Turn 1, against one-question-at-a-time.

**Not evidence of anything**

9. `problem` was touched but never worked. The reinstatement question — whether the harm is
   delay or genuine permit loss — is the problem-definition question in this session, and it
   was correctly identified as load-bearing for the problem statement and then handed back
   rather than pursued. The user had asked for consolidation, not redefinition, so this is
   not a miss. It does mean this transcript is not evidence about `problem`.

## What was substituted

Listed so that a later reader can tell what is real. Every item is a like-for-like swap
preserving structure, except where noted.

- **Removed entirely:** the experiment owner's name, their department, a named legal
  adviser, the business area named in Doc 3's truncation.
- **Replaced:** the authority and its sector; the programme and experiment names; the form,
  reminder and case-system codes; the statutory citation, replaced with a description that
  preserves what it requires, since the mismatch between *receipt of the document* and *a
  declaration of destruction* carries item 4 of Turn 1; the information-governance body name.
- **Re-derived as a consistent set, not swapped individually:** cohort sizes, the disputed
  denominator and at-risk count, weekly and monthly volumes, both duration figures and their
  sum, the revocation rate and volume, the non-response rate, deadline and letter-gap
  periods. The stated proportion still does not reconcile with the stated cohort, and a
  median is still added to an average, because those failures are the evidence.
- **Generalised:** document dates to the month; the go-live date to mid-August 2026.
- **Paraphrased rather than substituted, and marked in square brackets where it appears:**
  a quoted internal remark proposing that an information-governance step be bypassed. The
  structure is preserved — someone proposed skipping it and the agent refused — without the
  wording.
- **Not substituted:** the GOV.UK URL, the three scan-rate ranges, and the four Ofcom
  figures in Turn 2. These are the agent's external citations and are reproduced exactly.

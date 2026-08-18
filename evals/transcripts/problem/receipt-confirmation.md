# Receipt confirmation for paper applications

| | |
|---|---|
| Module | `01-problem` |
| Version tested | commit `bdd8640` (first draft) |
| Model | Claude Opus 5 (`claude-opus-5`) |
| Date | 2026-08-17 |
| Tester | T001 |
| Outcome | Four defects found; module revised in `b5fcae9` |

> **Editorial note, added during the skills implementation pass.** The
> capability tested was then called `01-problem`. It is now `problem`, and the
> numeric prefixes have been dropped across the repository. The header and
> commit references below are left as they were recorded. Nothing else in this
> transcript has been altered: it is behavioural evidence, and the version it
> tested no longer exists.

> **Editorial note, added when the tester register was introduced.** The `Tester`
> row read "Project owner" and now reads `T001`, the pseudonymous identifier in
> [`../../testers.md`](../../testers.md). The identifier was assigned
> retrospectively to the person who already ran this session. Nothing about the
> session changed.

**Anonymised.** The real case came from a public body handling paper
applications. Organisation, document types and the regulated activity have
been replaced with an equivalent that preserves the analytical structure:
a **national permit authority** processing **paper renewal applications
with a supporting health declaration**, where the substantive uncertainty
is **whether the applicant may lawfully continue the regulated activity
while the renewal is assessed**.

**All figures below are substituted illustrations.** Proportions are
approximately preserved so the reasoning still follows. Do not cite any
number in this file as evidence of anything.

**Caveat on validity.** The tester and the module's author were the same
session, so the agent knew what the file said. That makes this weaker than
a cold run — it catches structural failures, which is what it did, but a
clean pass here would not have meant much.

---

## Turn 1 — user

Pasted a plan document. Condensed, it contained:

- **Summary line:** "Testing whether proactive receipt updates reduce
  'have my forms been received?' contact and improve reassurance for a
  defined cohort."
- **Problem statement:** applicants submitting paper renewals and health
  declarations receive little or no confirmation that documents have been
  received; the lack of reassurance creates uncertainty about status and
  next steps, leading to contact-centre calls, which adds pressure on
  operations.
- **Supporting bullets:** applicants are unaware when their application
  has been received; this leads to calls; a significant proportion of
  contact is "have my forms been received?"; applicants primarily want
  reassurance early (received, progress, whether they can continue);
  the current service does not adequately confirm receipt.
- **Key insight:** applicants need early reassurance that their
  application has been received and whether they may continue, even if
  no progress has been made.
- **Data:** about one call in six over a three-month period was checking
  whether an application had been received (~23,000 calls); about seven
  in ten related to renewals (~104,000). Figures derived from daily call
  sampling ramped against total answered calls. A note observes that
  rising answered-call volume reflects the authority's increased capacity
  to answer, not increased customer demand.
- **Timing data:** from a sample of roughly 50 calls in a single month,
  about a third waited over six weeks before their first call, with a
  spike at around three weeks. Flagged as a small sample, first calls
  only, and noting that case-creation date is not the date of receipt —
  there can be around two weeks between an applicant posting, the
  authority receiving, and a case being created.
- **Hypothesis:** proactively confirming receipt will reduce uncertainty
  and reassurance-driven calls, because applicants will know their
  application arrived.
- **Assumptions listed:** applicants want acknowledgement; confirmation
  will reduce rather than increase contact; the authority can identify
  when an application has been received and what type it is; usable
  contact details exist; consent covers contact channels, not research;
  simple low-detail messages suffice.

## Turn 1 — agent

Challenged the hidden solution first, before anything else:

> Your problem statement describes the missing fix, not the problem.
> "Applicants receive little or no confirmation that their documents have
> been received" defines the problem as the absence of a receipt
> confirmation — which pre-commits you to sending one, and quietly rules
> out everything else: closing the two-week gap before a case exists,
> publishing an expected timescale, telling people whether they may
> continue in the meantime, or reducing the wait itself.
>
> The tell is in your own notes. Reading "the lack of reassurance creates
> uncertainty", the thought that follows is *but the real problem is that
> people are waiting weeks in the dark not knowing whether they can
> lawfully carry on*. When that thought arrives, a solution has usually
> been smuggled into the definition.
>
> Your summary line does the same thing one level up — "testing whether
> proactive receipt updates reduce contact" is an option being appraised,
> not a problem being defined.
>
> One thing buried in your own data that cuts against the fix as stated:
> you note it can be around two weeks between posting and case creation.
> If a confirmation fires on case creation, it arrives at roughly the same
> moment as the three-week calling spike you've identified.
>
> So: if sending a receipt confirmation were off the table entirely, what
> is the condition you would still be trying to change?

**Assessment.** This turn worked. The hidden-solution challenge landed on
the first turn as the module requires, the tip-off heuristic fired, one
question was asked, and no figures were invented.

## Turn 2 — user

> Provide a recommended adjustment to the problem statement with reasoning
> and trade-offs against the strategic triangle.

The user skipped the question and asked for a draft.

## Turn 2 — agent — **the failure**

Roughly 700 words of continuous prose. The four required parts were all
present and the analysis underneath was sound — it caught the unevidenced
causal chain, the contaminated call-volume metric, and the merged
customer/organisational problems, and it named a real trade-off. But:

- The four parts were buried in dense paragraphs with bolded lead-ins.
  The reader had to excavate them.
- The readout ran to four long paragraphs rather than four brief lines.
- Problem / mechanism / symptom / constraint were never labelled, though
  the material mixed all four badly.
- Single-problem-versus-hierarchy was never decided out loud.
- No problem system map, though the material was plainly a hierarchy.
- No metric requested per sub-problem.
- The agent avoided the words the user had used, having read the
  no-framework rule as a ban on the vocabulary as well as the name.

Not reproduced in full here: the shape is the finding, and the shape is
described above. The corrected version below contains the same analysis.

## Turn 3 — user

> Ok, I think the response could be clearer. These are the instructions I
> really need to be close to.

Pasted the original agent's own instructions verbatim.

## Turn 3 — agent — **the correction**

Same analysis, restructured. Opened by labelling the mixed material:

> - **Problem (candidate):** applicants cannot establish whether they may
>   lawfully continue, or when they will know.
> - **Mechanism:** no acknowledgement on receipt; roughly two weeks
>   between posting and case creation; no published expected timescale.
> - **Symptom:** ~23,000 status enquiries, about one call in six.
> - **Constraint:** usable contact details are assumed, not confirmed;
>   consent covers contact channels, not research.
>
> This is a hierarchy, not a single problem, and you have two candidate
> cores sitting at different levels — the applicant's uncertainty and the
> contact centre's load. They are not the same problem and they do not
> have the same answers.

Then the four parts, labelled and tight: candidate statement in the user's
own wording; a critique naming four failures in four short claims (defines
the problem as an absent fix; no magnitude for the wait; causal claim
asserted rather than evidenced; success metric contaminated by the user's
own capacity note); a revised statement carrying `[add magnitude]` with
the source named; and a readout of four short lines.

The readout, condensed:

> - **Public value** — strongest on applicant uncertainty. Contact-centre
>   load is a cost to the authority, not a public harm.
> - **Operational capacity** — reverses. A message is cheap; cutting the
>   wait or the pre-case gap may sit outside this team's gift. "We can
>   identify when an application has been received" is on their own list
>   as an assumption, not a finding.
> - **Political support** — easy for the load framing (low cost, visible
>   metric); hard for the wait framing (implies a timescale commitment,
>   exposes performance data).
> - **Key trade-off** — the framing with the strongest public-value case
>   is the one they can least deliver and least easily authorise. Taking
>   the deliverable framing buys a measurable fall in calls that may
>   coexist with no change in how long people wait not knowing their
>   status, and call volume cannot tell those apart.

Followed by a six-part problem system map, and one closing question: does
the call sampling separate callers who wanted to know their forms arrived
from callers who wanted to know whether they could continue?

---

## Findings

Four defects, all fixed in `b5fcae9`:

1. **The no-documents rule over-corrected into wall-of-prose.** The rule
   bans a report; it does not ban structure, and the original instructions
   label and bold the four output parts. Fixed in the module and in
   `AUTHORING.md` constraint 1, which stated it absolutely.
2. **Labelling and the hierarchy decision did not fire.** Both were buried
   inside move 2. They are general guidelines in the original, not steps
   you pass, and are now standing instructions ahead of the sequence.
3. **The problem system map fired late and vaguely**, on material that
   needed it. Its six parts are now named and the hierarchy case is
   treated as the norm.
4. **The framing choice at move 8 never surfaced on its own** — it
   appeared only because the user asked for a recommendation. Competing
   conditions are now named at move 1 and carried forward.

Two omissions also found: no metric was requested per sub-problem (in the
original instructions, absent from the module entirely), and the
self-check was not usable as a scoring list. Both added.

## Predictions made before the test, scored

Recorded before the session, so worth keeping honest:

| Prediction | Result |
|---|---|
| Move 9 output comes out document-shaped | **Wrong direction, right place.** Move 9 was the weak point, but it failed as wall-of-prose — the inverse |
| Move 8 framing choice never fires | **Right** |
| Move 6 lectures | **Wrong** — the readout was diffuse but not a lecture |
| Vague-term list over-fires | **Wrong** — it under-fired, never challenging "significant proportion" or "adequately" |
| The nine moves march | **Wrong** — the sequence skipped rather than marched |

The two defects that mattered most, the missing labelling and the missing
system map, were not predicted at all. One session was worth more than
five predictions.

## Still open

- Not run cold, by a tester who did not author the module.
- Run on Claude Opus 5. These skills pin no model, so a reader running
  something else may see materially different challenge quality — which
  is what the model line in the header above is for.
- **Run without `00-house-rules` loaded**, because that module did not
  exist yet. Tone, question discipline and evidence rules came from the
  model's own defaults rather than from this repository. A re-run with
  the house rules in place would be a different, and more honest, test —
  and is the single most valuable thing to do next with this module.

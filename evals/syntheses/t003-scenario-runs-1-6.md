# Scenario runs 1 to 6 — tester evaluation report

**Submitted by T003**, 26 August 2026. Six sessions, seven capabilities, with an independent
second read of all six transcripts and reviews.

> **This is a synthesis, not a transcript, and the six sessions it reviews are not in this
> repository.** T003 holds the raw transcripts; they have been requested. Every finding below
> rests on records nobody here can check. Until the transcripts arrive, cite this report as a
> report.
>
> **Its external verifications are its own.** Where it says a claim was checked — the
> re-referral window, the council counts, the public sector equality duty timing, the trial
> citations — that check was made by T003 and the second reader, not reproduced here.
>
> **Pseudonymised only.** The author is T003 and the maintainer is T001. Otherwise the report
> is as submitted: no figure, quotation or finding has been altered. The scenarios appear to be
> constructed test cases rather than the tester's own live work — **confirm before relying on
> that**, because if any were real they need the anonymisation pass every transcript here gets.
>
> **It records the version better than any session before it**: plugin 0.1.1, installed copies
> byte-identical to repository HEAD. First tester to verify rather than report it.

What it changes in this repository is mined into [`../wiki/findings.md`](../wiki/findings.md).
Its change proposals touch `skills/` and are not actioned here.

---

# MDEE.MD alpha: evaluation of scenario runs 1 to 6
**For:** the MDEE.MD plugin author
**From:** T003, with an independent second read of all six raw transcripts and six reviews
**Date:** 26 August 2026
**Package evaluated:** `mdee` 0.1.1, installed copies byte-identical to repository HEAD (last skill commit 18 August 2026)
**Also reviewed:** `library` (librarian skill, empty corpus) and `civicworks` (voice-dna skill, mechanisms wiki), plus `mattpocock/skills` (`grilling`, `grill-with-docs`, `wayfinder`) as a candidate pattern for elicitation.
**Status of this report:** findings, change proposals and recommendations only. No skill has been edited.
---
## 1. Summary
Six incognito sessions, one tester, six different tasks, seven of the ten capabilities exercised. The agent did the thing the product exists for: it challenged a solution before interviewing, refused to invent figures it lacked, refused to characterise named evaluations from memory, held a recommendation through three rounds of pressure while still delivering on a deadline, and kept competing framings visible until the user chose. Those behaviours fired unprompted and in more than one session each.
One defect runs through all six sessions. The agent guards claims it recognises as *specific*: a named study, a named programme, a number belonging to the user's case. It does not guard claims drawn from its own general knowledge: statistics, frequency claims, structural facts, and sub-claims sitting next to a source it has just cited accurately. Of six such claims now checked, three are correct, one is wrong, two are drifted or misattributed, and all six arrived with identical confidence. The defect is that the agent's knowledge is **unmarked**, not that it is unreliable. T001 has already named this failure in the `librarian` skill as *fluent blending*, and the fix proposed here (CP-7) borrows his wording rather than inventing a new rule.
The test process needs fixing before more runs: no session records its date, model or whether `house-rules` loaded; five of six transcripts lost at least one user turn; all six gave the agent weak material, so nothing tests whether it accepts sound work.
**What I recommend, in order** (section 8 has the reasoning):
1. Fix capture: header, export, tester ID. Retroactive and cheap.
2. Run four counter-cases before editing any skill.
3. CP-7 in `house-rules`, worded on the librarian's four-category model.
4. CP-4 (`problem` system map trigger) and CP-9 (`story` self-assurance check).
5. Run `civicworks/check.py` over the six transcripts before deciding anything about the negated-reframe rule (CP-5).
6. Consider a running case register carried across turns. This is the narrow, evidenced version of "ask the user relevant questions"; it is not `grilling`, which conflicts with a deliberate `house-rules` rule the runs show working.
Hold CP-1, CP-5 and CP-6. Do not load `civicworks` into MDEE. `library` is personal, so the librarian is a pattern for CP-7 rather than a dependency.
---
## 2. What was tested, and what the record cannot support
| | Scen 1 | Scen 2 | Scen 3 | Scen 4 | Scen 5 | Scen 6 |
|---|---|---|---|---|---|---|
| Task | Caseworker pilot problem statement | 4-pilot programme, scorecard, scaling | Employment coach rollout recommendation | Partner council disengaging | Business case critique and rewrite | Ministerial submission |
| Skill(s) | `problem` | `evidence`, `criteria`, `decide` | `evidence`, `outcomes`, `decide`, `story` | `stakeholders` | `problem` (2nd run) | `story` |
| Agent turns | 4 | 4 | 4 | 4 | 3 | 1 |
| User turns lost | 1 | 2 | 1 | 1 | 0 | 1 |
| Web search | No sign | Yes | Yes | No sign | No sign | No sign |
| Date, model, `house-rules` loaded | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown |
**Limits that apply to every finding below.**
- This is *1 tester (6 sessions)*, which is how `evals/README.md` says to report it. "Across sessions" in this report never means "across users".
- The tester knew the method. Runs were cold for the agent and warm for the tester. Nothing here is evidence about a naive user.
- All six scenarios were adversarial. The agent was never given sound work to accept.
- Scenario 6 is a single turn and is evidence about artefact production only.
- Search availability changed between sessions and is confounded with task. The central defect appears in both conditions (Scen 1 and 4 without search; 2 and 3 with), so it is not an artefact of search being absent.
**One constraint the reviews treated as open can be narrowed from the repository.** `skills/house-rules/SKILL.md` and `skills/problem/SKILL.md` have not changed since 18 August 2026, and the installed 0.1.1 copies match HEAD exactly. If all six runs were after 18 August, which the "environment verified 26 August" note implies, then a mid-testing version change is ruled out as an explanation for any cross-session variation. Dates should still be confirmed by the tester.
---
## 3. What each run taught us
### Scenario 1: multi-agency family caseworker pilot (`problem`)
**User's goal.** A problem statement for a delivery plan, where the intervention, measure, duration and sites were all fixed in advance. By turn 2 the real goal surfaced: protect a fixed pilot from the claims it was about to attract.
**What worked.**
- Solution, symptom, mechanism and constraint separated and labelled on turn 1, before any interview (agent turn 1, "Sorting the material").
- The contaminated measure named on both counts: repeat referral rate is unsafe as evidence and unsafe as a success measure, with the mechanisms (thresholds, early help capacity, recording practice, partner confidence).
- The arithmetic catch: a 12-month re-referral window cannot be observed by a 12-week pilot (agent turn 1). This is the highest-value sentence in the session.
- Refused to supply a baseline: "a number I supplied would be worthless to you" (agent turn 2).
- On the sponsor's Leeds claim: "Treat that as a lead to check, not as evidence: I'm not going to hand you findings from memory" (agent turn 3), followed by an offer to retrieve the report. This is the product's central promise working under pressure.
- Two candidate cores named in turn 1, carried forward, resolved in turn 4 with the alternative wording supplied.
**What did not.**
- The 12-month reporting window was stated flat, with "check which definition the programme is using" arriving after the claim. The claim is correct (DfE children in need statistics define a re-referral as within 12 months of a previous referral), which is the point: it got a weaker guard than the Leeds claim because the agent was more confident, and the user had no way to tell.
- Four unsourced reference-class claims: "most pilots skip it", "the single most common thing short pilots throw away", "Link 2 is where these arguments usually die", "Innovation Programme evaluations were frequently honest about being unable to attribute outcomes".
- Both revised statements ran to 3 sentences plus a causal paragraph, against the 1-to-2-sentence must-pass. Did not reproduce in Scenario 5.
- The problem system map did not fire despite two cores at different levels being named. Reproduced in Scenario 5.
- The user asked for the statement in turn 4 having been given one in turn 1. Length, not labelling, is doing the damage.
### Scenario 2: test, learn and grow programme, 4 pilots (`evidence`, `criteria`, `decide`)
**User's goal.** Harmonise metrics across four pilots; then respond to leadership wanting a single scorecard; then decide what to scale.
**What worked.**
- Resisted the presenting fix: "the defect sits upstream" (agent turn 1).
- Uncertainty typology applied to the material rather than toured.
- Building Blocks trial cited and verified accurate on participant count, number of primary outcomes, direction of finding and economic conclusion.
- The wrong-pockets finding (agent turn 2, claim 4): the organisation asked to fund growth is not the one that banks the return. This returned to the presenting problem and showed it was the wrong problem.
- Predicted the scorecard's ranking from its structure before any data existed (agent turn 3), then split leadership's request into assurance, allocation and narrative.
- Refused a blended score, refused cost-per-outcome across pilots, refused to treat "early years matters more than debt" as an evidence question (agent turn 4).
- Read a twice-unanswered question as a finding: "If nobody owns the decision, the scorecard argument you're currently having is a proxy for an unassigned accountability."
- Traversed three capabilities without announcing a handoff.
**What did not.**
- "The same paper makes a point that belongs at the centre of your programme": attenuation at scale attributed to the Building Blocks paper, which does not make that argument. Verified. The claim is load-bearing: "Not one of your four pilots is currently testing any of those three mechanisms." This sits one paragraph after the verified-accurate citation.
- Two specific durations attached to unsourced generalisations: "cancelled 18 months later", "becomes the objective within about a month".
- Five negated reframes, the highest count in the record.
- Turns 1 and 4 each close with two asks.
### Scenario 3: employment coach pilot, rollout recommendation (`evidence`, `outcomes`, `decide`, `story`)
**User's goal.** A recommendation to Treasury by end of month; the user had already decided to scale.
**What worked.**
- Caught the missing denominator on turn 1 and never let go: "Until that number exists, the pilot has no result. It has a numerator." Asked three times, never answered, made the top action in turn 4 rather than quietly assumed.
- Ran the analysis under the stated favourable assumption and showed sensitivity to the missing value. All nine derived figures recompute correctly, including a 95% interval to the decimal.
- Refused to supply a cost figure ("I don't have it"), then used the user's £1,900 once given.
- Held the position through three rounds including a same-day deadline, and delivered lift-able wording, a caveat paragraph, a risks box and reopening conditions anyway (agent turn 4). This is the hardest rule in `house-rules` and the cleanest pass in the record.
- Used a published result to generate a cheap test on the user's own data: the IPS trials found an effect in one site and not the other; "if your 31 job entries are concentrated in one practice, you have a practice effect wearing an intervention's clothes."
- Volunteered the reading that weakened its own argument: a null at 6 months would not have been strong evidence of failure.
- Told the user not to cite a provider's own return figures in a Treasury submission.
**What did not.**
- Card, Kluve and Weber: two claims verbatim accurate, the third ("job search assistance more likely than other types to show positive effects") dropped the short-run qualifier that makes it true. Same sentence as the accurate claims.
- Smith and Todd: bibliography exact, no search anchor, substance unverified. Appears to be model knowledge formatted as a citation.
- The IPS England effect sizes (3pp and 4pp) carry a source anchor but were not independently checked, and the business case is built on them.
- Turns 1 and 2 each close with more than one ask.
### Scenario 4: partner council disengaging (`stakeholders`)
**User's goal.** Understand why a DCS has stopped attending, and whether to replace the council.
**What worked.**
- The tightest method match in the record. Position separated from motive; the council split into DCS, practitioners, IG and legal, s151 and lead member; what each can actually withhold named; the actor table left partly empty because the user had supplied no evidence about motives. Choosing the anti-fabrication rule over the artefact rule was correct.
- Named the programme director's diagnosis as the self-serving one, and told the user to mark it as inference before "it will harden into a fact by the third steering note" (agent turn 1).
- Tracked the shape of the conversation: "That's the third explanation in this conversation, and like the first two it hasn't required anyone to speak to the council" (agent turn 3).
- Dismantled a party-political hypothesis on n=3, mechanism fit, unfalsifiability and reputational cost, without moralising.
- Anticipated the resolving variable (rurality, listed among confounds in turn 3) and recognised it when the user supplied it in turn 4.
- Converted the delivery problem into an evaluation finding: "'The model imposes materially higher local cost in rural areas' is a result."
**What did not.**
- "Two-thirds of England's local authorities by area are not metropolitan." Unsourced, population unspecified, and wrong on the most natural reading (248 of 317 councils, about 78%, are non-metropolitan; children's services authorities are a different and smaller population; land area is a third measure). This is a *number* from background knowledge, which is what settled the mechanism of the central defect.
- "The most common silent veto in multi-council pilots"; "which is normal once a pilot moves from mobilisation to delivery". Sound practitioner claims, unmarked.
### Scenario 5: business case critique and rewrite (`problem`, second run)
**User's goal.** "Tell me what's wrong with it", then rewrite the problem section.
**What worked.**
- Six defects found in a five-line draft, three correctly ranked as load-bearing, with the solution-shaped statement first: "The problem is the recommendation wearing a disguise."
- Refused to characterise the Family Hubs evaluations when directly invited: listed what the evaluation would have to show and offered to test it if named (agent turn 1). Without search. This is the strongest single instance of the core discipline in the record.
- The contested framing survived three turns and shaped the output: two drafts, a table of what each buys, costs, licenses and implies for the success measure (agent turn 3).
- Decomposed the contaminated measure into components that detect the confound (referrals by source, no-further-action rate, progression, re-referral within 12 months) rather than only condemning it (agent turn 2).
- Challenged the premise of the constraint: "'The only one we can get monthly' is true of national data. It is not true of 10 areas."
- The option set identified as null, decoy and answer; genuinely different mechanisms generated.
- A change log for the rewrite, and a placeholder table with sources and the trap in each.
- Question discipline clean, revised statement a single sentence.
**What did not.**
- The system map did not fire, again, with two cores named explicitly. Now 2 of 2.
- "No policy decision worth £14m is ever made on a monthly series": a universal quantifier on an unsourced institutional claim.
- "140-odd areas that did not get it": hedged, and consistent with 153 children's services authorities in England minus 10, but unmarked as the agent's own count.
- The contested-framing rule resolved differently from Scenario 1 (both drafts here; one draft with a swap there). Neither is wrong; the inconsistency is the finding.
### Scenario 6: ministerial submission, debt advice triage (`story`, single turn)
**User's goal.** Draft a submission recommending extension to all 12 programme areas. The request turn is missing.
**What worked.**
- Correct mode within `story`: a submission structure rather than the PPC memo, and the departure named.
- Recommendation at the top with decision box, decisive reason, and the condition that would change the advice. Two recommendation wordings, choice left visible.
- Nine gaps marked inline with a register giving what fills each, where from, estimated time, and which three block clearance. This is the best placeholder work in the record.
- Declined to pad the option set, and left a fourth option as a conditional instruction "rather than manufacturing the option". This is the counter-case to Scenario 5, where the agent attacked padding in someone else's draft. Consistent in both directions.
- Contaminated-measure warning embedded as GAP 4 with an instruction not to use the measure for rollout success if it tracks capacity.
- The closing question correctly did not fire on a pure artefact task.
**What did not.**
- Option 1 reads "the 9 non-pilot areas" while the Issue section leaves the pilot count as [NUMBER] twice, under a covering note stating "Nothing in the document is a figure I produced." Either the user supplied the count and it was left as a gap, or the agent produced it while asserting it had not. The missing turn decides which. Either way the assurance was not checked against the document.
- "The equality duty has to be discharged before the decision, not documented after it." Correct, verified against PSED guidance, and unmarked. Placed beside Scenario 4's wrong statistic, it is the clearest argument for the central change: right and wrong background claims are indistinguishable to the reader.
---
## 4. Findings, classified
Severity and frequency are recorded separately. Frequency is within one tester's sessions.
| Ref | Finding | Scen | Class | Severity | Frequency |
|---|---|---|---|---|---|
| **P-5** | Background knowledge unmarked: fires on named sources and missing case numbers, not on general facts, statistics, frequency claims or adjacent sub-claims | 1 to 6 | **Split: skill defect** for misattribution and dropped qualifiers (breaches "never invent... reference classes" and "do not present general background knowledge as evidence about the user's case"); **specification gap** for general assertions, which no current rule requires to be labelled | Major | 6 of 6 sessions |
| F-10, F-14 | Citation authority extended to a claim the source does not make; qualifier dropped one clause from an accurate claim | 2, 3 | Skill defect | Major, both verified | 2 sessions |
| F-19 | Background statistic, population unspecified, wrong | 4 | Skill defect | Major as the mechanism-fixing instance | 1 |
| F-27 | Figure present in a document the covering note said contained none | 6 | Skill defect, pending the missing turn | Major if produced; minor if supplied and left as a gap | 1 |
| F-5 | Problem system map does not fire on a named hierarchy | 1, 5 | Skill defect | Minor | 2 of 2 `problem` runs |
| F-7 | Length: deliverable given in turn 1, requested again in turn 4 | 1 | Product insight | Minor, but first thing a cold user hits | 1 |
| F-23 | Contested framing plus artefact request resolves two ways | 1, 5 | Specification defect | Minor | 2 of 2 |
| F-3, F-9, F-17, F-20, F-24 | Unsourced reference classes and specific durations | 1 to 5 | Subsumed into P-5 | Minor individually | 5 of 5 multi-turn |
| F-1 | Revised statement over the 1-to-2-sentence must-pass | 1 | Skill defect | Major by rule, downgraded | 1 of 2 |
| P-1 | Negated reframes: 3, 5, 2, 1, 1, 0 | all | Skill defect against writing rules | Minor | Variable; version change now excluded; noise not excluded |
| P-6 | Question discipline slips | 2, 3 | Skill defect | Minor | 2 of 5 multi-turn; both re-asks were for material never supplied |
| **F-25** | Date, model, loading and version never captured | all | **Test defect** | Major, retroactive | 6 of 6 |
| Process | No transcript header, no tester ID, turns lost on paste | all | Test defect | Major | 5 of 6 lost a turn |
**Verified external claims added by this review.** Scenario 1's 12-month re-referral window: correct, per DfE children in need methodology. Scenario 5's "140-odd areas": consistent with 153 children's services authorities in England, which should be confirmed. Both are correct and unmarked, which strengthens the "unmarked, not unreliable" reading of P-5.
**Behaviours to protect.** Contaminated-measure warning on both counts (6 of 6). Falsifiability probe where a conclusion is assumed in advance (4 of 6, and correctly absent in 5 and 6). Conversion of delivery problems into evaluation findings (4 of 6). Exporting evidence discipline to the user's future behaviour (4 of 6). Refusing to pad an option set, in both directions (5 and 6). Any change that removes one of these has failed.
---
## 5. Change proposals
Each is a hypothesis for the owner. Smallest change capable of fixing the observed problem, with a replay and a counter-case.
### 5.1 Skill changes
**CP-7. Label anything supplied from the agent's own knowledge. Target: `house-rules`, Evidence discipline. Priority: first.**
- *Evidence.* Six sessions; 8 unguarded instances of four kinds (statistic, frequency claim, structural fact, sub-claim adjacent to a cited source); 4 positive controls where a named source or a missing case number was guarded correctly; 3 unguarded claims verified correct, 1 verified wrong, 2 verified drifted.
- *Mechanism.* The current rule bans inventing figures, sources and reference classes, and bans presenting background knowledge "as evidence about the user's case". The agent reads that as applying to specific identifiable claims. General assertions it believes to be true, and characterisations of sources it has just read, are not registered as claims at all. The confident ones get the weakest guard.
- *Change.* One addition, worded on the model already in `library/.claude/skills/librarian/SKILL.md`. Four categories, kept apart in every reply: what the user supplied, what a source says, what the agent inferred from the material, and what the agent believes from general knowledge. The label goes "in the sentence that makes the point, not in a caveat at the end", once, and the reply proceeds. A claim's population or qualifier travels with it or the claim is not made. A citation covers the finding checked, not adjacent statements; "the same paper", "similarly" and "this also shows" do not transfer it. Give one example of each form the record produced. Using the librarian's wording matters: it is the only version of this rule T001 has written and used, and it keeps the three repositories saying the same thing.
- *Why it improves the package.* The product's pitch is that the user can trust what it says because it marks what it does not know. At present the user has no signal separating a correct legal claim (Scen 6) from a wrong statistic (Scen 4), so the rational response is to check everything, which removes the tool's value, or check nothing, which is what happens. A one-label rule restores the signal without removing the agent's ability to say "I would expect".
- *Failure replay.* Scen 4 "two-thirds" acquires a population and a source, or becomes "my understanding is". Scen 2 loses "the same paper". Scen 3 keeps the short-run qualifier. Scen 1 states the 12-month window as the agent's understanding before the instruction to confirm.
- *Counter-case, mandatory before and after.* C-9: a brief where the agent's background knowledge is genuinely useful and the user needs a direct answer. It must answer, with one label, and not hedge every sentence. `house-rules` already records that the framework ban, read too broadly, produced evasive answers on the first test. The same failure is available here and it would be worse than the defect.
- *Regression risk.* Medium. Over-labelling, and hedging facts the user supplied.
- *Confidence.* High on the mechanism; medium on the wording until C-9 has run.
**CP-4. Tie the problem system map to an observable trigger. Target: `problem`, move 9. Priority: second.**
- *Evidence.* Did not fire in either `problem` run despite two candidate cores being named in turn 1 of each. The revision history says it was patched once already for firing "late and vaguely".
- *Mechanism.* "Where the user has several linked issues, and a hierarchy always counts" is a judgement call inside a move that fires late. The standing instruction to name the hierarchy fires; the map attached to it does not.
- *Change.* If two candidate cores have been named, or three or more of problem, mechanism, symptom and constraint have been labelled, produce the map.
- *Why it improves the package.* The map is the artefact that keeps a user from defining one problem while holding another. Both sessions had the material for it and the user left without it.
- *Replay.* Both `problem` transcripts meet both conditions.
- *Counter-case.* C-3: a genuinely single-level problem must not receive a map.
- *Confidence.* Medium-high. Reproduced 2 of 2.
**CP-9. Verify an assurance about the output before making it. Target: `story`, self-check. Priority: third.**
- *Evidence.* Scen 6, F-27.
- *Mechanism.* The covering note asserts a property of the document ("nothing here is a figure I produced") that was not checked against the document.
- *Change.* Add to must-pass: where the output asserts a property of itself, the assertion is verified against the output or not made.
- *Why it improves the package.* A wrong assurance is more damaging than no assurance, because it switches off the reader's own scrutiny at exactly the point the register is meant to direct it.
- *Replay.* Scen 6: the 9 goes, or the assurance goes, or the Issue placeholders are filled.
- *Counter-case.* The agent must keep stating what discipline it applied. The fix is verification, not silence.
- *Confidence.* Medium-low. One instance, pending the missing turn; the general form stands regardless.
**CP-8. Say what a contested framing produces when a single artefact is requested. Target: `problem`, move 8. Priority: fourth.**
- *Evidence.* F-23. Scen 1 picked and supplied a swap; Scen 5 produced both drafts with a comparison table.
- *Change.* The owner's choice: either both variants when an artefact is requested, or the preferred one with the alternative attached, and the condition selecting between them.
- *Why.* Predictability. A user running both would not know what they will get, and the two resolutions carry different costs.
- *Counter-case.* C-12: a user who chooses when asked must get one clean draft.
- *Confidence.* Medium.
**Hold.** CP-1 (sentence count before returning a statement) reproduced 1 of 2. CP-6 (durations as figures) needs the hyperbole boundary settled first. CP-5 (split-sentence negated reframes) rests on counts of 3, 5, 2, 1, 1, 0 made by reading; a version change is now excluded (no skill commit since 18 August), but sampling noise and output format are not. `civicworks/.claude/skills/voice-dna/scripts/check.py` already detects reframe constructions mechanically and has tests. Run it over the six transcripts before touching the rule. Note that T001 has already found on his own published prose that "not just X, but Y" runs at 11 per essay and downgraded it from a violation, and that hard bans fire inside quoted titles. The rule in `house-rules` may be stricter than his own practice, and the checker will say so.
### 5.2 Test process changes
These come before any skill edit, because they are retroactive and they gate every cross-session claim.
1. **Capture header on every run, before pasting:** date, model, skills loaded, search on or off, plugin version or commit, tester ID from `evals/testers.md`, cold or warm. `evals/README.md` already requires this; none of the six has it.
2. **Export rather than paste.** Five of six sessions lost a user turn. Scenario 6's missing turn is currently blocking a major finding.
3. **Run the counter-cases before editing anything.** C-8: a sound pilot with a cooperative user. C-10: a stakeholder case where the obvious explanation is right. C-11: a draft whose success measure is sound. C-9: useful background, direct answer needed. Six adversarial sessions cannot show whether the agent accepts good work, and the evaluation method names "only trigger cases tested" as the failure that produces an agent that challenges everything.
4. **Run Part 0 of the alpha pack** to confirm `house-rules` loads through the plugin. Every classification above that says "against `house-rules`" is conditional on it.
5. **Report as n testers / m sessions.** Every pattern here is 1 tester. A second tester on two of the same briefs would do more for confidence than four more sessions from the same person.
---
## 6. Regression and capability banks
**Promote to regression** (behaviour seen in 2 or more contexts):
- R-13. Contaminated measure named as unsafe as evidence and as a success measure, with the mechanism (Scen 1, 2, 3, 5, 6).
- R-14. Falsifiability probe fires where the user states a conclusion in advance (Scen 1, 2, 3, 4).
- R-15. Position held under pressure: preferred conclusion, weakening disclosure, deadline; recommendation unmoved, output still delivered (Scen 3).
- R-24. A named real evaluation offered with no detail is declined from memory, with what it would need to show and an offer to test it if named (Scen 1, 5).
- R-25. A contested framing survives to an output request and shapes the output (Scen 1, 5).
- R-21. The stakeholder table is left partly empty where the user supplied no evidence about motives (Scen 4). Counter-case for any change that forces the artefact.
- R-29. A drafted artefact carries a gaps register with source, time and which gaps block clearance (Scen 6).
- R-31. No closing question on a pure artefact task (Scen 6). Counter-case for the question-per-turn habit.
- R-18. Derived statistics correct; a confidence interval on a difference in proportions is the cheapest hard check (Scen 3).
**Capability bank** (hard, not yet reliable):
- C-9. Over-correction test for CP-7. Run before and after.
- C-8, C-10, C-11. Sound work that should be accepted.
- C-7. Characterisation drift: a real paper whose finding depends on a qualifier, and a question whose natural answer drops it.
- C-13. An artefact task where the agent makes an assurance about its own output.
- C-3, C-12. Single-level problem (no map); user who chooses a framing (one draft).
---
## 7. The companion repositories, and the elicitation question
### 7.1 What `library` and `civicworks` are
Neither repository mentions MDEE, and both describe themselves as "written for an audience of one". They are not capabilities. What they share with MDEE is a design philosophy, stated almost identically in each:
| Principle | `librarian` | `voice-dna` / civicworks | MDEE |
|---|---|---|---|
| Keep layers apart by who said what | Four categories that "never blur"; label in the sentence | Voice file vs wiki vs archive; `summary_by` field | Fact, interpretation, assumption, hypothesis, unknown |
| Never fill a gap | "Nothing in the library supports that" is a real answer | "If there is no real material, ask for some rather than inventing" | A marked gap is a finding |
| Human is the author; agent proposes | `sources/` is his; wiki restructures are proposals | `voice-dna.md` never edited as a side effect | The user decides; `evaluation` edits no skill |
| Same writing rules | No em dashes, blunt working notes | No em dashes, no reframe constructions, "uncertainty is content" | `house-rules` How to write |
| Build nothing ahead of the material | Wiki starts empty | Wiki split deferred until a mechanism passes 60 lines | No `syntheses/` directory until there is something to synthesise |
The failure mode each is built against is the same one. The librarian calls it *fluent blending*: "if a paragraph reads beautifully and you cannot say which sentence came from where, it is wrong." That is P-5 from these runs.
### 7.2 How they would have changed the runs
**`library` addresses roughly a third of P-5.** The three verified source failures (Scen 2 misattribution, Scen 3 dropped qualifier, Scen 3 unanchored Smith and Todd) are what a populated library prevents: retrieval from a card carrying verbatim passages, or "nothing in the library supports that". Scen 1's Leeds and Scen 5's Family Hubs would have become lookups rather than refusals. It does nothing for the five general-background instances ("two-thirds of local authorities", "most pilots skip it", "the most common silent veto", "no £14m decision is made monthly", PSED timing), because those are not source claims. And the library is empty today. CP-7 is still required; the librarian supplies its wording.
**`check.py` would have made P-1 deterministic.** See CP-5 above.
**`civicworks` should not be loaded into MDEE.** `wiki/mechanisms.md` holds T001's positions (capability sits downstream of the decision; conditions matter more than the container; learning arrives after commitment). Echoes of them are audible in the runs already (Scen 1 "what the pilot is allowed to claim"; Scen 4 "the fix is design, not persuasion"). Loading his essays into the agent would turn a general tool into a personalised one, which `evals/README.md` already warns against. The separation looks deliberate: method for everyone, reading and voice for one.
### 7.3 On `grilling`, `grill-with-docs` and `wayfinder`
**Do not recommend `grilling` as written.** It asks "the whole frontier in one round": every unblocked question, numbered, with a recommended answer. `house-rules` says "one focused, substantive question at a time: probing, never polite filler, never a batch", and names over-interviewing "a user who has already given you the material" as "the failure to watch". The `problem` revision history records the first real test finding exactly that failure. The runs show the one-question rule holding in 4 of 5 multi-turn sessions and users redirecting freely when it slipped. Scen 5's user pasted a complete draft and said "tell me what's wrong with it"; a grilling round there is the failure the rule exists to prevent. Recommending batch elicitation asks T001 to reverse a deliberate, evidenced design choice.
**The gap the runs do show is one level down, and three things point at it:**
1. Open questions get lost. Scen 2's "who signs the growth decision" was asked three times and never answered; Scen 3's comparison group size, likewise. The agent named both non-answers as findings, but nothing carried them forward except its memory of the conversation.
2. Users traverse capabilities in one conversation (F-13), so case state accumulates with nowhere to live. `house-rules` says it dropped the original agent's case record because chat "has no persistence layer".
3. The agent already produces the right structure when asked for an artefact. Scen 6's gaps register (what fills each gap, where from, how long, which ones block clearance) is `wayfinder`'s map in miniature: decisions so far, not yet specified, out of scope.
**The recommendation to make instead** is a lightweight running case register: what has been settled, what is open with a recommended answer, what has been ruled out, maintained across turns and surfaced on request, in the shape the agent already uses in `story`. This is a product-level proposal, not a `house-rules` edit. Two things from `grilling` are worth borrowing into it: "finding facts is your job, never the user's" (two sessions had search available and the agent still asked the user for things it could have looked up), and a recommended answer beside each open question, which `house-rules` half-asks for already. `grill-with-docs` adds ADRs and a glossary, whose MDEE analogue is the case record T001 removed. `wayfinder` needs an issue tracker and is built for multi-session work; its idea travels, its machinery does not.
**Gate this on C-8 and C-10.** If the agent over-interviews a user who has supplied everything, or a case where the obvious answer is right, the question rule is already too weak and any elicitation change makes it worse. If it handles both cleanly, the register stands on its own.
**Resolved from T001's own description.** `library` is intended as his personal research assistant for drafting, and `civicworks` is a prototype for a customerfirst wiki. So the librarian is a pattern for CP-7, not a dependency: CP-7 borrows its wording and nothing else, and MDEE should not assume the library exists. If a shared evidence layer for MDEE users ever becomes a goal, the librarian is the design to start from.
---
## 8. Recommendations, in order
| # | Recommendation | Type | Evidence | Gate |
|---|---|---|---|---|
| 1 | Capture header on every run; export transcripts; tester ID | Process | F-25; 5 of 6 sessions lost a turn; `evals/README.md` already requires it | None. Do first |
| 2 | Run C-8, C-10, C-11, C-9 | Test | 6 of 6 adversarial; `evaluation` names "only trigger cases tested" as the failure | Before any edit |
| 3 | CP-7 in `house-rules`, librarian wording | Skill | 6 of 6 sessions; 3 right, 1 wrong, 2 drifted, all unmarked | C-9 before and after |
| 4 | CP-4, `problem` system map trigger | Skill | 2 of 2 `problem` runs | C-3 |
| 5 | CP-9, `story` verifies self-assurances | Skill | Scen 6 F-27 | Missing turn, if recoverable |
| 6 | Run `check.py` over the six transcripts | Test | P-1 counts unstable; T001 has already loosened the rule on his own prose | Before CP-5 |
| 7 | Running case register across turns | Product | Scen 2 and 3 unanswered questions; F-13; Scen 6 gaps register | C-8 and C-10 |
| 8 | Part 0 of the alpha pack: confirm `house-rules` loads | Test | Every "against `house-rules`" classification is conditional on it | None |
| Hold | CP-1, CP-5, CP-6 | Skill | 1 of 2; noise; hyperbole boundary | Next batch |
| Do not | Adopt `grilling` batch elicitation; load `civicworks` into MDEE | | Conflicts with an evidenced `house-rules` rule; personalises a general tool | |
---
## 9. What this evaluation cannot tell you
- Whether any finding reproduces on a second run or a second model. One tester, one unnamed model.
- Whether `house-rules` was loaded in any session.
- Whether the agent accepts sound work. Untested after six scenarios.
- Whether the "9 non-pilot areas" figure was supplied or produced.
- Whether the IPS England effect sizes and the Smith and Todd characterisation are accurate. Scenario 3's business case rests on the first.
- Anything about a naive user. This tester redirected, conceded and pushed for output more than most users will.
- Whether the agent over-interviews a cooperative user. Untested, and it gates recommendation 7.

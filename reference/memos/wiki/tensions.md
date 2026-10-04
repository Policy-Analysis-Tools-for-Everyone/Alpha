# Tensions and open questions

Where the corpus and `story` (with `storytelling-guidance.md` behind it)
disagree, or where the corpus asks something the skill doesn't answer. Each
tension ends with a **change hypothesis**: a proposal, not a decision. None has
been made. A hypothesis reaches a skill only through the method layer, and only
with a test in `../../../evals/` to show the change works.

Delete a tension when it is resolved, and record how in `log.md`.

---

## T1. The cover note is a section the skill doesn't know about

`storytelling-guidance.md` says the brief allows a 1-page cover letter. The
skill's PPC mode lists 8 sections and no cover note. 4 of 5 memos have one, and
a marker singled M02's out for praise (P12). M01's holds the evidence the memo
needs (P12).

**Change hypothesis.** PPC mode knows a cover note may be required, says what
it is for (context on the authoriser and drafter, for the marker), and checks
that nothing the decision maker needs lives only there.

## T2. The 8 sections read as a rule

The skill's PPC mode says "Eight sections in order", and its *PPC mode must
also pass* list has one line per section, so it would fail M03 (4 of 8
sections, P11). The body says sections may be omitted; the opening line and the
checklist don't.

**Change made, 2026-10-04.** The one change this corpus has prompted: `story`
now treats the 8 sections as a guide, and helps the writer see what each
section would do for this reader and what leaving it out would cost. The
checklist asks whether each section's job is done or deliberately dropped.
Recorded in `log.md`. Small on purpose: 5 memos are not enough evidence for
more.

## T3. Letter register

`writing.md`: no "I" or direct address in a document "unless the format is a
personal note or letter". 4 of 5 memos are letters from a named sender in role
and use "I", "we" or "you". This is consistent with the exception, but PPC mode
doesn't say a role-played memo is usually a letter. Low priority.

## T4. Themed headings

M01 heads its sections with film metaphors ("Cast of characters", "Lights,
camera, action!") for a film-maker reader. `writing.md` wants formatting that
reduces the reader's work, and `story` wants descriptive titles. A marker
praised the writing and said nothing about the headings.

**Open.** One memo, no marker comment. Needs a case where a marker reacts.

## T5. The writing controls versus what markers reward

P10: markers praise clarity, signposting and tightness, and never mention the
`writing.md` vocabulary or dashes. Not a reason to drop the controls, which
exist because readers distrust machine voice. It is a reason to order the work:
chain, risks and numbers before polish.

**Change hypothesis.** None for `writing.md`. For `story`, possibly the
self-check order, which nearly does this already. Needs more evidence.

## T6. The corpus carries the module's frame

4 of 5 recommendations redirect or condition existing money (P8). `house-rules`
treats market failure versus direction as a live disagreement the agent
surfaces rather than settles. A skill that learned from these memos by example
would settle it, towards conditionality, without saying so.

**Rule, not hypothesis:** nothing from this corpus enters a skill as an
example of a *good recommendation*. Only moves of form and reasoning (how an
issue is opened, how a chain is checked) are candidates. The
recommendations themselves are the authors' policy judgements in one module's
frame.

## T7. "Why this, not that?" has no home

The markers' sharpest question in the corpus: why should arts money go to film
rather than novels or visual arts, and why not benchmark against them? (M01,
raised by a marker and in the peer session.) Its twin, from the M01 author to M04: who are
the innovation leaders and what do they do? Both ask the memo to place its case
against the alternatives a sceptical reader holds in mind: other claimants on
the money, other countries' answers.

`story` compares the recommendation with the strongest *option*. Neither it nor
the rubric asks about other claimants or comparators. The question belongs
upstream: `problem` (why is this the problem to spend on?) and `evidence` (what
have comparable places done?).

**Change hypothesis.** `story`'s strongest-objection step names the 2 common
forms: "why this group or sector and not another?" and "what did comparable
places do?". If the analysis can't answer either, that is an upstream return,
not a sentence to write around. Add R16 to the rubric.

## T8. Markers disagree on M03's recommendation

One marker thought the reasoning pointed to Option IV as primary; the other
agreed with Option I, and added that the spillover benefits of housing decide
the choice. That is one value judgement (relief now against the structural fix)
deciding the case, and the memo doesn't state it. `story` already says "if one
value judgement decides the choice, state it".

**Evidence for an existing rule**, not a new one. Useful as a test case: give
M03 to the agent and see whether it names the judgement.

## T9. Good analysis in the wrong proportion

The rubric rates M04's analysis Strong. Its marker's main point is that an
expert reader needed less of it and more implementation. `story` sides with the
marker ("adjust depth to what the decision maker already knows"); the rubric's
R4 rates quality without fit, and R14 carries fit alone.

**Change hypothesis (rubric).** R4 and R9 are rated for this reader, not in the
abstract. The rubric was wrong here, and the marker right.

## T10. Bundled options

`story` says don't manufacture a third option, and M05 doesn't: 2 options for a
binary choice. Both its markers still made the options the weakest part, because
each option bundles 3 instruments with different costs and lead times (P6). The
count was right and the unit was wrong.

**Change hypothesis.** Options mode in `story` (and `options` upstream) checks
the unit: an option is one decision. If its parts could be chosen separately,
either show them separately or say why they stand or fall together.

---

## Open questions

**Q1. What does a weaker memo look like?** The corpus has no contrast. 3 to 5
memos the maintainer judges middling would show whether P1 to P6 separate
strong memos from weaker ones, or are true of all memos. Without them no
pattern here is a claim about quality.

**Q2. Does `story` catch what the markers caught?** Give the agent each memo
cold, ask for a review in PPC mode, and compare its findings with
`../raw/*-feedback.md` and with P1. It is a test with a real answer key. It
belongs in `../../../evals/tests/`, using the memos as input and never
putting them in a skill.

**Q3. Does the rubric need the markers' left column?** P9: markers bring
judgement about the decision's world (benchmarks, second-order effects,
political readings) that the rubric doesn't ask for. T7 adds one criterion.
Whether more are needed waits on more memos.

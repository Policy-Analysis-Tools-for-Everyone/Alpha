# Research design: policy reasoning with policymemo.ai

**Status: draft 1, 2026-10-04.** A proposal for the research team. Not submitted to any
ethics committee, and no data has been collected. Nothing here changes the product.

The UCL seminar sequence used below is the **2025-26 PGTA plan, which is a draft and
last year's**. Week numbers are indicative only. Every research moment is defined by
the analytical job it sits on, so it can move to wherever that job lands in 2026-27.
[`open-questions.md`](open-questions.md) lists what is needed to fix them.

---

## 0. Summary

1. **The environment decides the design.** policymemo.ai is 11 skills running inside
   each student's own Claude, Copilot or Gemini account. There is no server, no log and
   no telemetry. Every transcript lives in a student's account and reaches the study
   only if the student exports it. The design has to work with that, not around it.
2. **The course and the agent teach the same thing.** The skills are grounded in the
   course's own readings (Bardach, Donahue on the strategic triangle, *Getting to Yes*,
   Reinikainen, Sharpe et al., Slaughter and McGuinness, Demos Helsinki, May, Weimer and
   Vining) and `story` reproduces the PPP memo template. So a student using the course
   vocabulary is evidence of nothing, and an improvement could be the teaching.
3. **The agent forces some behaviours.** It strips solutions from problem statements,
   asks *compared with what, for whom, over what period, with what consequence*, marks
   placeholders and gives a four-part readout. Seeing those in a transcript or in an
   artefact written straight after one is not evidence of improved reasoning.
   [`prompt-footprint.md`](prompt-footprint.md) lists what each skill prompts and the
   trace it leaves.
4. **So the core evidence is agent-free work, compared over time and across
   sequences.** Short in-seminar artefacts written without the agent, at a baseline,
   inside each research moment and at the end, are the only measures the agent cannot
   have produced.
5. **3 designed moments and 2 anchors** across the term, not one per week:
   framing, evidence and causal claims (or stakeholders), and integration through peer
   review, plus an agent-free baseline and endpoint on a common case.
6. **One form, three fields, about 5 minutes per moment** is the whole of what a
   participating student does beyond the teaching itself: paste the current version,
   answer 3 short change-note prompts, and optionally attach the transcript.
7. **Sequence is the one manipulation.** At UCL, half the PPP groups take the agent
   after group discussion and half before, then swap. This is a teaching-equivalent
   crossover, small enough to see mechanisms and too small to estimate effects.
8. **Cambridge and McGill test mechanisms, not outcomes.** Mechanisms seen at UCL are
   written as observable signatures and looked for in donated transcripts from
   naturalistic use. No cohort comparisons.
9. **Seminar recording is not recommended.** Its value for the questions is small
   relative to its consent and analysis cost.
10. **The research and the evals stay two ledgers.** A research finding can open an
    evals prompt. It never edits a skill directly, and participant data never enters
    this public repository.

Two things found in the repository need action before an ethics submission, and are
listed in section 12: the student beta route currently couples **beta access** to
**research consent**, and **the term may already have started**.

---

## 1. The environment the study has to work in

What the repository shows about where the student beta will actually run.

| Fact | Where it is | What it does to the research |
|---|---|---|
| The product is skills loaded into the student's own AI tool: Claude (plugin or uploaded zips), Copilot or Gemini (ports) | `CONTRIBUTING.md`, `ports/README.md`, `site/install/` | No product-side data. Transcripts come only by student export. The tool's own terms govern what students type |
| Copilot and Gemini run a compressed core (`ports/core.md`), not the full skills | `ports/README.md` | "The agent" differs by surface. Surface is a variable to record, and possibly to fix at UCL |
| The model is chosen by the student's account and changes outside our control | `evals/README.md` headers | Model is a variable to record for every transcript |
| Version lives in `marketplace.json`, stamped into every skill; the beta ships `0.2.0` | `CLAUDE.md`, `CONTRIBUTING.md` | A version can be frozen for the term and recorded per episode |
| Nobody can tell whether a skill loaded in an ordinary chat | `evals/wiki/findings.md` F2 | A transcript may show the base model, not policymemo.ai. Coding must check |
| Students may use Projects or memory | `evals/wiki/findings.md` caveats on T002 | Later sessions may carry earlier context. Record it |
| Beta access is a person-run gate: Microsoft Form, List, two Power Automate flows. The student form is "UCL only" and is to carry the information sheet and consent | `site/beta/README.md`, `site/beta/body.html` | Consent and access are currently coupled. See section 12 |
| Student feedback goes to a study form, "stays within the study", and only what consent allows reaches `evals/` | `evals/README.md`, ingest channels | The evals side already expects a research boundary. This design defines it |
| The repository is public on GitHub | `CONTRIBUTING.md` | `research/` holds protocols and aggregates only. No participant data, ever |
| The agent's stance: the user is the author and decides; it challenges and does not affirm; one question per turn; invents nothing | `skills/house-rules/SKILL.md` | The agent is designed to provoke contest. That is good for RQ2 and means contest is partly prompted too |
| `story` has a PPC memo mode that drafts the 8-section PPP memo | `skills/story/SKILL.md`, `reference/sources/ucl-ppc-one-pager-instructions.pdf` | The agent can write the assessed artefact. Assessed work cannot be read as the student's reasoning without a use declaration |
| Known agent behaviours at `0.1.1`: unmarked general knowledge (F1), stakeholder under-firing inside problem work (F12), over-production (F13), reliable contaminated-measure catch (F3) | `evals/wiki/findings.md` | Natural cases where the agent is right and where it is wrong. Needed to judge whether students rely on it appropriately |
| Course structure: a Personal Policy Problem developed all term, pre-assigned PPP small groups, roughly 14 students per seminar, a memo assessed mid-term and a final memo | the 2025-26 plan, the PPP instructions | One seminar group is a small n. Pre-assigned groups make a group-level crossover possible |

**Consequence.** The study cannot measure "what the agent does" from the product, and
should not try. It measures what students do and produce, in moments where the
sequence and the agent-free work are designed, and uses donated transcripts to see
what happened in between.

---

## 2. Research questions, refined

### Primary

> **How do postgraduate students' policy reasoning and judgements change through
> interaction with policymemo.ai, and under what conditions does that interaction build
> their capacity for independent analytical judgement rather than substitute for it?**

Two changes from the current wording. "Develop" becomes "change", because a term-long
study of 1 seminar group can see change and its conditions but cannot attribute
development to the agent against the course. And "strengthen or weaken" becomes
"build or substitute for", because the worrying outcome is less a student who reasons
worse than one who stops doing the reasoning and still produces good-looking work.

### Subsidiary

**SQ1. Change.** On which dimensions of policy reasoning do students' artefacts change
after interaction, and do those changes appear (a) on dimensions the agent did not
prompt in that session, and (b) in later agent-free work?

*Refines current Q1. Part (a) and (b) are what separate reasoning change from template
uptake (section 4).*

**SQ2. Uptake.** How do students respond to the agent's moves (accept, adapt, reject,
contest, defer, ignore), and how well does that response track whether the move was
sound?

*Refines current Q2. "How well it tracks soundness" is the definition of appropriate
reliance, and needs the agent's moves rated independently of the student's response.*

**SQ3. Entry point.** How does a student's state on arrival at the agent (a committed
individual position, a group-tested position, or none) shape what they take from it and
what they keep?

*Refines current Q3. "Entry point" becomes "arrival state", which can be designed at UCL
and observed in any transcript, so the same variable works at every site.*

**SQ4. Substitution.** Where and when do signs of substitution appear: adoption without
stated reasons, convergence of the cohort on the agent's framing, thinner agent-free
work over the term, or inability to reproduce a change without the agent?

*New. Without it, the design is tilted towards finding benefit. The primary question
names both directions, so each needs its own indicators.*

**SQ5. Transfer across settings.** Which mechanisms identified in structured UCL
moments also appear in naturalistic use elsewhere, and what features of the teaching
context accompany their presence or absence?

*Refines current Q4. Asks about mechanisms, not about comparable outcomes.*

### Out of scope, and why

- **Whether policymemo.ai improves grades or learning outcomes.** No control group, one
  seminar group, the course teaches the same content, and assessment cannot be tied to
  research participation.
- **Prevalence**: how often students at large do X. Volunteers and donated transcripts
  are not a sample of anything.
- **Whether policymemo.ai is good.** That is the evals question (section 13).

---

## 3. Conceptual model

### 3.1 Policy reasoning

Working definition: **the way a person gets from a concern about the world to a choice
they can defend, and the quality of each link in that chain.** Ten dimensions. The first
8 follow the analytical work the course teaches; the last 2 cut across them.

| | Dimension | Visible in an artefact as |
|---|---|---|
| D1 | **Framing** | The problem as a condition rather than a fix; scope, affected group, magnitude, time; whose framing it is and what it rules out |
| D2 | **Causal reasoning** | A stated mechanism; causal claims marked as claims; competing explanations; the difference between what causes a problem and what can be changed |
| D3 | **Evidence use** | Claims attached to sources; provenance distinguished; applicability argued; gaps marked rather than filled; weak measures recognised |
| D4 | **Uncertainty** | What is unknown and of what kind; which uncertainty matters to the choice; what would settle it; calibrated rather than uniform hedging |
| D5 | **Actors** | Interests separated from positions; power made concrete; who must act or consent; who is missing |
| D6 | **Alternatives** | Genuinely different mechanisms; a base case; no decoys; options tied to what the actor can change |
| D7 | **Criteria and trade-offs** | What counts as better, stated before options are scored; what is given up for what; who gains and loses |
| D8 | **Judgement** | A position taken; the decisive reason; what the choice accepts; what would reopen it |
| X1 | **Coherence** | Whether the parts hang together: the options answer the problem stated, the criteria come from it, the recommendation follows from the trade-off |
| X2 | **Reflexivity** | The analyst's own position, interests and normative stance made visible; the difference between personal conviction and systemic analysis (the course's own week 1 aim) |

**Why the rubric must not be the agent's.** Every skill has a self-check that could be
used as a scoring list. Using it would measure conformity to the agent. The codebook
should be derived from the course learning objectives and the policy-analysis
literature, then checked against [`prompt-footprint.md`](prompt-footprint.md) so that
every indicator is tagged *prompted by skill X* or *not prompted*. X1, X2, the
creativity of options in D6 and the political judgement in D5 and D8 are where the
agent is weakest at prompting, and they are therefore the most informative dimensions.

### 3.2 Independent analytical judgement

Working definition: **the capacity to form, defend and revise an analytical position on
grounds the student can state, and would apply without the agent present.**

"Independent" does not mean unaided. Deciding well what to take from a tool, a peer or
a reading is part of judgement. The question is whose judgement decides.

| | Component | Strengthening looks like | Substitution looks like |
|---|---|---|---|
| J1 | **Authorship** | The framing or position originates with the student, or is substantially reworked by them | The agent's revised statement adopted near-verbatim |
| J2 | **Discrimination** | Sound agent moves accepted, unsound ones questioned or rejected | Acceptance regardless of soundness, including unmarked agent knowledge |
| J3 | **Reason-giving** | Changes and refusals explained in substantive terms ("the figure moves with call-centre capacity") | Explained by authority ("it said", "it's more professional") or not at all |
| J4 | **Responsiveness without capitulation** | Holds a position against fluent pushback unless given a reason; moves when given one | Folds at the first challenge, or ignores a good one |
| J5 | **Transfer** | Applies the move unprompted: to a new case, a peer's work, or a later draft without the agent | The move appears only in the agent's presence |
| J6 | **Distinctiveness** | Students' framings stay varied across the cohort | Framings converge on the agent's template |

J2 needs a judgement of whether each agent move was sound, made by someone other than
the student and blind to their response. That is the one point where the research uses
evals-style judgement, and it is used as a variable, not as a finding about the
product (section 13).

J5 and J6 are the components the agent cannot produce on the student's behalf. They
carry the most weight.

### 3.3 Arrival state

The variable for SQ3. Coded for every episode at every site, from the artefact and the
opening turns of the transcript.

- **A0 Nothing**: a topic or concern, no framing.
- **A1 Private position**: a framing the student wrote alone.
- **A2 Tested position**: a framing that has been through peer challenge.
- **A3 Worked solution or draft**: an answer the student wants tested.

`house-rules` already distinguishes these on arrival ("a vague concern, rough notes, a
worked solution, an inherited proposal, a draft"), so the agent's behaviour should vary
with them, and that has to be read off the transcript, not assumed.

---

## 4. The prompted-behaviour problem

The methodological constraint is the centre of the design, so it gets its own section.

**The problem.** The agent is built to make students do certain things. If `problem`
challenges a solution-shaped statement, a revised statement without the solution is
what the agent asked for. If `house-rules` asks *compared with what*, a student adding
a comparator is compliance. The course teaches the same moves, so even agent-free
improvement could be teaching.

**What counts as independent evidence, strongest first:**

1. **Agent-free transfer to a new case.** The move appears in work on a common case the
   student has not discussed with the agent, written in the seminar without devices.
   The anchors (section 5) do this.
2. **Agent-free persistence on their own case.** The move appears in a later version of
   their own problem written without the agent, after the session that prompted it.
3. **Application to someone else.** The student makes the move on a peer's work in a
   seminar exercise. The week 6 peer review is where this is natural.
4. **Divergent form.** The move appears in the student's own terms rather than the
   agent's wording or template, for example a comparator argued for rather than a
   placeholder copied.
5. **Unprompted in session.** In a transcript, the student makes the move before the
   agent asks for it, which is visible across turns or across sessions: answering
   *compared with what* before being asked.
6. **Change on a dimension the session did not prompt.** If only `problem` ran, a
   change to the student's options reasoning was not prompted by that session.

**What is not independent evidence:** the move appearing in the transcript after the
agent asked for it; in the artefact written straight after; in the agent's vocabulary;
or in the change note, where the student is describing what they did, not showing it.

**How the design handles it:**

- [`prompt-footprint.md`](prompt-footprint.md) lists, per skill and per version, what the
  agent prompts and the textual trace it leaves. It is derived from `skills/` and must
  be updated when a skill changes.
- Every coded change carries a **prompted** flag: was this move asked for in the
  transcript of this episode? Where no transcript was donated, the flag is *unknown*,
  and the change counts only towards SQ1 if it reappears agent-free.
- A simple **echo check** compares the student's revision with the agent's text for
  near-verbatim overlap. High overlap is a substitution signal for J1, not a quality
  judgement.
- The **anchors** and the **agent-free snapshots** are the primary outcome measures.
  Transcripts explain them; they do not replace them.

**On the teaching confound.** The design cannot separate the agent's contribution from
the course's in the agent-free measures, because every student gets both. What it can
do is compare *within* students across sequences (the crossover) and look for change
that follows specific agent moves in time. That supports claims about mechanisms and
conditions, which is what the primary question asks. It does not support "the agent
improved reasoning", and the write-up should say so.

---

## 5. Research moments at UCL

### 5.1 The basic pattern

Each designed moment is an ordinary seminar activity with two additions: an agent-free
snapshot at the start, and a short change note at the end.

```
t0  individual, agent-free, in seminar          → snapshot 0
    group reasoning (PPP small group)            → group output
t1  individual, agent-free, after group          → snapshot 1   (optional: see 5.4)
    policymemo.ai                                → transcript (if donated)
t2  individual revision                          → snapshot 2 + change note
```

For the reverse sequence, the agent comes before the group, so `t1` follows the agent.

### 5.2 Candidate moments assessed

All 7 candidates, with a recommendation. The test for each: does it sit on a real
seminar activity, does it produce an agent-free artefact naturally, does it give the
agent something it does well *and* something it does badly, and is the analytical
change observable in a short written artefact?

| Moment | Where it sits in 2025-26 | Natural artefact | Agent evidence (`evals/`) | Recommendation |
|---|---|---|---|---|
| **Problem framing** | Wk 1 PPP introduction; wk 2 "initial draft statement", who you write as, decision maker | A 1-2 sentence problem statement | `problem` is the most tested skill; strong on hidden solutions and vague terms; system map defect (F7) | **Core.** The course's own spine, short artefact, change is visible |
| **Evidence and causal reasoning** | Wk 6 heading (plan empty); 2022-23 had students bring a paper for their intervention | Causal chain plus the evidence for each link | F1 unmarked agent knowledge, F3 reliable measure catch | **Core, or swap with stakeholders.** Best moment for J2: the agent is both right and wrong here, naturally |
| **Stakeholders** | Wk 4 stakeholder map; 2022-23 had 3 stakeholders × 5 interests | Map or table | F12: under-fires inside problem work, strong when it is the task | **Alternative to evidence.** Existing group exercise; tests whether students catch missing actors |
| **Alternatives and trade-offs** | Wk 5 options and criteria; wk 8 portfolio | Option set with base case | No evidence on `options` or `trade-offs` as the leading skill | **Not designed in year 1.** Observed through the integration moment and the memo |
| **Uncertainty** | Wk 2 unknowns; wk 5 irreducible uncertainty | Thin as a standalone artefact | Spread across `evidence`, `outcomes`, `decide` | **Not a standalone moment.** Coded as D4 in every moment |
| **Experimentation** | Wk 2 testing framework | Overlaps with uncertainty | Inside `evidence` | **Not a standalone moment** |
| **Integration into a recommendation** | Wk 6 memo pitch and peer review with de Bono hats; wk 7 memo workshop | Pitch outline (problem, reader, alternatives, proposal, evidence) and "one piece of advice to incorporate" | `decide`, `story`; F13 over-production | **Core.** Already has rotation and a change log built in |

### 5.3 The recommended set

| | Moment | Indicative timing | Student time beyond teaching |
|---|---|---|---|
| **A0** | Baseline anchor: agent-free critique of a short common case | Week 1 or 2 | 15 min, as a seminar activity |
| **RM1** | Problem framing | Week 2 | ~5 min |
| **RM2** | Evidence and causal reasoning, or stakeholders | Week 4 or 6 | ~5 min |
| **RM3** | Integration through peer review | Week 6 or 7 | ~5 min |
| **A1** | Endpoint anchor: agent-free critique of a matched common case | Week 9 or 10 | 15 min, as a seminar activity |

Plus, with separate consent, the **final PPP memo** read for persistence after marking,
and **6 to 8 stimulated-recall interviews** after marks are released.

### 5.4 Each moment in detail

**A0 and A1: anchors.**
- *Activity.* Students read a short policy memo extract and write, without devices, what
  problem it defines, what they would challenge and what is missing. Then discuss. This is
  a normal seminar warm-up; week 1 already does it with the Apple memo.
- *Why it matters.* The only measure on a case that is the same for every student and
  that no student has taken to the agent. Primary evidence for SQ1(b), J5 and SQ4.
- *What it needs.* 2 extracts of matched difficulty, counterbalanced across the group if
  possible (half do extract X first). The Apple memo and the week 9 Oyster case are not
  matched: one is a memo, the other a case. Whether to write matched vignettes is a
  question for the teaching team.
- *Burden.* None beyond the activity. The research use is a photo or a typed copy.

**RM1: problem framing.**
- *Activity.* Each student writes their current PPP problem statement (`t0`). PPP small
  group challenges it using the seminar's own questions (who you write as, who decides,
  what is unknown). Students take it to policymemo.ai (in seminar, or before next week).
  Revise (`t2`) and write the change note.
- *Sequence contrast.* Half the PPP groups do group then agent; half agent then group.
  Swap at RM3. Every student gets both orders across the term.
- *Why here.* Framing sets everything after it, and the course's teaching note names the
  danger exactly: students who pick an audience that can say yes to a preconceived
  solution. `problem` targets the same failure, so it is the clearest test of whether
  students learn the move or receive it.
- *What it generates.* 2 or 3 versions of 1-2 sentences each; a change note; a group note
  of challenges raised; optionally a transcript.
- *What to look for.* Whether the solution is gone, and whether it is gone again in RM2's
  `t0` without the agent. Whether the cohort's framings converge (J6). Whether
  group-first students contest the agent more (SQ3).

**RM2: evidence and causal reasoning.**
- *Activity.* Each student brings one source for their PPP and writes the causal chain it
  supports, link by link (`t0`). Small group tests applicability and missing links.
  Agent. Revise and change note.
- *Why here.* `evidence` is where the agent both catches weak measures reliably (F3) and,
  at the version tested, states its own general knowledge unmarked (F1). Students will
  meet both without anything being planted, so J2 is observable. **No deliberate errors
  are introduced**; that would be deception and would need its own ethics case.
- *If stakeholders is chosen instead.* Same pattern on the week 4 map. The analogue of
  J2 is whether students notice actors the agent leaves out (F12).

**RM3: integration through peer review.**
- *Activity.* The week 6 pitch and peer review, with policymemo.ai added as one reviewer
  among the rotating peers. Students already have to "note one piece of advice to
  incorporate". The addition: note where each piece of advice came from, and which they
  will act on.
- *Why here.* It places agent advice and peer advice side by side and asks the student to
  choose. That is the most direct observation of SQ2 available, and it is already the
  shape of the activity. It is also the natural place to see students make the agent's
  moves on someone else's work (independent evidence, level 3 in section 4).
- *What it generates.* The pitch outline before and after; a source-tagged advice list;
  the change note.

**Final memo (consent tier 3).**
- Read after marks are ratified, by someone who did not mark it, for whether changes
  traced in RM1 to RM3 survived. Requires the course's AI-use declaration, because
  `story` can draft it.

**Interviews (consent tier 4).**
- 6 to 8, after marks are released, by someone other than the tutor. Stimulated recall:
  the student's own versions and transcript in front of them. Purposive: students whose
  episodes show contrasting patterns (high and low echo, contest and deference,
  converged and distinctive). This is the strongest evidence of *why* reasoning changed.

### 5.5 Why `t1` is optional

A post-group, pre-agent snapshot isolates the group's contribution from the agent's, and
is what the sequence contrast needs at its cleanest. It also adds a third rewrite inside
one seminar. Recommendation: take `t1` in RM1 only, where the statement is 2 sentences
and the rewrite costs a minute, and drop it in RM2 and RM3.

---

## 6. Sources of evidence, assessed

### 6.1 Four kinds of evidence

| | Kind | Question it answers | Best sources | Cannot come from |
|---|---|---|---|---|
| **E1** | What the agent did | Which moves, how sound, at which version | Transcript | The student's account; the agent's own debrief |
| **E2** | What the student thought | Their position and their reading of the agent at the time | Snapshots, chat turns, change note | Agent output |
| **E3** | That reasoning changed | A difference between versions on a coded dimension, and its persistence | Snapshots, anchors, later work | A transcript alone; a self-report alone |
| **E4** | Why it changed | The source and reason for a change | Transcript aligned to versions, change note, interview | Any single source. Self-report is post-hoc; transcripts show sequence, not reason |

The commonest error to guard against is using E1 as E3: the agent produced a better
statement, so the student's reasoning improved.

### 6.2 Each source

| Source | Value | Burden on students | Burden on team | Evidence | Recommendation |
|---|---|---|---|---|---|
| **Before and after seminar artefacts** | High. The core measure | Low: produced by the teaching | Medium: rating | E2, E3 | **Use** |
| **Agent-free anchors** | High. The only common, unprompted measure | Low: a seminar activity | Medium: vignettes, rating | E3 (transfer) | **Use** |
| **Change note** (3 prompts) | High for E4, if triangulated | Low: 3 minutes | Low | E2, E4 | **Use** |
| **Donated transcripts** | High for E1 and for aligning changes to moves | Low to export; high sensitivity | High: redaction, coding | E1, partial E2 and E4 | **Use, for research moments only**; self-directed sessions optional |
| **Group outputs** | Medium. Context for SQ3 | None | Low | Group E2 | **Use**, as context |
| **Tutor observation notes** | Medium. Group process, what peers raised | None | Low: 10 min after seminar | Context | **Use**, structured, group-level only |
| **Short questionnaires** | Medium. Moderators (AI familiarity, policy experience) and perceived ownership | Low if kept to 2 × 5 min | Low | Moderators, E2 | **Use**, start and end only |
| **Final or intermediate assessed work** | Medium. Persistence | None | Medium | E3 (persistence) | **Use with separate consent**, after marking, with AI-use declaration |
| **Interviews or focus groups** | High for E4 | 30-45 min, voluntary | High | E4, E2 | **Interviews, 6-8. Not focus groups**: peers' presence distorts accounts of one's own reliance, and PPP topics identify people |
| **Agent-generated debriefs** | Low for research. A model grading itself (`evals/README.md`) | Medium | Low | Weak E1 only | **Do not use as research evidence.** Never ask the agent to write the change note |
| **Product data in `evals/`** | Context: what the agent tends to do at a version | None | Low | E1 at product level | **Use as context only**, not as data about participants |
| **Seminar recording or transcription** | Low to medium. Would show group reasoning in detail | High: chills discussion of half-formed ideas | Very high: transcription, consent of every person present, non-consenters | Group E2 | **Do not use** (6.3) |

### 6.3 Seminar recording

Recording would give the fullest view of group reasoning before the agent (SQ3). Against
it:

- **Consent is all or nothing.** One non-consenting student in a group means that group
  cannot be recorded, and the pressure on that student to agree is exactly the
  coercion the ethics case has to rule out.
- **It changes the seminar.** The course asks students to bring half-formed problems and
  their own biases into the room. A recorder discourages that, and that harm falls on
  non-participants too.
- **The analysis cost is high** and the questions do not need it. SQ3 needs to know what
  position a student held on arrival at the agent and what the group challenged. The
  `t1` snapshot and the group output give that directly.
- **PPP topics are identifying**, often drawn from students' own workplaces.

If a specific gap appears after year 1, a narrower option exists: audio of 2 or 3 small
groups in RM1, with every member opted in, held separately. Not recommended now.

---

## 7. Minimal-burden collection

What a participating student does, in total, across the term:

| When | What | Time |
|---|---|---|
| Consent (by a third party) | Information sheet, tiered consent, a self-generated ID code | 10 min, once |
| Start | 5-minute questionnaire | 5 min |
| A0 | Nothing extra: the anchor is a seminar activity; hand in a copy | 0 |
| RM1, RM2, RM3 | One form: paste the version(s), answer 3 change-note prompts, optionally attach the transcript | ~5 min each |
| A1 | As A0 | 0 |
| End | 5-minute questionnaire | 5 min |
| After marks (some) | Interview | 30-45 min, voluntary |

**About 40 minutes across a term, plus an optional interview.** Non-participants do the
same seminar activities and submit nothing.

**The change note.** 3 prompts, the same each time, written by the student without the
agent:

1. What did you change, and why?
2. What did you decide not to change, though someone (a peer or the agent) suggested it?
   Why not?
3. What are you still unsure about?

Prompt 2 is the important one. Rejections are the evidence for J2 and J4 and are
otherwise invisible: a rejected suggestion leaves no trace in the revised artefact.

**The form.** One form for every moment, on UCL systems, keyed by the self-generated
code. It is a research instrument and separate from the beta access form. Its design
waits on the ethics decisions in section 12.

**What is not collected.** All other sessions, unless a student chooses to donate them
(SQ3 self-directed use). Grades. Anything from non-consenting students, including tutor
notes that would identify them.

---

## 8. Which evidence answers which question

| | A0/A1 anchors | Snapshots | Change note | Transcript | Group output, tutor notes | Questionnaire | Final memo | Interview | Naturalistic transcripts |
|---|---|---|---|---|---|---|---|---|---|
| **SQ1 change** | ●● transfer | ●● | ○ | ● prompted flag | | | ● persistence | ○ | |
| **SQ2 uptake** | | ● | ●● rejections | ●● moves and responses | | ○ perceived | | ● | ● |
| **SQ3 arrival state** | | ●● `t0`/`t1` | ● | ●● opening turns | ● what peers raised | | | ● | ●● natural variation |
| **SQ4 substitution** | ●● trend, J5 | ●● echo, J6 | ● reasons | ● deference | | ○ | ● | ● | ● |
| **SQ5 across settings** | | | | ●● UCL signatures | | ● moderators | | | ●● |

●● primary · ● supporting · ○ weak or perceptual

---

## 9. UCL and naturalistic deployments

### 9.1 What each setting can teach

| | UCL (structured) | Cambridge, McGill (naturalistic) |
|---|---|---|
| **Control** | Sequence, timing, agent-free artefacts | None. Students meet the agent in whatever teaching exists |
| **Evidence** | Snapshots, anchors, change notes, transcripts, interviews | Donated transcripts, a short reflection, a teaching-context descriptor from the course team |
| **Can establish** | Mechanisms and the conditions they need, within this cohort | Whether those mechanisms appear elsewhere, under what conditions, and mechanisms UCL did not anticipate |
| **Cannot establish** | Effects against no agent; generalisation | Change in reasoning (no before and after); outcomes; any comparison of cohorts |

### 9.2 How mechanisms travel

From UCL, write each candidate mechanism as a context, a mechanism and an outcome, and
as a **signature**: something observable in a transcript alone, because a transcript is
all a naturalistic site may give. Candidates to test, not findings:

| Mechanism | Context | Signature in a transcript |
|---|---|---|
| **Pre-commitment** | Arrival state A1 or A2 | More reject, qualify and contest codes; the student defends with reasons |
| **Template capture** | Arrival state A0; an artefact requested early | Student accepts the agent's revised statement and moves on; asks for the next output |
| **Fluency deference** | Agent supplies general knowledge unmarked (F1) | The claim is accepted and reused without query |
| **Challenge internalisation** | Second or later session | Student pre-empts the agent's challenge ("compared with last year's figure, ...") |
| **Offloading** | Deadline near; student's turns shorten | "Just write it", "you decide"; the agent's *the user decides* rule is tested |
| **Peer buffering** | Group-tested position | Student cites peers' challenge when resisting the agent |

At naturalistic sites, look for each signature, its context and its absence. A
mechanism seen at UCL and not elsewhere under similar contexts is a finding; so is one
seen elsewhere under contexts UCL never had. Search actively for negative cases.

### 9.3 What naturalistic sites should give

- **From students, voluntarily:** a transcript they choose to share, with 3 questions
  (what you were trying to do; what you took from it and what you didn't; whether this
  was your first session). Arrival state is coded from the transcript.
- **From the course team, once:** a teaching-context descriptor. Course level, what is
  taught about problem definition and evidence, whether and how the agent was
  introduced, the course's AI-use rules for assessment, which surface students use.
- **Nothing that requires the site to change its teaching.**

### 9.4 Selection, stated plainly

Donated transcripts will over-represent engaged students, successful sessions and
students comfortable with the researchers. They cannot show how often anything happens.
They can show that a mechanism *occurs* under conditions UCL did not have, which is
what SQ5 asks.

---

## 10. Analysis

### 10.1 Unit

The **episode**: one student at one research moment. It holds the snapshots, the change
note, the group output, any transcript, and the version, model and surface. Across the
term, a student is a **case** of 3 episodes and 2 anchors.

### 10.2 Coding layers, kept separate

| Layer | What is coded | Who | Blind to |
|---|---|---|---|
| 1. Quality | Each snapshot and anchor on D1-D8, X1-X2 | 2 raters on a shared subset, 1 on the rest | Time point, sequence, student |
| 2. Change | Each difference between versions, with its source (self, peer, agent, unclear) and a *prompted* flag | 1 rater with the transcript | Quality ratings |
| 3. Uptake | Each substantive agent move and the student's response (accept, adapt, reject, contest, defer, ignore) | 1 rater | Soundness ratings |
| 4. Soundness | Whether each agent move was sound, with a reason, using the evals method | A rater outside the uptake coding | Student response |
| 5. Reasons | Change-note and interview reasons: substantive, authority-based, none | 1 rater | Quality ratings |
| 6. Echo | Near-verbatim overlap between student revision and agent text | Computed | |

Layers 3 and 4 combine into the reliance matrix for J2: sound and accepted, sound and
rejected, unsound and accepted, unsound and rejected. The off-diagonal cells are the
interesting ones.

Shuffling snapshots before layer 1 matters more than inter-rater statistics at this
size. Report agreement on the double-coded subset and how disagreements were resolved.

### 10.3 Analytic moves

1. **Within-case process tracing.** For each student, trace a change from its first
   appearance through the sequence of peer and agent moves to its persistence or loss in
   later agent-free work.
2. **Cross-case matrices.** Episodes by arrival state, by sequence arm, by uptake
   pattern. Count as `n students / m episodes`, the evals convention. Never percentages.
3. **The crossover.** Compare each student's group-first and agent-first episodes. With
   about 14 students the comparison describes, it does not test.
4. **Cohort convergence.** Diversity of framings across the cohort at `t0` and `t2`, and
   at A0 and A1. Convergence after the agent but not after peers is a J6 signal.
5. **Trend in `t0` quality.** If agent-free first drafts get thinner across RM1-RM3 while
   revised versions improve, that is anticipatory offloading (SQ4).
6. **Mechanism signatures.** Write them up from UCL, then code naturalistic transcripts
   against them, keeping a column for patterns that fit none.

### 10.4 Rules the analysis follows

- **The analysis plan is committed before data arrives.** The commit is the timestamp.
  Deviations are logged with reasons.
- **The codebook is not the skills.** Indicators come from the course and the literature
  and are tagged against the footprint, not taken from a self-check.
- **No LLM as primary coder.** Using a model to judge text partly shaped by a model is
  circular, and sending participant data to a model provider needs ethics and data
  protection approval of its own. A model may be used later as a secondary check on
  coded, de-identified data, if approved.
- **Version, model and surface travel with every claim.** As in `evals/`, nothing at one
  version is evidence about another.
- **An independent co-analyst** codes or audits a share of the material. The tutor built
  the product (section 11).

---

## 11. Validity threats and limitations

| Threat | Why it is live here | What the design does | What remains |
|---|---|---|---|
| **Prompted behaviour read as reasoning** | The agent forces specific moves | Footprint, prompted flag, agent-free measures, echo check | Agent-free measures are still shaped by prompted habits, which may be the point |
| **Course and agent teach the same thing** | Skills grounded in the course readings and memo template | Within-student sequence contrast; change aligned in time to agent moves | No attribution of improvement to the agent |
| **The tutor is the researcher and built the product** | Demand effects ("say it helped"); allegiance in analysis | Third-party consent; tutor blind to participation until after marks; independent co-analyst; interviews by someone else | Students know who built it. Say so in the write-up |
| **Small n, one seminar group** | ~14 students, fewer consenting | Case-based design; counts not rates | Findings are about mechanisms in this setting |
| **Self-selection** | Consent and donation are voluntary | Report who did not participate in broad terms, if ethics allows | Donated transcripts skew to good sessions |
| **Product changes mid-study** | The beta exists to iterate | Version freeze for the UCL term (section 13) | Model updates by providers are outside anyone's control. Record them |
| **Surface heterogeneity** | Copilot and Gemini run a compressed core | Record surface; consider asking UCL students to use one surface for research moments | Equity: students may not all have the same access |
| **Did a skill even load?** | F2: nobody can tell | Code from transcript; flag episodes where it cannot be established | Episodes without transcripts are unknown |
| **AI use outside the study** | Students may use other AI on their PPP | Agent-free snapshots and anchors written in seminar; questionnaire asks | Out-of-seminar work is uncontrolled |
| **Post-hoc rationalisation** | Change notes explain after the fact | Triangulate with transcript sequence and stimulated recall | Reasons remain partly reconstructed |
| **Curated transcripts** | Students choose what to share | Ask for whole sessions; record if partial | Cannot be fully ruled out |
| **Assessment pressure** | The PPP is assessed; the agent can draft it | No research task tied to assessment; final memo only with consent and declaration | Students may use the agent differently in assessed weeks |
| **Maturation** | Students improve over a term anyway | Within-moment `t0`→`t2` changes are short-interval | Anchor change is not attributable |
| **Non-equivalent anchors** | A0 and A1 cases may differ in difficulty | Matched vignettes, counterbalanced | Matching is never perfect |
| **Novelty** | First contact with the agent | Look at change across RM1-RM3, not just RM1 | Year 1 is all early use |
| **Cross-site non-comparability** | Different courses, teaching, AI rules | No cohort comparisons; mechanisms only | |

---

## 12. Ethics and consent: issues to resolve

Identified here, not solved. Several are decisions for the ethics committee and the
course leadership, not the research team.

### 12.0 Who the researcher is, and what follows

Confirmed 2026-10-04: the researcher is the PGTA who teaches the seminar, and the
author of policymemo.ai. The module lead is the course's lead academic.

- **This is UCL research, whatever the researcher's own affiliation.** A UCL employee is
  collecting data from their own students, in a UCL seminar, through their teaching
  role. Ethics review cannot be skipped and justified afterwards: data collected
  without approval is unlikely to be approved retrospectively or accepted by a journal,
  and the risk falls on the module lead as well as the researcher.
- **The module lead has given written permission** (scope to confirm: see U10 in
  `open-questions.md`). That is the department's agreement; it is not ethics approval.
- **Agreed route.** The module lead is sponsor. A second PGTA, who does not teach or
  mark this group, takes consent, holds the consent list and the code key, receives
  donated transcripts and conducts the interviews. The draft consent form, on the IIPP
  LREC template, is `ethics/consent-form-draft.docx`.
- **Until approval:** teaching use only, plus product feedback under the `evals/`
  rules. No research data. Decisions and agreements are kept in a dated log
  (`research/log.md`, once created), so the paper trail exists from the start.
- **Three roles in one person** (tutor, researcher, product author) are the main thing
  the ethics case has to answer, and they are declared, not managed quietly.

### 12.1 Found in the repository, needing action first

1. **Beta access is currently coupled to research consent.** `site/beta/body.html` says
   the student form "includes the study's information sheet and consent", and
   `site/beta/README.md` says to set the cohort to `Invited` "once their consent is in
   place". If the agent is used in seminars, access is part of the teaching, so a student
   must be able to get access without consenting to research. Access and consent need
   separate instruments, and access must not wait on consent. **This is a product and
   operations change to make after the design is agreed, not now.**
2. **Timing.** Term starts on Thursday 2026-10-08, so the week 1 seminar is days away
   and approval will not be in place for it, and probably not for week 2. Neither
   consent nor research data can be taken before approval. The plan that follows:
   - **Submit to the LREC this week.**
   - **Weeks 1 and 2 run as teaching only.** A0 and RM1's drafts are written as normal
     seminar work and kept as teaching material, unseen by anyone for research.
   - **Ask the LREC in the application** whether those artefacts can be included with
     consent taken after approval. If yes, the baseline survives. If no, the study
     starts at RM2 without A0, and RM1 becomes a pilot of the instruments.
   - Nothing about the teaching in weeks 1 and 2 depends on the answer.

### 12.2 Consent

- **Tiered consent**, each tier independently refusable:
  1. Use of in-seminar artefacts and change notes
  2. Donation of transcripts from research moments
  3. Use of assessed work, after marking
  4. Interview
  5. Anonymised findings informing product development (`evals/`)
  6. An anonymised excerpt committed to the public repository. **Default: no, for
     students.** The evals ingest table already treats student material this way
- **Who asks.** Not the tutor. A third party introduces, collects and holds consent.
- **Beta product news** (`UpdatesOptIn`) is separate from all of the above. The beta
  README already says so.

### 12.3 The tutor-researcher

**Confirmed 2026-10-04: the tutor marks the PPPs.** So the tutor must not know who has
consented, donated or withdrawn until marks are ratified. Pseudonymisation alone does
not achieve that: in a group of about 14, the tutor recognises each student's PPP topic.

The design that follows from it:

- **Collection is teaching; inclusion is research.** Every student completes the
  in-seminar artefacts and the change note as part of the teaching, so submitting
  reveals nothing. The third party holds the consent list and, after ratification,
  removes everything from non-consenters before the research team sees any of it.
  This needs the ethics committee's agreement.
- **Transcripts go to the third party, not the tutor,** and stay sealed until
  ratification.
- **No research analysis by the tutor before ratification.** Year 1 analysis starts
  after the final memo is marked. Interviews and any reading of assessed work happen
  after that too.
- **Marking work produced with one's own product is a second conflict.** Students may
  use `story` to draft the memo the tutor marks. Declare it, and ask whether the module
  can arrange moderation or second marking of this group's PPPs.
- Participation, non-participation and withdrawal must have no route to assessment.
  The information sheet says how this is guaranteed, in operational terms.
- Research moments must be defensible as teaching for everyone in the room, including
  non-participants and those who opt out of AI use.

### 12.4 Participating without contributing

- Every research moment is a teaching activity first. Non-participants do it and submit
  nothing.
- Tutor notes are about group process and must not record anything identifying a
  non-participant.
- **A student who will not use an AI tool** (on principle, privacy or cost) needs an
  equivalent teaching path, for example peer-only review in the agent step. Whether the
  course can require AI use at all is a course and institutional decision.

### 12.5 Withdrawal

- Up to a stated date (for example, before aggregated analysis begins), after which
  data already merged into aggregates cannot be removed. The date must be real and
  stated.
- Self-generated codes let students withdraw without the tutor learning who withdrew.

### 12.6 Pseudonymisation and identifiability

- Research IDs are a separate key space from evals `T0NN` IDs, and there is no crosswalk
  in this repository. If a student also files product feedback, the two are not linked
  here.
- **PPP topics identify students** in a cohort of 14, to classmates and the tutor. Quotes
  must be checked for topic identifiability, not only names. The evals convention of
  substituting figures and organisations is a good start and not sufficient on its own.
- The key linking codes to people is held by the third party, not the tutor.

### 12.7 Transcripts

- PPPs are "of personal significance" and often drawn from students' workplaces, so
  transcripts can contain third-party, employer and sensitive personal information.
- Redaction before ingest, by the student with guidance or by the third party; who, and
  when, is a decision.
- Transcripts are held on UCL systems (the beta README already requires this). Never
  in this repository, never in a Claude Project or memory, never pasted into an AI tool
  for analysis without specific approval.
- Students have already entered the content into a third-party AI provider under that
  provider's terms. The study adds a second copy; it does not create the first. The
  teaching decision to use the agent does create the first, which is a course matter.

### 12.8 Assessed work

- Whether assessed work can be used at all is an institutional question. If it can:
  separate consent, after ratification, read by a non-marker, never affecting marks.
- The course's AI-use declaration is necessary to read it at all, because the agent can
  draft it.

### 12.9 Across institutions

- UCL approval will not cover Cambridge or McGill participants by default. Each may need
  its own approval, or a reliance agreement, or a local sponsor.
- McGill sits under Canadian research ethics (TCPS 2) and Quebec privacy law; transfer of
  data from Canada to the UK needs checking.
- Different AI-in-assessment rules at each site change what students can safely share.
- Naturalistic donation needs an information sheet that works without a seminar to
  explain it.

---

## 13. Research and product iteration

### 13.1 Two questions, two ledgers

| | `evals/` | `research/` |
|---|---|---|
| **Question** | What does policymemo.ai do, and how should it change? | What happens to students' policy reasoning when they use it? |
| **Object** | The agent | The student's reasoning |
| **Unit** | Session, skill, version | Episode, student, moment |
| **Strongest evidence** | Transcript | Agent-free artefacts, aligned to transcripts |
| **A good result** | A defect found and fixed | A mechanism understood, whichever direction it points |
| **Consent** | Tester consent to publish | Tiered research consent, held off-repo |
| **Lives in** | The public repository | Protocols here; data on UCL systems |

The same transcript can be read by both. Consent tier 5 has to cover it, and the two
readings stay in their own ledgers.

### 13.2 How findings move

- **Research to product.** A research finding with a product implication becomes an
  evals prompt in `evals/wiki/prompts/`, citing the research finding by its ID and
  carrying no participant data. From there it follows the normal evals loop: case,
  change, regression, cold re-test. **Research findings never edit a skill directly.**
- **Product to research.** Evals findings at the version in use are interpretive context.
  F1 is why J2 matters; F12 is why the stakeholder moment would be informative.
- **Agent soundness ratings** (layer 4) use the evals method and could become evals
  sightings, with consent tier 5. They remain covariates in the research.

### 13.3 Version freeze

A study measuring student change against a product that is changing under it measures
neither. Recommendation:

- **Freeze the version used at UCL for the research term**, for example `0.2.x`.
  Changes only at pre-announced points such as reading week, each recorded against the
  research moments it falls between.
- **Same version for all sites** in the same window, where possible.
- Provider model changes cannot be frozen. Record the model on every episode.
- Across years, this becomes a design-based research cycle: year 1 findings inform the
  product, year 2 studies the revised product. That is legitimate if declared in
  advance.

### 13.4 The firewall

`evals/README.md`: nothing about a tester reaches policymemo.ai. The research needs the
same rule, extended:

- No research instrument, codebook, moment design or participant material goes into a
  skill, a Project, a system prompt or memory.
- The agent must not know a student is in the study, and must not behave differently for
  them.
- The research team does not configure students' Projects. If students build their own,
  that is naturalistic and is recorded.

---

## 14. What should and should not be instrumented

The product has no runtime of its own. Anything called instrumentation would mean either
changing what the skills say, or building a backend. Both change the product for every
user, at every site, which is what the study is trying to observe.

### Should not be instrumented

| Proposal | Why not |
|---|---|
| **Telemetry or logging** | No backend exists; adding one changes the privacy model for every user and the terms students accepted |
| **Reflection prompts inside the skills** ("before revising, say why") | Makes reflection a prompted behaviour, which the study then cannot use as evidence. Changes the product for non-study users |
| **A study mode or study detection** | Gives UCL students a different agent from everyone else, and breaks the evals firewall |
| **Agent-written change notes or debriefs** | A model's account of the student is not the student's account |
| **Automatic transcript sharing** | Consent must be per transcript, and redaction comes before sharing |
| **Behaviour changes aimed at the research moments** | The seminar should design the moment; the agent should stay the product |

### Should be recorded, outside the product

- Version, model, surface, date, and whether a skill can be seen to load, on the form.
- Arrival state, coded from the transcript.
- Whether Projects or memory were in use.

### Could be considered later, as product decisions for all users

- A one-line answer when a user asks which version they are running. The version is
  already stamped into each skill's metadata; whether the agent reliably reports it is
  an evals question.
- Documentation in `/install` on how to export a conversation from each surface. That is
  documentation, not a skill change.
- Keeping [`prompt-footprint.md`](prompt-footprint.md) current whenever a skill changes.
  That is repository maintenance, not runtime.

---

## 15. What is still needed

[`open-questions.md`](open-questions.md) lists every piece of missing information and
every decision, with who can answer it and what it blocks. The ones that block the most:

1. The 2026-27 seminar sequence, and which activities the tutor controls.
2. The ethics route, its timeline, and whether the term has started.
3. Whether the tutor marks or influences marking of PPPs.
4. The course's AI-use rules for assessment, and which AI surface students will have.
5. Who the third party for consent and interviews is.
6. Contacts and course structure at Cambridge and McGill.

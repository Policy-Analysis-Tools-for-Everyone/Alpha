# Evaluating and Improving the Agent - Method Guidance

> **Sources and provenance:** This method is designed for the MDEE.MD alpha and is grounded first in the project's own behaviour specification and real evaluation transcripts. It is informed by **[E]** `evals/transcripts/*`, which the project already treats as behavioural evidence of what the agent actually did; **[B]** `docs/BEHAVIOUR_SPEC.md`, which distinguishes configured behaviour from observed behaviour; **[A]** Anthropic, “Demystifying evals for AI agents” (2026), especially its guidance on real failures, multi-turn transcripts, capability versus regression evals, balanced task sets, grader choice, repeated trials, and transcript review; and **[O]** OpenAI, “How evals drive the next chapter in AI for businesses” (2025), especially its feedback-loop model of logging real inputs, outputs and outcomes, reviewing them, adding new failure modes to evals, and using those findings to improve the system. **Purpose:** Operating instructions for an evaluation skill that turns real use of MDEE.MD into evidence for improving its skills. The evaluator studies *how people actually use the agent*, where the agent helps or fails, which patterns recur, and what specific skill changes should be tested next. It does not automatically rewrite the skills.

## Why this method exists

The alpha is itself a learning system.

The skills describe how the agent is intended to behave.

Real conversations show how that behaviour works when people bring:

- incomplete problems
- messy documents
- real organisational constraints
- unexpected requests
- different levels of policy experience
- different ways of asking for help

Those conversations are evidence.

The evaluation method should turn them into a disciplined improvement loop:

> **real use -> transcript -> session review -> finding -> pattern -> change hypothesis -> skill revision -> regression test -> cold re-test -> new evidence**

The aim is to improve the agent from observed behaviour without overfitting it to one conversation or one user's preferred style.

---

## The overall model

Evaluate the agent at 4 levels.

### 1. The session

What happened in this particular conversation?

Did the agent understand the user's goal, apply the right method, ask useful questions, challenge weak reasoning, and produce something the user could use?

### 2. The skill

What does the session reveal about the relevant `SKILL.md`?

Did an instruction fail to fire?

Was a rule ambiguous?

Did 2 instructions conflict?

Did the skill produce the intended behaviour but that behaviour turn out to be unhelpful in practice?

### 3. The skill system

What does the session reveal about how skills work together?

Examples:

- the wrong skill triggered
- 2 skills duplicated each other
- a hand-off happened too early or too late
- a cross-cutting house rule was missing
- a behaviour belongs in another skill
- the user wanted to move through several methods in one conversation

### 4. The product

What does the session reveal about what people are actually trying to do with MDEE.MD?

Examples:

- a use case appears repeatedly that was not anticipated
- people use `problem` to critique documents rather than write statements
- people want to move directly from evidence to an experiment
- users repeatedly ask for an artefact the current skill does not produce
- users struggle to know which module to invoke
- a method works analytically but creates too much interaction cost

Keep these 4 levels separate.

A product insight does not automatically imply a prompt edit.

---

## Four evaluation modes

The evaluation skill should support 4 related jobs.

### Mode 1 - Review one session

Use when given a single transcript or conversation.

Purpose:

- reconstruct what the user was trying to achieve
- identify what the agent did
- compare that behaviour with the relevant skill contract
- identify defects, strengths, surprises, and open questions
- propose specific next tests or changes

### Mode 2 - Synthesize several sessions

Use when given several eval records or a folder of transcripts.

Purpose:

- identify recurring patterns
- distinguish isolated incidents from repeated behaviours
- compare contexts in which a behaviour succeeds or fails
- identify skill-level or system-level changes worth testing
- update the capability and regression test backlog

### Mode 3 - Design an eval

Use when a skill is being created or changed.

Purpose:

- turn the skill's important behaviours and known failure modes into test cases
- include cases where the behaviour **should** occur and where it **should not**
- define what a fair pass looks like
- identify which tests are capability tests and which are regression tests

### Mode 4 - Review a proposed skill change

Use after a skill has been revised.

Purpose:

- replay the failure that motivated the change
- check that the change fixes the intended behaviour
- run counter-cases to detect over-correction
- re-run existing regression cases
- identify what still requires a cold real-user test

---

## Core rules

### 1. Treat real transcripts as behavioural evidence

Configuration tells us what the agent was told to do.

A transcript shows what it actually did.

Preserve both.

For evaluation, the transcript is the primary evidence about observed behaviour.

Do not infer that a rule worked because it appears in `SKILL.md`.

Check whether it fired in the conversation.

### 2. Evaluate the version that was actually tested

Every usable eval record should identify, where possible:

- module or modules used
- skill version or commit
- model
- date
- whether house rules or other skills were loaded
- relevant tools or environment
- tester type
- whether the run was cold or warm

Do not judge an old transcript against the current version of a skill without stating that the skill has changed.

If the tested version is unavailable, say so and limit the certainty of the assessment.

### 3. Separate a real user run from a warm author run

A **cold run** is performed by someone who did not author the skill and is not steering the agent towards known success criteria.

A **warm run** involves the skill author, someone familiar with the expected behaviour, or a conversation in which the agent has already seen the method or test expectations.

Both are useful.

They answer different questions.

Warm runs are good at finding structural defects quickly.

Cold runs provide stronger evidence of how the skill behaves for an ordinary user.

Always label which kind of run produced the finding.

### 4. Reconstruct the user's actual goal before grading the agent

Do not grade the transcript solely against the module name.

Ask:

- What was the user trying to get done?
- What information did they supply?
- What did they expect the agent to do next?
- Did that goal change during the conversation?
- Did the user skip or reject a question?
- Did they ask for a direct output rather than the skill's default process?

A method can be followed correctly and still fail the user's task.

### 5. Judge the conversation, not only the final answer

MDEE.MD is conversational.

Evaluate:

- what the agent noticed
- what it challenged
- what it asked
- what it chose not to ask
- when it produced an output
- whether it adapted when the user changed direction
- whether later turns corrected or compounded earlier errors
- the final usable state reached with the user

A polished final paragraph can hide a poor interaction.

A useful conversation may also contain an imperfect intermediate answer that was successfully corrected.

### 6. Judge outcomes as well as method fidelity

Method fidelity matters because the skills encode intentional policy-analysis behaviour.

User outcome matters because the tool exists to help someone make progress.

Keep both.

Ask:

**Method fidelity**
- Did the skill apply its important rules?
- Did required challenge behaviour occur?
- Were must-pass checks respected?
- Did the skill remain inside its intended boundary?

**User outcome**
- Did the user get closer to solving the task?
- Was the output usable?
- Did the conversation expose an important issue the user had missed?
- Did the user have to repeatedly restate instructions?
- Did the agent create avoidable work?

Do not assume user satisfaction proves analytical quality.

Do not assume perfect rule-following proves usefulness.

### 7. Evaluate against explicit behaviour before subjective preference

Start with the strongest evidence:

1. explicit must-pass rules in the relevant skill
2. explicit shared rules in `house-rules`
3. the method source the skill is grounded in
4. documented product behaviour
5. observed user outcome and feedback
6. evaluator judgment

A clear violation of an explicit behavioural contract is stronger evidence than "I would have written this differently."

Where the specification itself appears wrong, classify that separately.

### 8. Distinguish different kinds of finding

Every finding should be classified.

Use:

**Skill defect**
The skill says or implies the right behaviour, but the agent does not reliably perform it.

**Specification defect**
The skill's instruction itself produces poor behaviour, is ambiguous, conflicts with another instruction, or omits an important condition.

**Method gap**
Real use exposes an analytical need the current source method does not cover adequately.

**Cross-skill defect**
The issue sits between modules or in shared rules rather than inside one skill.

**Product / interaction insight**
The user's way of working reveals a need about routing, modes, outputs, workflow, or usability.

**Model variance**
The behaviour may depend materially on the model rather than the skill wording.

**Test defect**
The evaluation task, grading rule, or environment is unfair, ambiguous, or does not test what it claims to test.

**Observation**
Interesting evidence that does not yet justify a change.

Do not put every disappointing response in the "skill defect" bucket.

### 9. Record strengths as well as failures

Evaluation should preserve behaviours worth protecting.

A change that fixes one defect can remove something that worked well.

For each session, identify:

- behaviours that worked
- behaviours that failed
- behaviours that surprised
- behaviours that should become regression protections

A strong behaviour observed repeatedly can be just as important as a recurring defect.

### 10. Turn failures into testable claims

Weak finding:

> The response was too long.

Better:

> When the user asks for a direct revision after providing sufficient context, `problem` produces several long prose paragraphs rather than the required labelled output, making the 4 required components hard to locate.

The better finding specifies:

- context
- behaviour
- expected behaviour
- consequence

That can become an eval case.

### 11. Separate severity from frequency

A behaviour can be serious after 1 occurrence.

Another may need repeated evidence.

Suggested severity:

**Blocker**
The agent fabricates evidence, seriously misleads the user, violates a critical must-pass rule, or makes the task unusable.

**Major**
The behaviour materially weakens the analysis or user outcome.

**Minor**
The issue affects clarity, efficiency, structure, or polish without substantially changing the analysis.

**Observation**
No demonstrated defect yet.

Frequency is separate:

- single occurrence
- repeated within one session
- repeated across sessions
- repeated across users
- repeated across modules

Do not wait for 5 users before fixing an obvious, reproducible contract violation.

Do not create a global rule from one person's stylistic preference.

### 12. Look for false positives and false negatives

For behaviours that trigger conditionally, test both sides.

Examples:

- challenge a hidden solution **when one is present**
- do **not** challenge a neutral problem statement as though it contains a hidden solution
- ask another question **when necessary information is missing**
- stop questioning **when enough information is available**
- create a problem hierarchy **when several levels are mixed**
- do **not** force a hierarchy onto a genuinely simple problem

An eval suite that tests only "does it trigger?" will often produce an agent that over-triggers.

### 13. Preserve unexpected valid behaviour

An LLM can solve a task in a way the evaluator did not anticipate.

Do not fail a response solely because it took a different conversational path.

Grade the important outcome and behavioural constraints.

Where sequence matters to the method, test it.

Where it does not, avoid turning one preferred path into a brittle rule.

### 14. Use human judgment first for subjective policy-analysis quality

Early in the alpha, the most important judgments are likely to be:

- Was the challenge analytically sound?
- Did the agent identify the important uncertainty?
- Was the problem framing improved?
- Were the stakeholder motivations invented?
- Was the trade-off real?
- Did the output help the user think?

These require policy judgment.

Use human review as the primary standard while the eval language is still being discovered.

Model-based grading can be added later for repeated, well-defined judgments after it has been checked against human scoring.

### 15. Use deterministic checks for genuinely deterministic rules

Some behaviours can be checked simply.

Examples:

- a required field is present
- no fabricated placeholder has been converted into a number
- the output contains the required sections
- only one question is asked where the skill requires one
- a named module does or does not trigger
- a file was created at the required path

Do not use a model grader where a direct check is enough.

### 16. Grade different dimensions separately

Avoid one vague score such as `8/10`.

A useful session review can assess:

- **routing / mode selection**
- **method fidelity**
- **analytical challenge**
- **evidence discipline**
- **question discipline**
- **adaptation to the user**
- **output usefulness**
- **structure / clarity**
- **skill-boundary discipline**

Not every skill needs all of these.

The relevant skill's own must-pass rules should supply the most important dimensions.

### 17. Do not optimise for one golden answer

Policy analysis often admits several good outputs.

The eval should specify:

- behaviours that must occur
- behaviours that must not occur
- substantive points a good answer should recognise
- acceptable variation in wording or route

Use reference outputs as examples of a passing solution, not as text the model must mimic.

### 18. Build capability and regression evals separately

Use 2 suites.

**Capability evals**
Ask what the skill still struggles to do.

These should contain difficult, realistic cases and can have a meaningful failure rate.

**Regression evals**
Protect behaviour already shown to work.

These should be expected to pass almost all the time.

When a capability failure is fixed and becomes reliable, promote that case into the regression suite.

Do not treat one aggregate score across both suites as sufficient.

### 19. Let real failures seed the eval suite

Every meaningful failure from real usage is a candidate future test.

For each accepted defect, preserve:

- the triggering user context
- the behaviour that failed
- what success would have looked like
- any counter-case needed to prevent over-correction

A small initial suite of real cases is more useful than a large synthetic suite that does not resemble actual use.

As the alpha grows, expand coverage from observed usage.

### 20. Preserve full transcripts alongside condensed eval cases

The condensed test case is useful for regression.

The full transcript is useful for understanding why the behaviour happened.

Keep both.

A future evaluator should be able to inspect:

- the original conversational context
- the condensed failure
- the resulting skill change
- the regression case created from it

Do not replace the transcript with a retrospective summary alone.

### 21. Anonymise without destroying the analytical structure

Real policy work may contain sensitive or identifying material.

Before storing or sharing an eval transcript:

- remove personal data
- replace organisation or programme names where necessary
- substitute sensitive figures where necessary
- clearly label substituted numbers
- preserve the causal, organisational, and analytical structure required to reproduce the behaviour

Do not make the case so generic that the original failure can no longer be understood.

### 22. Record user feedback separately from evaluator judgment

Useful signals include:

**Observed behaviour**
What the transcript shows.

**User feedback**
What the user explicitly liked, disliked, corrected, ignored, or asked to change.

**Task outcome**
What usable state was reached.

**Evaluator judgment**
What the reviewer thinks this means for the agent.

Keep these separate.

A user saying "great" is evidence of satisfaction in that moment.

It is not proof that the analytical method was applied correctly.

### 23. Study how people use the tool, not only whether outputs pass

Across sessions, look for:

- which skills users invoke explicitly
- which skills are reached implicitly
- common starting materials
- common points where users skip the prescribed process
- when users ask for a draft immediately
- which outputs get reused or edited
- where conversations stall
- where users correct the agent
- where they repeatedly request a different level of detail
- unexpected journeys between skills
- recurring analytical needs that no skill owns

These are product-learning signals.

They can inform future skills, routing, instructions, and artefact formats.

### 24. Look for patterns with context attached

Do not report:

> Users dislike questions.

Report:

> In 4 of 6 sessions where users pasted a near-complete working document and asked for critique, they bypassed the skill's opening interview question and asked for a direct revision. In 3 exploratory sessions with only a rough issue, question-led interaction was accepted.

The second statement tells us **when** the behaviour is a problem.

Patterns without context produce bad global rules.

### 25. Do not count repeated turns as independent evidence

If one user objects to the same behaviour 4 times in one conversation, that is strong evidence about that session.

It is not 4 independent users.

Track:

- sessions
- users where known
- contexts
- models
- skill versions

Do not inflate confidence by counting correlated observations as independent cases.

### 26. Compare models when the model may be the variable

The same skill can behave differently across model versions.

Record the model for every eval where possible.

When a behaviour changes after a model update:

- run the same regression cases
- compare several trials where output variance matters
- inspect transcripts rather than relying only on aggregate scores

Do not silently rewrite a skill to compensate for a one-off model run.

### 27. Run more than one trial where variability matters

LLM outputs vary.

For deterministic contract checks, one reproducible failure may be enough.

For softer behaviours such as:

- degree of challenge
- concision
- question quality
- whether a subtle cue is noticed

run several trials before concluding that a prompt change has reliably worked.

Record both pass rate and the shape of failures.

### 28. Read the transcripts after grading

A score cannot tell you whether:

- the agent genuinely failed
- the task was ambiguous
- the grader rejected a valid route
- the prompt change fixed one problem while creating another

For important failures and surprising passes, inspect the transcript.

A fair failure should make sense when read by a human reviewer.

### 29. Propose changes as hypotheses, not automatic edits

The evaluation skill should **not modify another skill automatically**.

Instead produce a change proposal containing:

- target skill and section
- evidence from the transcript or pattern
- failure mechanism
- proposed behavioural change
- why that change should help
- possible regression risk
- eval case that would show whether the change worked
- counter-case that would show whether it over-corrected
- confidence in the proposal

The human owner decides whether to edit.

### 30. Make the smallest change capable of fixing the observed problem

Do not rewrite a whole skill because one instruction failed.

Prefer:

- clarifying a trigger
- moving an important rule earlier
- splitting an overloaded instruction
- adding a must-pass check
- narrowing an absolute rule
- adding one counter-example
- moving cross-cutting behaviour to house rules where repeated across modules

Then test.

Large rewrites make it hard to know why behaviour changed.

### 31. Test for regression after every meaningful change

At minimum, after changing a skill:

1. replay the case that failed
2. run a counter-case where the new behaviour should **not** fire
3. re-run relevant existing regression cases
4. inspect the resulting transcripts
5. run a cold real-user test when practical

Do not declare the change successful because the author can now produce one good run.

### 32. Record why a skill changed

A future reviewer should be able to trace:

> **real session -> finding -> change -> test**

For every accepted behavioural change, preserve:

- eval record
- issue or finding ID if used
- skill commit before
- skill commit after
- stated change hypothesis
- regression case

This prevents the skill from becoming a pile of unexplained instructions.

### 33. Allow evals to reveal that the method source needs work

Sometimes the agent follows the method correctly and the method still does not answer the user's real need.

Classify this as a **method gap**.

Possible responses include:

- add a complementary source
- revise the method MD
- create a new module
- move the need to another existing skill

Do not patch the `SKILL.md` with unsupported analytical advice merely because a user asked for it once.

### 34. Keep skill improvement separate from model training language

Within this repository, the main improvement mechanism is:

- change method guidance
- change skill instructions
- add or revise examples
- change shared rules
- improve routing
- add regression tests

These changes condition how the model behaves when the skills are loaded.

Unless the project later undertakes model fine-tuning or another training process, do not describe every prompt or skill revision as literal model training.

The evaluation loop is still a form of iterative agent development: real use teaches the team how the configured system should change.

---

## Eval record

Every stored real-session eval should begin with enough metadata to interpret it later.

Suggested header:

```markdown
# [Short case title]

| | |
|---|---|
| Module(s) | `problem` |
| Version tested | commit `abc1234` |
| Model | Claude [model/version] |
| Date | YYYY-MM-DD |
| Tester | [role or anonymised type] |
| Test type | cold / warm |
| House rules loaded | yes / no / unknown |
| Other skills loaded | [list / none / unknown] |
| Case type | real / anonymised real / synthetic / replay |
| Outcome | [short result] |
```

Then include:

### Context

What the user was trying to do and what they supplied.

### Transcript

The interaction needed to understand the behaviour.

### User feedback

Explicit corrections, approvals, confusion, requests, edits, abandonment, or follow-up.

### Assessment

What worked and what failed.

### Findings

Numbered findings, each classified by:

- type
- severity
- evidence
- expected behaviour
- observed behaviour
- effect on user or analysis

### Change proposals

Only where the evidence supports one.

### New eval cases

Regression, counter-case, or capability test created from the session.

### Open questions

What this session cannot tell us.

---

## Single-session review scaffold

For one conversation:

1. **Identify the tested version and environment.**
2. **Classify the run as cold or warm.**
3. **Reconstruct the user's actual goal.**
4. **Identify the skill or skills that should have governed the conversation.**
5. **Read the relevant skill's must-pass rules and method source.**
6. **Walk the transcript turn by turn.**
7. **Mark strong behaviours worth preserving.**
8. **Mark clear failures against explicit requirements.**
9. **Mark user friction or unexpected usage even where no rule was broken.**
10. **Separate agent failure from ambiguous instructions or test design.**
11. **Classify each finding.**
12. **Set severity separately from confidence and frequency.**
13. **Identify the likely failure mechanism.**
14. **Propose the smallest plausible change where warranted.**
15. **Write the regression case.**
16. **Write a counter-case if the change could over-trigger.**
17. **State what requires another real-user run.**

→ **Session verdict:** `[what worked] + [main defect or learning] + [likely source] + [change/test recommendation] + [confidence and limitation]`.

---

## Cross-session synthesis scaffold

When reviewing several sessions:

1. **Group by skill, version, model, and use-case type.**
2. **Separate cold and warm runs.**
3. **Extract findings from each session without merging them yet.**
4. **Cluster similar findings by behaviour.**
5. **Count independent sessions, not turns.**
6. **Describe the contexts in which the pattern appears.**
7. **Look for the opposite pattern or counter-examples.**
8. **Separate defects from user-preference patterns.**
9. **Identify behaviours that work reliably and need regression protection.**
10. **Identify new use cases or skill journeys.**
11. **Rank changes by severity, frequency, user effect, and confidence.**
12. **Propose changes at the narrowest correct level: skill, house rule, method, routing, or product.**
13. **Create or update capability and regression suites.**
14. **Name what further evidence is needed before making broader changes.**

A useful synthesis should answer:

> **What is the agent repeatedly getting right?**

> **What is it repeatedly getting wrong?**

> **Under what conditions?**

> **What should we change next?**

> **How will we know the change helped without breaking something else?**

---

## Change proposal format

For every proposed change:

### Finding

`[concise description of observed problem]`

### Evidence

- Sessions: `[IDs / filenames]`
- Versions: `[commits]`
- Models: `[models]`
- Cold/warm: `[mix]`
- User effect: `[what happened]`

### Diagnosis

`[skill defect / specification defect / method gap / cross-skill defect / product insight / model variance / test defect]`

### Proposed change

**Target:** `[file + section]`

**Change:** `[specific behavioural edit]`

### Why this should help

`[mechanism linking change to observed failure]`

### Regression risk

`[what useful behaviour could be weakened or over-triggered]`

### Test

**Failure replay:** `[case]`

**Counter-case:** `[case where behaviour must not over-fire]`

**Existing regressions to rerun:** `[cases]`

### Confidence

`high / medium / low` with a short reason.

Do not output a revised `SKILL.md` unless the user explicitly asks for the edit.

---

## Building the eval suite

### Start from real cases

The first cases should come from:

- real user transcripts
- manually discovered defects
- behaviours the author already checks before a skill is released
- known failure modes in the method or behaviour specification

Do not wait for hundreds of examples.

A small set of high-information cases can guide alpha development.

### Build 2 banks

**Capability bank**

Difficult or unsolved cases.

Examples:

- subtle hidden solutions
- plausible but unsupported causal claims
- stakeholder systems with conflicting internal factions
- evidence questions where another experiment is better than more desk research
- options that look different but are variants of one strategy
- trade-offs involving a hard-to-compare value
- decisions where the twenty-dollar-bill test exposes missing ownership

**Regression bank**

Cases the agent is expected to handle reliably.

Examples:

- known failures already fixed
- must-pass behaviour from each skill
- boundaries where a behaviour should not trigger
- recurring successful patterns worth protecting

### Balance trigger and non-trigger cases

For every important conditional behaviour, include both:

> **should fire**

and

> **should not fire**

This is especially important for a challenging policy-analysis agent, because an over-trained challenge reflex can become as unhelpful as an under-active one.

---

## Suggested grading model

Do not force every evaluation into one number.

Use a mixture.

### Hard checks

Binary pass/fail for explicit requirements.

Examples:

- fabricated a figure: fail
- failed to challenge a clear hidden solution: fail
- asked 4 questions when the skill explicitly requires one at a time: fail
- crossed a stated skill boundary without reason: fail

### Quality judgments

Use a short anchored scale, for example:

**0 - failed**
The behaviour is absent or materially wrong.

**1 - partial**
The right issue appears, but weakly, late, unclearly, or with meaningful errors.

**2 - pass**
The behaviour is substantively correct and useful.

**3 - strong**
The behaviour is correct, well judged for the user's context, and creates unusually good progress.

Use only dimensions that matter for the skill.

### User signal

Record separately:

- positive
- mixed
- negative
- unknown

with the actual evidence from the transcript.

### Outcome signal

Record separately:

- task completed
- useful partial progress
- stalled
- abandoned
- wrong outcome
- unknown

Do not combine these mechanically into one "quality score" during the alpha.

---

## What to look for across the whole MDEE.MD system

As the alpha grows, track themes such as:

### Challenge

- Does the agent challenge weak reasoning at the right moment?
- Does it challenge too often?
- Does it accept hidden assumptions?
- Does it mistake uncertainty for error?

### Evidence

- Does it distinguish evidence, inference, and assumption?
- Does it invent facts?
- Does it ask for evidence that could actually change the analysis?
- Does it know when further research has low value?

### Interaction

- Does it ask one useful question or turn the interaction into an interview?
- Does it stop asking when enough is known?
- Does it adapt when the user requests a direct draft?
- Does structure help or burden the user?

### Policy method

- Does each module perform its intended analytical job?
- Does a module duplicate another one?
- Are important concepts falling between skills?
- Are users naturally jumping between modules in ways the system should support?

### Outputs

- Are outputs used, edited, copied, or rejected?
- Do users repeatedly ask for a different format?
- Does the agent produce analysis when the user needs a decision artefact?
- Does it bury the key point?

### Boundaries

- Does evidence work become option generation too early?
- Do criteria quietly decide the option?
- Does stakeholder analysis turn into political strategy without enough evidence?
- Does trade-off analysis make the decision rather than expose it?

These themes can become shared eval dimensions only after repeated use shows they matter across modules.

---

## Anti-patterns

### Pitfall A - User satisfaction is the eval

**Failure:** a positive reaction is treated as proof the agent performed well.

**Challenge:** compare user signal with method fidelity and task outcome.

### Pitfall B - The spec is assumed correct

**Failure:** every deviation from `SKILL.md` is treated as model failure even when real use shows the instruction itself is poor.

**Challenge:** distinguish skill defect from specification defect.

### Pitfall C - One session becomes a universal rule

**Failure:** a personal preference or unusual case triggers a global behaviour change.

**Challenge:** ask whether this is a reproducible contract failure or a pattern requiring more evidence.

### Pitfall D - Waiting for a pattern before fixing an obvious defect

**Failure:** a serious, reproducible must-pass failure remains because it has only appeared once.

**Challenge:** severity and evidence quality matter as well as frequency.

### Pitfall E - Warm testing is treated as cold evidence

**Failure:** the author steers the model toward the expected behaviour and counts the pass as realistic user evidence.

**Challenge:** label the run and require a later cold test.

### Pitfall F - Current skill used to judge an old transcript

**Failure:** the evaluator criticises behaviour using instructions added after the session occurred.

**Challenge:** evaluate the tested version.

### Pitfall G - Only failures are preserved

**Failure:** successful behaviours disappear during later rewrites.

**Challenge:** promote important successes into regression protection.

### Pitfall H - Only trigger cases are tested

**Failure:** the skill learns to challenge, map, search, or question everything.

**Challenge:** create matched counter-cases.

### Pitfall I - Golden-answer grading

**Failure:** a sound response fails because it differs from one reference wording.

**Challenge:** grade required behaviours and outcomes.

### Pitfall J - One score hides the failure

**Failure:** an `82%` score does not reveal that the agent fabricated evidence in an otherwise good answer.

**Challenge:** keep critical checks separate.

### Pitfall K - Evaluation auto-edits the agent

**Failure:** an evaluator changes `SKILL.md` before the owner has reviewed the evidence and regression risk.

**Challenge:** propose the change and its test first.

### Pitfall L - Big rewrites destroy causal learning

**Failure:** many instructions change at once and nobody knows what fixed or broke the behaviour.

**Challenge:** prefer the smallest change that tests the hypothesis.

### Pitfall M - Transcript summaries replace transcripts

**Failure:** later reviewers cannot inspect what actually happened.

**Challenge:** preserve the source interaction alongside the summary.

### Pitfall N - Sensitive material is stored unchanged

**Failure:** real organisational or personal information enters the eval corpus unnecessarily.

**Challenge:** anonymise while preserving the analytical structure.

### Pitfall O - Synthetic tests drift away from real use

**Failure:** the suite passes while actual users keep finding new problems.

**Challenge:** continuously add real failures and sample real transcripts.

---

## Self-check rubric

Before returning an evaluation, confirm:

### Must pass

- The tested **skill version and model** are recorded where available.
- The run is labelled **cold or warm** where this can be determined.
- The user's actual goal has been reconstructed before grading.
- Observed behaviour is separated from evaluator interpretation.
- User feedback is separated from analytical quality.
- Findings are classified by likely source.
- Severity is separated from frequency.
- Important claims cite the transcript evidence that supports them.
- Proposed changes identify a concrete target and mechanism.
- Every proposed behavioural change has a **failure replay**.
- Conditional changes have a **counter-case** to detect over-correction.
- The evaluator does not automatically rewrite another skill.
- Sensitive material has been anonymised appropriately.

### Should pass

- Strengths worth protecting are identified.
- Independent sessions rather than turns are used for trend claims.
- Model differences are considered where relevant.
- Several trials are used where behaviour is variable.
- Capability and regression cases are kept distinct.
- Existing regressions are named for re-test after a change.
- The evaluator states what remains unknown.
- Product insights are separated from skill defects.
- Method gaps are sent back to the method layer rather than patched into skills without grounding.

### Process reminder

- Evals are living evidence.
- The eval suite should become more representative as real use grows.
- Every important failure should make the system easier to test next time.
- Every successful fix should leave behind a regression case.
- Every broad behavioural rule should be supported by evidence broader than one person's stylistic preference.
- The final question is always: **what should we test next to learn whether this change made the agent better?**

---

## Scope boundary

This method evaluates and improves the **MDEE.MD agent and its skills**.

It is not the method for evaluating whether a public policy itself worked after implementation.

That is a different analytical task and may later require its own policy-evaluation or experimentation method.

The `evaluation` skill should therefore be understood as the **agent improvement loop** for the alpha.

Its primary objects are:

- real conversations
- skill behaviour
- user outcomes
- recurring failure and success patterns
- proposed skill changes
- capability tests
- regression tests

---

## One-line reference

> Good agent evaluation turns real use into traceable learning: inspect what the user was trying to do and what the agent actually did, compare it with the tested skill contract, separate defects from product insights and model variance, look for patterns across independent sessions, propose the smallest evidence-backed change, and convert every meaningful fix into a regression test.

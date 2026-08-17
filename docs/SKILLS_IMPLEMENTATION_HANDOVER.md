# MDEE.MD skills implementation handover

**Status:** active implementation handover  
**Repository:** `Policy-Analysis-Tools-for-Everyone/Alpha`  
**Target branch:** current local/default branch unless the user says otherwise  
**Purpose:** take the now-settled method layer and turn it into a coherent, usable Claude Skills alpha.

> This file is temporary. Use it as the working checklist for this implementation pass. Once every task is complete, all enduring decisions have been moved into permanent repo documentation, and the final diff has been reviewed, delete this file before handback.

---

## 1. What this handover is for

The project began by recovering a useful policy-problem-framing agent and turning it into a broader set of Claude Skills for rigorous public problem solving.

The intellectual work has now moved much further than the runtime skills.

The repository currently has:

- a rich canonical method layer under `reference/`
- only 2 runtime skills under `.claude/skills/`
- documentation that still describes the older, incomplete state
- one real transcript from the earlier problem-skill test
- a new evaluation method designed to improve the agent from actual use

The job now is **implementation, consolidation and behavioural compression**.

Do not start another research phase.

Do not add new policy theory because it sounds useful.

Do not copy the method files wholesale into `SKILL.md`.

Read the method layer, decide what Claude must do differently at runtime because of it, and encode only that behaviour.

---

## 2. Product intent

MDEE.MD is a set of Claude Skills for rigorous public problem solving.

Its value is not that it writes policy documents quickly.

Its value is that it makes weak policy reasoning harder to pass unnoticed.

The agent should:

- challenge weak or solution-shaped problem framing
- distinguish evidence, inference, assumption, value judgement and unknown
- keep important competing framings visible
- construct genuine alternatives rather than a preferred option plus decoys
- make criteria and value choices explicit
- project outcomes rather than repeat intentions
- confront real trade-offs
- decide when the analysis supports a choice, when it supports a staged choice, and when it is not yet decision-ready
- preserve public value, operational feasibility and required political support as standing considerations
- turn important uncertainty into a proportionate learning move where useful
- use risk-opportunity reasoning when conventional appraisal assumptions are a poor fit
- keep the user as author and accountable decision maker
- communicate mature analysis clearly without turning every interaction into a report

The agent applies methods without touring named frameworks to the user.

Bardach remains the main analytical spine, but the product is **not a mandatory linear journey**.

Users should be able to enter wherever their actual problem is.

---

## 3. Canonical method architecture

The new method layer is the primary source for current skill authoring.

### Capability methods

These live under:

`reference/methods/capabilities/`

Current files:

- `problem-definition-guidance.md`
- `stakeholder-analysis-guidance.md`
- `evidence-guidance.md`
- `alternatives-guidance.md`
- `criteria-guidance.md`
- `outcomes-guidance.md`
- `trade-offs-guidance.md`
- `decision-guidance.md`
- `storytelling-guidance.md`
- `agent-evaluation-guidance.md`

These files explain the method in enough depth for maintainers and future revisions.

They are **not runtime prompts**.

### Shared methods

These live under:

`reference/methods/shared/`

Current files:

- `strategic-triangle-guidance.md`
- `uncertainty-and-learning-guidance.md`
- `risk-opportunity-appraisal-guidance.md`

These cut across several capabilities.

They are not extra sequential stages and should not become user-facing "step 10, 11, 12" skills.

### Writing guidance

This lives under:

`reference/writing/anti-ai-writing-style.md`

It is a shared output-quality specification.

It is not a policy-analysis method.

It should shape substantial user-facing prose without changing evidence, analysis or necessary technical terminology.

---

## 4. Ownership map

Treat these ownership boundaries as settled unless the files themselves reveal a direct contradiction.

| Analytical job | Canonical home |
|---|---|
| What is the problem? | `problem-definition-guidance.md` |
| Who matters, why, what power do they have, and how are they connected? | `stakeholder-analysis-guidance.md` |
| What do we know, how strong is it, and what evidence is worth gathering? | `evidence-guidance.md` |
| What is uncertain and what should we learn next? | `uncertainty-and-learning-guidance.md`, usually called from evidence |
| What could we do? | `alternatives-guidance.md` |
| What should outcomes be judged against? | `criteria-guidance.md` |
| What will probably happen? | `outcomes-guidance.md` |
| What appraisal approach fits the decision? | `risk-opportunity-appraisal-guidance.md` |
| What do we gain and give up? | `trade-offs-guidance.md` |
| Is the proposition worthwhile, deliverable and sufficiently supported? | `strategic-triangle-guidance.md` |
| What should we choose? | `decision-guidance.md` |
| How should mature reasoning be communicated? | `storytelling-guidance.md` |
| How is the agent itself performing and improving? | `agent-evaluation-guidance.md` |

Do not let one skill swallow the jobs owned by several others.

---

## 5. The key implementation principle

### Method completeness is not skill completeness

The method files are intentionally rich.

They contain:

- provenance
- distinctions
- source synthesis
- conceptual explanation
- examples
- anti-patterns
- scaffolds
- boundaries
- self-checks

A skill needs only the behaviour required in live use.

For each capability, extract:

1. **Trigger:** when should Claude recognise that this capability is needed?
2. **Ownership:** what analytical job does this capability own?
3. **Attention:** what should Claude notice, challenge or distinguish?
4. **Questions:** what might it need to ask?
5. **Question discipline:** when should it stop asking?
6. **Moves:** what is the smallest useful reasoning sequence?
7. **Transitions:** what must be true before moving on?
8. **Output behaviour:** what should a useful conversational result look like?
9. **Handoffs:** what kind of gap belongs to another capability?
10. **Failure modes:** what should never happen?
11. **Self-check:** what must be true before the turn is returned?

Leave the rest in the method layer.

A source insight belongs in runtime instructions only if it changes what Claude:

- asks
- notices
- challenges
- produces
- refuses to invent
- hands off
- or uses to decide that enough analysis has been done

Do not reward theoretical completeness at the cost of usable skills.

Prefer the smallest skill that preserves the intended behaviour.

---

## 6. Fixed product decisions

These decisions should not be reopened casually.

### 6.1 Non-linear entry

The method has a logical spine, but the user does not have to complete a numbered workflow.

Claude should recognise the analytical job in front of it.

Evidence may send the work back to the problem.

Outcome projection may expose a missing evidence question.

Trade-offs may expose a missing criterion.

Decision work may reveal that the option set is poor.

### 6.2 Stakeholders are a deliberate capability

Stakeholder analysis is not one of Bardach's 8 steps.

It remains a separate capability because it has a distinct job:

- actors
- motivations
- beliefs
- interests
- resources
- power
- arena
- relationships
- coalitions
- changing political conditions

### 6.3 The 3 shared methods are not stages

Strategic alignment, uncertainty and learning, and risk-opportunity appraisal are shared methods.

Use them selectively inside the relevant capabilities.

Do not create a mandatory user journey through them.

### 6.4 User authorship and accountability

The user remains the author of the work.

The authorised person or institution remains accountable for consequential public decisions.

The agent may analyse, challenge, draft and recommend.

It does not acquire public authority through confidence or fluency.

### 6.5 No fabricated evidence

Never invent:

- facts
- figures
- dates
- sources
- causal support
- probabilities
- reference classes

Mark gaps.

Say what would close them.

### 6.6 Chat first

Normal interaction is conversational.

Do not produce a full report or filed document as the routine response shape.

Structure is allowed and often useful.

If the user explicitly asks for a memo, document or other artefact, produce the requested form.

### 6.7 Frameworks stay backstage

Use the methods.

Do not give the user a tour of Bardach, the Strategic Triangle, post-normal science or other frameworks unless they explicitly ask about them.

Working vocabulary such as public value, operational capacity, political support, mechanism, constraint, evidence and assumption is fine.

### 6.8 Writing quality is shared

`reference/writing/anti-ai-writing-style.md` is canonical for substantial user-facing prose.

It should influence the runtime through a compact house-rule layer and, most strongly, storytelling.

Do not paste the entire file into every skill.

---

## 7. Desired runtime skill set

The target capability names should be non-numbered unless a verified current Claude Skills constraint makes that mechanically unwise.

Preferred skill directories:

```text
.claude/skills/
  house-rules/
  problem/
  stakeholders/
  evidence/
  options/
  criteria/
  outcomes/
  trade-offs/
  decide/
  story/
  evaluation/
```

This deliberately drops the old numeric prefixes.

It also keeps familiar product language such as `options`, `decide` and `story`, even where the canonical method filename uses `alternatives`, `decision` or `storytelling`.

If current official Anthropic documentation shows that another structure is necessary for reliable skill discovery or shared loading, verify that before deviating.

Do not retain numbering merely because the old repo used it.

If a real platform constraint would force a materially different architecture, stop and explain the constraint to the user before making that product-level change.

---

## 8. Current repo state that must be reconciled

At the time of handover:

- `.claude/skills/` still contains only `00-house-rules` and `01-problem`
- `README.md` still says only 2 modules are written
- `README.md` still says several later methods have no sources
- `docs/AUTHORING.md` still describes the old numbered, sequential module architecture
- `docs/AUTHORING.md` still says evidence through decision are blocked on missing sources
- `docs/BEHAVIOUR_SPEC.md` still points to old source paths and describes an earlier product state
- `00-house-rules/SKILL.md` still cites the old Bardach DOCX and old Strategic Triangle source path
- `01-problem/SKILL.md` still cites the old Bardach DOCX and the old source architecture
- old source material remains mixed directly under `reference/methods/`

Treat this as a migration.

Do not make the README or authoring guide look complete before the runtime skills actually exist.

---

## 9. Phase 0: read before editing

Before making substantive edits, read in this order:

1. `README.md`
2. `docs/AUTHORING.md`
3. `docs/BEHAVIOUR_SPEC.md`
4. current `.claude/skills/00-house-rules/SKILL.md`
5. current `.claude/skills/01-problem/SKILL.md`
6. all files in `reference/methods/capabilities/`
7. all files in `reference/methods/shared/`
8. `reference/writing/anti-ai-writing-style.md`
9. existing material under `evals/`
10. current repository status and diff

Then produce a short internal implementation plan and proceed.

Do not ask the user to approve routine implementation details that are already resolved by this handover.

Ask only where:

- the sources genuinely conflict
- a product-level decision is unresolved
- a destructive repository change would remove provenance that may still be needed
- current Claude Skills mechanics impose a constraint not anticipated here

---

## 10. Phase 1: finish the method layer

The method design is intentionally almost finished.

Do these remaining method-layer tasks only.

### 10.1 Problem definition

Review:

`reference/methods/capabilities/problem-definition-guidance.md`

Add only the small shared-method routing that is still missing.

The core method should remain compact.

Expected additions:

- call `uncertainty-and-learning-guidance.md` when problem, experience or mechanism uncertainty is preventing a responsible working frame
- call `strategic-triangle-guidance.md` only where public purpose, capacity or required support materially changes how the public problem should be understood

Do not add another major theory section.

### 10.2 Stakeholder analysis

Review:

`reference/methods/capabilities/stakeholder-analysis-guidance.md`

Add a compact **required support / authorising environment** check.

From the wider stakeholder ecosystem, identify the subset whose:

- authorisation
- funding
- legal permission
- operational cooperation
- legitimacy
- or non-opposition

is required for the proposition to proceed.

Point to `strategic-triangle-guidance.md` for the narrower political-feasibility question.

Do not bloat the main actor table.

The 4-column actor table remains the central artefact:

`Actor | Motivations | Beliefs | Resources`

Positions, intensity, arena, evidence status and network structure can remain overlays or separate views.

### 10.3 Consistency check across all method MDs

Check:

- filenames
- internal path references
- shared-method references
- old `bardach-*` filenames
- old numbered skill references
- inconsistent names for the same capability
- claims that the process must be linear
- stale references to missing sources

Fix mechanical inconsistency.

Do not rewrite settled methods for stylistic preference.

---

## 11. Phase 2: rationalise active references and archival sources

The new MD method layer is the canonical source for current skill authoring.

Original source material may still matter for provenance.

Keep those roles separate.

### 11.1 Strategic Triangle source replacement check

This is a required task.

Compare:

- `reference/methods/shared/strategic-triangle-guidance.md`
- `reference/methods/strategic-triangle-case-2090.pdf`

Ask:

- Does the MD faithfully preserve the source's important distinctions?
- Does it preserve the 3 dimensions?
- Does it preserve the 3 misalignment patterns?
- Does it preserve "good enough" rather than perfect alignment?
- Does it preserve alignment as constructed and unstable?
- Does it preserve the difference between public support and public value?
- Does it preserve operational feasibility as financial, legal, technical, personnel and managerial capacity?
- Does it preserve the point that the triangle is a cue to deeper analysis rather than a complete method?
- Has the MD introduced claims that the PDF does not support?

If the MD is faithful and more useful as the canonical method, make the MD canonical and remove the PDF from the active working method layer.

The project owner is comfortable with the MD replacing the PDF rather than retaining 2 competing canonical sources.

If removing the PDF would destroy provenance that is still needed by `BEHAVIOUR_SPEC.md`, either:

- update the provenance record so the MD clearly records the original source, then remove the PDF, or
- ask the user before retaining it purely as archive

Do not keep it in the active method directory simply because it was there first.

### 11.2 Old Bardach problem DOCX

The new current method is:

`reference/methods/capabilities/problem-definition-guidance.md`

The old DOCX is no longer the canonical current method.

However, it was part of the original agent's source history.

Do not silently delete historical evidence if `BEHAVIOUR_SPEC.md` still depends on it.

Preferred outcome:

- current method authoring points to the new MD
- old source material, if retained for provenance, is clearly archival rather than active
- no runtime skill has to choose between the old DOCX and the new MD

### 11.3 PPC PDF

Compare:

- `reference/methods/capabilities/storytelling-guidance.md`
- `reference/methods/ucl-ppc-one-pager-instructions.pdf`

The storytelling MD now treats PPC as one output mode rather than the whole storytelling method.

Decide whether the PDF still earns a place as original source material.

If retained, make its archival/source role unambiguous.

If the MD fully captures what current runtime authoring needs, the runtime skills should cite the MD, not depend on reading the PDF.

### 11.4 DPI material

The DPI files are domain-specific.

They should not sit in a way that makes them look like generic core policy methods.

Review the current files such as:

- `digital-public-infrastructure-and-public-value.pdf`
- `dpi-public-value-framework.md`
- `economics-of-shared-digital-infrastructures.pdf`

Preserve them if they are useful future domain material, but move or label them as domain-specific reference rather than generic core method.

Do not absorb them into the generic capability skills during this pass.

### 11.5 Original Copilot exports

Preserve the original Copilot JSON and packaging evidence unchanged.

They are historical evidence.

Do not rewrite original-source files to make the past architecture look like the current one.

---

## 12. Phase 3: settle how shared methods reach runtime skills

This is the main mechanical architecture question.

The conceptual design is fixed:

- Strategic Triangle is shared
- uncertainty and learning is shared
- risk-opportunity appraisal is shared
- they are not extra sequential stages

The current authoring guide assumes a skill must be self-sufficient because one skill may be loaded by description match.

Verify current Claude Skills behaviour using official Anthropic documentation if that is available in the environment.

Then implement the cleanest reliable mechanism.

### Preferred principle

A capability skill should contain the **minimum distilled shared behaviour it needs**, not a copy of the shared method.

For example:

- `outcomes` needs outside-view forecasting, feedback/path-dependence triggers and a rule to turn an ungrounded decision-sensitive forecast into a learning question
- it does not need the whole 6,000+ word risk-opportunity method

- `criteria` needs the appraisal gate around marginality, heterogeneity and uncertainty
- it does not need the full dynamic appraisal method

- `stakeholders` needs a required-support check
- it does not need a full Strategic Triangle tutorial

- `decide` needs a compact final value/capacity/support check, reversibility, lock-in and review conditions
- it does not need to restate every shared source

### Do not solve this by:

- creating 3 new mandatory sequential user skills
- pasting the full shared methods into every capability
- moving all shared theory into `house-rules`
- relying on a file being loaded automatically unless current Claude Skills mechanics actually guarantee that

Record the chosen mechanical rule in `docs/AUTHORING.md`.

---

## 13. Phase 4: update house rules before authoring the rest

Refactor the current `00-house-rules` into the target `house-rules`.

Preserve its strongest existing behaviour:

- user remains author and decision maker
- concise, critical rather than affirming
- one focused question at a time by default
- stop questioning once there is enough to produce useful work
- do not re-ask supplied information
- never invent facts, figures, dates or sources
- mark missing evidence
- separate facts, interpretations, assumptions, hypotheses, values and unknowns
- preserve competing framings
- challenge vague evaluative terms
- chat is the normal experience
- no routine full-report response shape
- apply the method without touring named frameworks

Revisit the current treatment of the Strategic Triangle.

The new canonical shared method is richer than the old house-rules summary.

Do not turn `house-rules` into the canonical location of the full triangle.

Keep only what truly applies across every capability.

### Writing style

Add the compact runtime subset of:

`reference/writing/anti-ai-writing-style.md`

House rules should cover the most universal output habits, such as:

- UK spelling
- short paragraphs
- direct language
- natural contractions where appropriate
- numbers as digits
- no em dash
- restrained formatting
- no generic AI filler, hype or self-congratulatory transitions
- avoid obvious AI rhetorical habits where the writing file forbids them

Do not paste the entire banned-word catalogue if a smaller runtime rule can achieve the same behaviour.

`story` should apply the writing file most strongly.

If the runtime architecture can reliably read the full writing file only when substantial prose is being drafted, use that. Otherwise distil the necessary rules into the relevant skills.

---

## 14. Phase 5: implement the capability skills

Target skill set:

- `problem`
- `stakeholders`
- `evidence`
- `options`
- `criteria`
- `outcomes`
- `trade-offs`
- `decide`
- `story`
- `evaluation`

The skill descriptions are critical.

Write each description as a **recognition rule for when the skill applies**, not as a course title.

The user should not have to say "use criteria".

Claude should recognise that the real problem is criteria selection.

### 14.1 Problem

Canonical method:

`reference/methods/capabilities/problem-definition-guidance.md`

Owns:

- core condition
- scope
- affected group/context
- magnitude and time
- public-problem basis
- hidden solutions
- causal claims
- problem hierarchy
- framing alternatives

Apply shared methods lightly.

Do not let it become a full stakeholder, evidence or appraisal skill.

Refactor the current `01-problem` rather than blindly replacing behaviour that has already been tested once.

Update its sourcing to the new canonical MD.

### 14.2 Stakeholders

Canonical method:

`reference/methods/capabilities/stakeholder-analysis-guidance.md`

Owns:

- actors
- motivations
- beliefs
- resources
- positions vs interests
- power
- arena
- relationships
- networks
- coalitions
- brokers/boundary spanners
- changing political picture

Preserve the main 4-column actor view.

Add the compact required-support check.

Do not turn every stakeholder conversation into technical social-network analysis.

### 14.3 Evidence

Canonical method:

`reference/methods/capabilities/evidence-guidance.md`

Owns:

- what the evidence is for
- data / information / evidence
- evidence / inference / assumption / value judgement / unknown
- framing effects on relevance
- alternative frames
- uncomfortable knowledge
- policy-based evidence
- source fit and applicability
- disagreement
- responsible quantification
- value of information
- stopping rules

Uses uncertainty-and-learning for critical uncertainty and active learning.

Uses risk-opportunity selectively for forecast integrity, model uncertainty and reference classes.

Do not make more research the default answer.

### 14.4 Options

Canonical method:

`reference/methods/capabilities/alternatives-guidance.md`

Runtime name: `options`.

Owns:

- alternatives as hypotheses
- iteration with problem framing
- policy variables
- feasible manipulations
- packaging manipulations into coherent strategies
- strategic thrust
- BAU
- serious variants
- genuine option distinction
- learning as an option where justified
- packages/pathways where relevant
- transition

Do not "brainstorm 3 options" mechanically.

Do not create decoys.

### 14.5 Criteria

Canonical method:

`reference/methods/capabilities/criteria-guidance.md`

Owns:

- what counts as better
- primary objective
- outcome dimensions
- objectives vs constraints vs secondary values
- efficiency
- equity/distribution
- rights
- process values
- practical criteria
- direction
- measure/proxy distinction
- visible weighting
- aggregation caution

Uses the risk-opportunity method only as an appraisal gate.

Do not score options before outcomes are projected.

### 14.6 Outcomes

Canonical method:

`reference/methods/capabilities/outcomes-guidance.md`

Owns:

- projection rather than intention
- base case
- causal pathway
- initial conditions
- direction
- magnitude
- range
- time/pace
- outside view
- reference classes
- feedbacks
- path dependence
- option interaction
- side effects
- actor response
- sensitivity
- break-even/switchpoints

If a decision-sensitive forecast cannot responsibly be made and is learnable, turn it into a learning question rather than inventing a central estimate.

### 14.7 Trade-offs

Canonical method:

`reference/methods/capabilities/trade-offs-guidance.md`

Owns:

- dominance
- outcome comparison
- magnitude
- base case
- commensurability
- non-commensurable values
- marginal reasoning
- distribution
- risk/opportunity
- systemic effects
- uncertainty
- switchpoints
- implied valuation
- central exchange

Stop before final recommendation.

### 14.8 Decide

Canonical method:

`reference/methods/capabilities/decision-guidance.md`

Runtime name: `decide`.

Owns:

- actual choice
- accountable decision maker
- decisive reason
- accepted trade-off
- diagnosing difficulty choosing
- learn now vs act now
- reversibility
- staged commitment
- final public value / capacity / support check
- twenty-dollar-bill test
- ownership/policy entrepreneur
- strongest contrary case
- dissent
- decision readiness
- decision record
- review condition

The agent may recommend.

It must not present itself as the accountable public authority.

### 14.9 Story

Canonical method:

`reference/methods/capabilities/storytelling-guidance.md`

Runtime name: `story`.

Owns:

- audience
- purpose
- Grandma Bessie test
- selection and compression of mature analysis
- evidence/projection/judgement distinction
- central trade-off
- recommendation visibility
- serious objection
- output-mode choice
- PPC memo mode
- writing-quality pass
- sending weak analysis back upstream

PPC is an output mode, not the analytical workflow.

Apply `reference/writing/anti-ai-writing-style.md` strongly here.

### 14.10 Evaluation

Canonical method:

`reference/methods/capabilities/agent-evaluation-guidance.md`

Owns evaluation of the **agent**, not public policy.

Support these modes:

1. review one session
2. synthesise several sessions
3. design capability/regression tests
4. review a proposed skill change

Preserve the core improvement loop:

`real use -> transcript -> session review -> finding -> pattern -> change hypothesis -> skill revision -> regression test -> cold re-test -> new evidence`

Do not auto-edit a skill because one transcript looked bad.

Classify the finding first.

---

## 15. Skill authoring contract

Update `docs/AUTHORING.md` so it reflects the new architecture before treating it as authoritative.

The following principles should survive.

### Frontmatter

Each skill needs:

- `name`
- a strong `description` that controls discovery
- status if still useful in the current Claude Skills format

Do not keep old names solely for numeric ordering.

### Sourcing

Every skill should point primarily to its **canonical method MD**.

The method MD already carries its own source provenance.

Do not make every runtime skill re-list every paper and PDF unless a claim bypasses the canonical method layer.

Keep a clear line between:

- canonical method
- recovered original-agent behaviour
- project-owner product decisions
- behavioural evidence from testing

### Body

The old 5-part pattern remains useful if it still produces clear skills:

1. what this capability is for / when it applies
2. moves with transition conditions
3. what strong output looks like
4. self-check
5. failure modes

Do not preserve the format mechanically if a particular skill genuinely needs a slightly different shape.

### Transition conditions

Every multi-move skill needs a stopping or transition rule.

This prevents a skill from marching through a syllabus.

### Conversational output

The skill should produce useful work in chat.

Do not require every turn to end with a document-shaped artefact.

### Size

Prefer lean runtime skills.

Roughly 1,000-2,500 words is a useful pressure, not a hard limit.

Behavioural completeness beats arbitrary length.

A 5,000-word skill should have a strong reason to exist.

---

## 16. Skill routing and handoffs

Skills should recognise adjacent gaps without turning the user's conversation into framework navigation.

Do not tell the user:

> Now invoke the evidence skill.

Instead, continue naturally:

> The choice currently turns on whether uptake would actually change. We do not have enough evidence for that yet.

Then move into the appropriate analytical job if the runtime supports it.

Descriptions should help Claude route correctly.

Useful adjacent boundaries:

- problem -> evidence when the frame depends on an untested factual or causal claim
- stakeholders -> strategic support question when a proposal depends on a specific authoriser/funder/enabler
- evidence -> uncertainty/learning when a critical unknown can be reduced
- options -> criteria when the serious choice set is ready
- criteria -> outcomes when the standards are clear enough to project against
- outcomes -> evidence/learning when a decision-sensitive projection is ungrounded
- outcomes -> trade-offs when projections are good enough
- trade-offs -> criteria when the real disagreement is a missing or hidden value
- trade-offs -> decide when the exchange is explicit
- decide -> options/evidence/learning when the case is not decision-ready
- story -> any upstream skill when the narrative exposes unfinished reasoning

Do not force this sequence when the user entered elsewhere.

---

## 17. Phase 6: update permanent repository documentation

Once the skills are implemented, update the permanent docs.

### 17.1 README

The current README is stale.

Update it to explain:

- what MDEE.MD is now
- current skill set
- non-linear entry
- the role of house rules
- the difference between capability methods and shared methods
- the writing layer
- current status honestly
- install/use instructions using the new non-numbered skill directories
- evaluation and feedback loop
- provenance at an appropriate level

Do not say the skills are "tested" simply because they were authored.

Distinguish:

- written
- structurally checked
- behaviourally tested on real work
- regression-tested

### 17.2 AUTHORING.md

This should become the lasting builder contract.

It must no longer claim that evidence through decision have no method sources.

Document:

- method layer vs skill layer
- capability vs shared method
- writing guidance
- non-linear routing
- canonical method sourcing
- shared-method compression
- skill description importance
- transition conditions
- real-use testing
- eval workflow
- naming convention

### 17.3 BEHAVIOUR_SPEC.md

Preserve its historical function.

Part A is recovered original-agent behaviour.

Do not rewrite history so the original Copilot agent appears to have had capabilities that were added later.

Update:

- stale paths
- notes about which material is now canonical
- the current product architecture where necessary
- any old statements that falsely describe the present repo state

Keep clear separation between:

- recovered behaviour
- product extension
- current runtime implementation

If enduring current-architecture material does not belong cleanly in README or AUTHORING, a small dedicated architecture section/file is acceptable.

Do not create extra documentation merely to avoid editing the existing docs.

---

## 18. Phase 7: evaluation scaffolding

Use:

`reference/methods/capabilities/agent-evaluation-guidance.md`

as the method.

The suggested evaluation structure is:

```text
evals/
  transcripts/
  capability/
  regression/
  syntheses/
```

Git does not preserve empty folders, so create only what has content or add a small explanatory README where useful.

### Preserve real transcripts

Real user sessions belong in:

`evals/transcripts/`

Keep the existing problem transcript.

Do not rewrite a real transcript to make the new skill look better.

Anonymise sensitive material.

Label substituted figures.

### Create a minimal alpha eval pack

Do not attempt a 500-case eval suite before real use.

For each new skill, create only a small initial capability set where useful:

- 1 clear positive trigger
- 1 adjacent/non-trigger case
- 1 known failure-mode case where that adds value

Focus especially on:

- hidden solutions
- evidence vs assumption
- policy-based evidence
- fake options
- premature scoring
- intention vs outcome
- false precision
- value conflicts mistaken for evidence gaps
- refusal to decide despite adequate analysis
- overconfident decision
- storytelling that manufactures missing analysis
- agent evaluation that auto-rewrites based on one anecdote

Synthetic cases belong in `capability/` or `regression/`.

Do not store synthetic conversations as if they were real behavioural evidence.

### Do not overclaim testing

Same-session self-tests are useful for:

- structure
- obvious routing
- missing rules
- formatting

They are weak evidence of behaviour.

Mark them as such.

Real cold sessions should drive the next major revision.

---

## 19. Phase 8: repository consistency and mechanical checks

Before declaring the implementation complete, search the repo for stale architecture.

Check for:

- `.claude/skills/00-house-rules`
- `.claude/skills/01-problem`
- other numeric skill names
- `bardach-problem-definition-guidance.docx` as a current canonical source
- "no source" claims for evidence/options/criteria/outcomes/trade-offs/decision
- "Two of eleven modules"
- claims that modules must be completed in order
- stale paths to the old Strategic Triangle PDF
- stale PPC path dependencies
- `bardach-*` current-method filenames
- broken relative links
- duplicated shared-method theory
- method files copied wholesale into skills
- references to shared methods as mandatory stages

Check YAML/frontmatter validity for all skills.

Check that every skill description describes **when to use it**.

Check that every multi-move skill has transition or stopping conditions.

Check that runtime prose follows the house rules.

---

## 20. Things not to build in this pass

Do not turn this into a larger software project.

Do not build:

- a web app
- persistent case memory
- a database
- an API
- a UI
- automatic telemetry
- a plugin system
- a complex orchestration layer
- a large synthetic benchmark
- a new teaching syllabus
- a DPI-specific policy pack

The target is a strong **skills-only alpha** with a canonical method layer and an evaluation loop.

---

## 21. Things not to redesign without evidence

Do not reopen these because another framework seems interesting:

- Bardach as the main analytical spine
- stakeholder analysis as a separate extra capability
- Strategic Triangle as shared
- uncertainty/learning as shared
- risk-opportunity appraisal as shared
- user authorship
- critical rather than affirming posture
- evidence discipline
- non-linear entry
- storytelling as downstream of analysis
- evaluation as meta-level agent improvement

If real use later shows one of these is wrong, the evaluation loop can change it.

This implementation pass should not pre-empt that evidence.

---

## 22. Decision rules for ambiguity

### Resolve yourself when:

- it is a naming/detail choice consistent with this architecture
- it is a mechanical path correction
- it is a wording improvement that preserves method meaning
- it is a leaner way to encode an already-settled behaviour
- it is an obvious stale-doc correction

### Ask the user when:

- 2 source-grounded methods genuinely conflict
- a change would alter what a capability owns
- a current Claude platform constraint would force a different product architecture
- a destructive cleanup would remove provenance you cannot safely preserve another way
- the choice is normative rather than mechanical
- you would otherwise need to invent missing method guidance

Do not ask permission for every edit.

Do not silently settle real analytical or product choices.

---

## 23. Definition of done

This implementation pass is complete when all of the following are true.

### Method layer

- [ ] `problem-definition-guidance.md` has the light shared-method routing
- [ ] `stakeholder-analysis-guidance.md` has the compact required-support check
- [ ] method file references are consistent
- [ ] no current canonical method depends on an old `bardach-*` filename
- [ ] Strategic Triangle MD has been compared with the source PDF and canonical status resolved
- [ ] old/source/domain material is clearly separated from current generic method guidance

### Runtime skills

- [ ] `house-rules`
- [ ] `problem`
- [ ] `stakeholders`
- [ ] `evidence`
- [ ] `options`
- [ ] `criteria`
- [ ] `outcomes`
- [ ] `trade-offs`
- [ ] `decide`
- [ ] `story`
- [ ] `evaluation`

For every skill:

- [ ] description says when the skill applies
- [ ] canonical method source is named
- [ ] runtime instructions are compressed rather than copied
- [ ] shared-method behaviour is included only where needed
- [ ] moves have stopping/transition logic
- [ ] self-check exists
- [ ] failure modes exist
- [ ] no facts or evidence can be invented
- [ ] no framework tour leaks into normal user output
- [ ] no mandatory linear journey is imposed

### Writing

- [ ] anti-AI writing guidance is represented in the runtime at the right level
- [ ] house rules contain the universal subset
- [ ] story applies the stronger writing pass
- [ ] technical accuracy and source terminology take precedence over style cleanup

### Documentation

- [ ] README reflects the actual current product
- [ ] AUTHORING reflects the new canonical method/skill architecture
- [ ] BEHAVIOUR_SPEC preserves history while correcting stale paths/current-state notes
- [ ] no permanent doc says later capabilities have no sources
- [ ] no permanent doc claims behavioural testing that has not happened

### Evaluation

- [ ] existing real transcript is preserved
- [ ] evaluation directory structure is explained
- [ ] a small alpha capability/regression set exists where useful
- [ ] synthetic tests are not presented as real-user evidence

### Final review

- [ ] stale numeric skill paths are gone unless a verified platform constraint required them
- [ ] broken links are fixed
- [ ] repo-wide search finds no misleading old status text
- [ ] git diff has been reviewed for accidental source deletion
- [ ] no UI/API/product expansion has slipped into scope
- [ ] remaining risks and untested behaviour are stated plainly

---

## 24. Final handback

At the end of the implementation:

1. review the complete diff
2. run the mechanical checks
3. state what was changed
4. state what was deliberately left unchanged
5. state what is still untested
6. recommend the first 3-5 real-use sessions that would give the highest-value behavioural evidence
7. make sure enduring decisions from this file now live in README, AUTHORING or BEHAVIOUR_SPEC
8. delete `docs/SKILLS_IMPLEMENTATION_HANDOVER.md`
9. do **not** push changes unless the user explicitly asks

The final response to the user should be concise and should include:

- completed work
- important architectural choices made
- any question that had to remain unresolved
- files they should inspect first
- what to test next

Do not claim the alpha is validated until real cold use supports that claim.

---

## 25. Short version of the job

Read the new canonical method layer.

Finish the 2 small method gaps.

Resolve active source/reference duplication.

Refactor house rules.

Convert each capability into a lean, self-contained runtime skill with the necessary distilled shared-method behaviour.

Remove numeric sequencing from the user-facing skill architecture unless current platform mechanics require it.

Update stale documentation.

Add minimal eval scaffolding.

Review the diff.

Move lasting decisions into permanent docs.

Delete this handover.

Then give the project back for real use and evaluation.

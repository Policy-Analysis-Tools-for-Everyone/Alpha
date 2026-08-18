# The method layer

The canonical methods. Everything in `skills/` is written against these
files, and every runtime skill names the one it is grounded in.

These are **not runtime prompts.** They are deliberately rich: provenance,
distinctions, worked examples, anti-patterns, scaffolds, self-check rubrics and
boundary statements. A skill needs only the behaviour that changes what the agent
does in a live conversation, which is a small fraction of what is here. Method
completeness is not skill completeness. See `docs/AUTHORING.md` for how the
compression is supposed to work.

Read these when revising a skill, when a real session exposes a method gap, or
when you need to know what a skill is claiming and on whose authority.

## `capabilities/`: one analytical job each

| File | Owns | Runtime skill |
|---|---|---|
| `capabilities/problem-definition-guidance.md` | What is the problem? | `problem` |
| `capabilities/stakeholder-analysis-guidance.md` | Who matters, why, with what power, and how are they connected? | `stakeholders` |
| `capabilities/evidence-guidance.md` | What do we know, how strong is it, and what is worth finding out? | `evidence` |
| `capabilities/alternatives-guidance.md` | What could we do? | `options` |
| `capabilities/criteria-guidance.md` | What counts as better? | `criteria` |
| `capabilities/outcomes-guidance.md` | What would probably happen? | `outcomes` |
| `capabilities/trade-offs-guidance.md` | What do we gain and give up? | `trade-offs` |
| `capabilities/decision-guidance.md` | What should we choose? | `decide` |
| `capabilities/storytelling-guidance.md` | How should mature reasoning be communicated? | `story` |
| `capabilities/agent-evaluation-guidance.md` | How is this agent performing, and how should it change? | `evaluation` |

The runtime names differ from the filenames in 3 places (`options`, `decide`,
`story`) because the product language and the source language differ.
Both are kept rather than forcing one to match the other.

**The capabilities are not a sequence.** They have a logical order, and Bardach's
method supplies most of it, but a user arrives wherever their problem actually
is. Evidence work can send the analysis back to the problem. Trade-offs can
expose a missing criterion. Each file's "Canonical boundaries" section says what
belongs to it and what belongs elsewhere; that is a division of labour, not a
running order.

Stakeholder analysis is not one of Bardach's steps. It is here as a separate
capability because it has a distinct job, and folding it into the political
support question would lose most of that job.

## `shared/`: methods several capabilities call

| File | What it contributes |
|---|---|
| `shared/strategic-triangle-guidance.md` | Is the proposition worthwhile, deliverable and supported enough? |
| `shared/uncertainty-and-learning-guidance.md` | What is uncertain, and what is the lightest credible way to learn it? |
| `shared/risk-opportunity-appraisal-guidance.md` | What appraisal approach fits this decision, and how should forecasts be challenged? |

**These are not extra stages and never become user-facing steps.** A capability
calls the part of a shared method it needs, at the point where it needs it. Each
shared file's "Canonical boundaries" section says which capability calls it for
what.

The runtime consequence: a capability skill carries the distilled shared
behaviour it actually needs and nothing else. `outcomes` needs the outside view
and a rule for turning an ungrounded decision-sensitive forecast into a learning
question. It does not need the rest of the appraisal method.

## `../writing/anti-ai-writing-style.md`

The shared output-quality specification for substantial user-facing prose. Not a
policy-analysis method. It shapes writing without changing evidence, analysis or
necessary technical terminology. `house-rules` carries the universal subset;
`story` applies it hardest.

## `../sources/`, `../domain/`, `../copilot-json/`

Archive. Original source documents, domain-specific material and the original
Copilot exports. See the README in each. No runtime skill reads them.

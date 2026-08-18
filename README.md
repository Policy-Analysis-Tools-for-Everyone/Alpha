# MDEE.MD

A set of [Claude Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills)
for rigorous public problem solving.

Most tools help you write policy analysis faster. These are built to make it
harder to write bad analysis. The agent challenges weak framing, refuses to invent
figures, separates evidence from assumption, keeps competing framings visible
instead of quietly picking one, and asks one substantive question at a time rather
than producing a plausible document on request.

**Alpha.** All 11 skills are written. One has been tested on real work, once. See
[Status](#status) before relying on this.

---

## Install

### Claude Code

```bash
git clone <this-repo-url> mdee-agent
cd mdee-agent
claude
```

The skills live in `.claude/skills/`, so Claude Code picks them up for this
project with no build step. Describe your actual problem and the matching skill
loads. To use them across all your projects:

```bash
cp -r .claude/skills/* ~/.claude/skills/
```

### claude.ai and Claude Desktop

Upload each `.claude/skills/<name>/` directory as its own skill under
**Settings → Capabilities → Skills**. Upload `house-rules` and then whichever
capabilities you want; `house-rules` is the one that should always be present.

### Anthropic API

Each skill is a `SKILL.md` with spec-compliant frontmatter, so they work through
the Skills API. If you assemble several into one system prompt, put `house-rules`
first.

---

## How it works

**`house-rules` always applies.** Tone, question discipline, evidence rules, how
competing framings are handled, how the agent writes, and the three standing
considerations below. Everything else assumes it is in play.

**Ten capabilities, each owning one analytical job.** You do not have to work
through them in order, and you should not have to name one. Describe the problem
you actually have and the right one should load.

| Skill | The question it owns |
|---|---|
| `problem` | What is the problem? |
| `stakeholders` | Who matters, why, with what power, and how are they connected? |
| `evidence` | What do we know, how strong is it, and what is worth finding out? |
| `options` | What could we do? |
| `criteria` | What counts as better? |
| `outcomes` | What would probably happen? |
| `trade-offs` | What do we gain and give up? |
| `decide` | What should we choose? |
| `story` | How should this be communicated? |
| `evaluation` | How is this agent performing, and how should it change? |

**Entry is not linear.** There is a logical spine, and most of it is Bardach's,
but the work moves both ways. Evidence sends you back to the problem. Trade-offs
expose a missing criterion. Deciding reveals the option set was poor. Each skill
knows which gaps belong to its neighbours and continues into them rather than
announcing a handoff.

**Stakeholder analysis is a deliberate addition,** not one of Bardach's steps. It
is separate because folding it into the political-support question loses the
people who are badly affected and hold no power.

**Three considerations cut across the capabilities** rather than being stages of
their own:

- **Public value.** Does this promise a benefit worth having, to someone other
  than the people proposing it?
- **Operational capacity.** Can it realistically be delivered?
- **Political support.** Do the people whose backing it needs actually endorse
  it, and believe it can be delivered?

They are explained once in `house-rules` and applied by each capability at its own
point. The aim is never to score three corners. It is to name what the current
choice *costs*, because sharpening public value routinely narrows what can be
delivered, and the reverse.

**One deliberate omission.** The agent never names a framework to you. It applies
the method rather than touring it. The working vocabulary, public value,
operational capacity, mechanism, constraint, evidence, assumption, is used
directly.

---

## What sits behind the skills

Three layers, deliberately separate.

**The method layer**, `reference/methods/`, is canonical. Ten capability methods
and 3 shared methods, written in enough depth for maintainers: provenance,
distinctions, worked examples, anti-patterns, scaffolds and self-check rubrics.
Every skill names the method file it is grounded in. See
[`reference/methods/README.md`](reference/methods/README.md).

**Shared methods are not extra steps.** Strategic alignment, uncertainty and
learning, and risk-opportunity appraisal cut across several capabilities. A skill
carries the distilled part it actually needs and calls nothing at runtime.
`outcomes` needs the outside view and a rule for turning an ungrounded forecast
into a learning question; it does not need the rest of the appraisal method.

**The writing layer**, `reference/writing/anti-ai-writing-style.md`, is the shared
output-quality specification for substantial prose. `house-rules` carries the
universal subset; `story` applies it hardest. It shapes writing without changing
evidence, analysis or necessary technical terms.

**The archive**, `reference/sources/`, `reference/domain/` and
`reference/copilot-json/`, holds original source documents, domain-specific
material and the original Copilot exports. Provenance, not current method. No
skill reads it.

---

## Status

Written is not tested. Four states worth keeping apart:

- **Written.** The skill exists and says what it should do.
- **Structurally checked.** Frontmatter validates, links resolve, no
  contradictions found by reading.
- **Behaviourally tested.** Run on real work in a session that was saved.
- **Regression-tested.** A saved case re-runs and still passes after changes.

| Skill | Written | Structurally checked | Behaviourally tested |
|---|---|---|---|
| `house-rules` | yes | yes | **no** |
| `problem` | yes | yes | once, warm, on the previous version |
| `stakeholders` | yes | yes | **no** |
| `evidence` | yes | yes | **no** |
| `options` | yes | yes | **no** |
| `criteria` | yes | yes | **no** |
| `outcomes` | yes | yes | **no** |
| `trade-offs` | yes | yes | **no** |
| `decide` | yes | yes | **no** |
| `story` | yes | yes | **no** |
| `evaluation` | yes | yes | **no** |

**Nothing here has been tested cold**, by someone who did not write it. The single
real session, `evals/transcripts/problem/receipt-confirmation.md`, was run warm by
the author against an earlier version of `problem`, and without `house-rules`,
which did not exist yet. It found 4 defects, which were fixed. Two of them had not
been predicted, and 4 of 5 predictions made beforehand were wrong.

The method layer is settled. The runtime is not validated.

Every capability method has a source. That was not true earlier in this project
and the older documentation said so; it is out of date, not the current state.

---

## Evaluation and feedback

`evals/` holds the improvement loop: real transcripts, a synthetic capability pack
and regression cases traceable to real fixes. `evals/README.md` explains what each
directory is for and how to save a session.

The most useful thing you can send is a conversation where the agent was
**confidently wrong.** Those are worth more than the ones where it worked, and
they are the easier ones to lose. Open an issue with the exchange, what you
expected and what you got. Redact anything sensitive; the analytical shape is what
matters, not your real figures.

`evals/transcripts/problem/receipt-confirmation.md` is the worked example of the
format, including how far the anonymisation goes.

---

## Provenance

Every skill carries a sourcing header naming its canonical method and what it is
**not** grounded in. A skill with an empty "not grounded" line is either very well
sourced or not being honest.

| Key | Source |
|---|---|
| `[B]` | Bardach, *A Practical Guide for Policy Analysis*, the main analytical spine |
| `[T]` | Donahue, "Strategic Alignment for Policy Analysis and Design", HKS Case 2090.0 |
| `[J]` | The original Microsoft 365 Copilot agent this work recovers, kept as a raw archive |
| `[O]` | Material the project owner authored directly |
| `[E]` | Behavioural evidence from saved sessions |

The capability methods carry their own fuller citations, including Weimer and
Vining, Fisher and Ury, May, Saltelli and Giampietro, Rodrik, McGuinness and
Slaughter, Flyvbjerg, Funtowicz and Ravetz, Kattel and colleagues, and Sharpe and
colleagues.

[`docs/BEHAVIOUR_SPEC.md`](docs/BEHAVIOUR_SPEC.md) records what the original
Copilot agent observably did, and which behaviour here is recovered from it rather
than added later. That separation is maintained deliberately: the original stopped
at the problem statement, so nothing downstream of it can claim recovered
provenance.

`reference/domain/dpi/` holds a synthesis of 2 UCL IIPP papers on digital public
infrastructure. It is domain material rather than generic method, and only one
thing from it reaches the runtime: `house-rules` records a live disagreement it
deliberately does not settle, whether market failure is the right primary test for
public action, or whether the better question is what direction is embedded in a
framing and who chose it.

---

## Building on this

[`docs/AUTHORING.md`](docs/AUTHORING.md) is the contract: how the method layer and
the skill layer differ, how to compress one into the other, frontmatter that works
on every surface, why descriptions matter more than anything else in the file, and
the loop that turns real use into a revision.

The two rules most often broken are *no document-shaped replies* and *do not
restate the house rules*.

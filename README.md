# MDEE.MD

A set of [Claude Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills)
for rigorous public problem solving.

Most tools help you write policy analysis faster. These are built to make
it harder to write bad analysis: the agent challenges weak framing,
refuses to invent figures, separates evidence from assumption, keeps
competing framings visible instead of quietly picking one, and asks one
substantive question at a time rather than producing a plausible document
on request.

**Public beta.** Two of eleven modules are written. See
[Status](#status) before relying on this for real work.

---

## Install

### Claude Code

Clone the repository and open it:

```bash
git clone <this-repo-url> mdee-agent
cd mdee-agent
claude
```

The skills live in `.claude/skills/`, so Claude Code picks them up for
this project with no build step. Ask it something like *"help me frame
this problem"* and it will load the matching module.

To use the skills across **all** your projects rather than just this one,
copy them into your personal skills directory:

```bash
cp -r .claude/skills/* ~/.claude/skills/
```

### Claude.ai and Claude Desktop

Skills are uploaded as folders under **Settings → Capabilities → Skills**.
Upload each `.claude/skills/<module>/` directory as its own skill.

Start with `00-house-rules` and `01-problem` — the others aren't written
yet.

### Anthropic API

The skills are plain `SKILL.md` files with YAML frontmatter, so they work
with the Skills API or as system-prompt content. If you assemble several
into one prompt, concatenate them in directory order and put
`00-house-rules` first.

---

## How it works

**`00-house-rules` always applies.** It holds what's true in every
conversation regardless of which method is in play: tone, question
discipline, evidence rules, how competing framings are handled, and the
three lenses below. Load it first, always.

**Everything else is a step**, in order — though the agent is meant to
recognise which one you actually need rather than march through them.

**Three lenses cut across every step**, rather than being steps of their
own:

- **Public value** — does this promise a benefit worth having, to
  someone other than the people proposing it?
- **Operational capacity** — can it realistically be delivered?
- **Political support** — do the people whose backing it needs actually
  endorse it?

They're explained once in `00-house-rules` and applied by each module at
its own step. The point isn't to score three corners; it's to name what
your current choice *costs* — sharpening public value often narrows what's
deliverable, and the reverse.

**One deliberate omission.** The agent never names a framework to you. It
applies the method; it doesn't tour it.

---

## Status

Honest state of each module. "No source" means the underlying method text
isn't in this repository yet, and writing the module without it would mean
inventing plausible policy-textbook content — the specific failure this
project exists to avoid.

| Module | What it does | Status |
|---|---|---|
| `00-house-rules` | Shared rules and the three lenses | **Written.** Not yet tested as a whole |
| `01-problem` | Define the problem: condition not fix, who's affected, scale, hidden solutions, causal claims | **Written**, tested once — see `evals/transcripts/` |
| `02-stakeholders` | Who holds the problem, who must back a response, who is affected differently | Not written |
| `03-evidence` | Assemble and judge evidence; separate fact from assumption | Not written — no source |
| `04-options` | Construct genuine alternatives, not a preferred one plus decoys | Not written — no source |
| `05-criteria` | Choose the criteria the options will be judged against | Not written — no source |
| `06-outcomes` | Project what each option would actually produce | Not written — no source |
| `07-trade-offs` | Confront what each choice costs | Not written — no source |
| `08-decide` | Decide — including "not yet, and here's what would settle it" | Not written — no source |
| `09-story` | Tell the story so it survives contact with a reader | Not written — source present, not yet used |
| `10-evaluation` | Gather feedback on the agent's own use | Not written |

Modules 03–08 are blocked on the method text for Bardach's steps 2–7.
Module 09 has its source (`reference/methods/ucl-ppc-one-pager-instructions.pdf`)
and is unblocked.

---

## Feedback

This is a beta and the most useful thing you can send is a conversation
where the agent was **confidently wrong** — those are worth more than the
ones where it worked, and they're the easier ones to lose.

Open an issue with the exchange, what you expected, and what you got.
Redact anything sensitive; the analytical shape is what matters, not your
actual figures.

`evals/transcripts/01-problem/receipt-confirmation.md` is a worked example
of the format, including how it was anonymised.

---

## Provenance

Every module carries a sourcing header naming what it's grounded in and —
more importantly — what it isn't. A module with an empty "not grounded"
line is either very well sourced or not being honest.

| Key | Source |
|---|---|
| `[B]` | Bardach, *A Practical Guide for Policy Analysis*, problem-definition guidance |
| `[T]` | Donahue, "Strategic Alignment for Policy Analysis and Design", HKS Case 2090.0 |
| `[J]` | The original Microsoft 365 Copilot agent this work recovers — raw export, kept as an archive |
| `[O]` | Material the project owner authored directly |
| `[E]` | Behavioural evidence from saved test sessions |

Source documents are in `reference/`. `docs/BEHAVIOUR_SPEC.md` records
what the original Copilot agent observably did, and which behaviour here
is recovered from it versus newly added.

Also in `reference/methods/`: a synthesis of two UCL IIPP papers on
digital public infrastructure and public value, which informs the
public-value stance in `00-house-rules`. That module records a live
disagreement it deliberately does not settle — whether market failure is
the right primary test for public action, or whether the better question
is what direction is embedded in a framing and who chose it.

---

## Authoring a new module

`docs/AUTHORING.md` is the contract: frontmatter shape, the sourcing
convention, the five-part body template, and the constraints that hold
the library together. Read it before writing a module — the two rules
most often broken are *no document-shaped replies* and *don't restate
the house rules*.

The loop that produced module 01, which is the only one with evidence
behind it: draft it, use it on a real problem you actually have, save the
conversation, revise. Most of the value is in the revision.

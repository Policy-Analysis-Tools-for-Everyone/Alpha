# Authoring a method skill

**Status: draft.** Revised as modules get written, which is the point.
Anything here that turns out to be wrong in practice should be changed,
not worked around.

This guide covers how to write one method module, so that eleven
separately-authored modules read as one agent rather than eleven
documents.

---

## 1. The library

Ten sequential modules plus a separate evaluation skill. Modules `01`–`09`
are the method itself, in order; `00` holds everything shared.

| Module | Method | Status |
|---|---|---|
| `00-house-rules` | Shared rules — tone, evidence discipline, entry, the three lenses | Written, untested as a whole |
| `01-problem` | Bardach 1 | Written, tested once (see `evals/transcripts/`) |
| `02-stakeholders` | Not a Bardach step — separated out deliberately | Not written |
| `03-evidence` | Bardach 2 | Not written — no source (§6) |
| `04-options` | Bardach 3 | Not written — no source (§6) |
| `05-criteria` | Bardach 4 | Not written — no source (§6) |
| `06-outcomes` | Bardach 5 | Not written — no source (§6) |
| `07-trade-offs` | Bardach 6 | Not written — no source (§6) |
| `08-decide` | Bardach 7 | Not written — no source (§6) |
| `09-story` | Bardach 8 | Not written — source present (§6) |
| `10-evaluation` | Not a method step — gathers feedback on the agent's own use | Not written |

They live in `.claude/skills/<nn>-<name>/SKILL.md`, so cloning the
repository gives a working agent with no build step.

**Three things cut across every module rather than being modules of
their own:** Bardach's method (which *is* the `01`–`09` spine, not a
separate thing to load), the three lenses of public value / operational
capacity / political support, and the public-value material derived from
the IIPP papers in `reference/methods/`.

Cross-cutting has a specific mechanical meaning here. Claude Code loads
**one** skill by description match, so a separate cross-cutting skill
would not reliably load alongside a method module. Therefore:
`00-house-rules` explains each lens **once**, and every method module
**applies** them at its own step without re-teaching them. Module 01's
move 6 is the worked example.

The cost of that arrangement, worth watching: `00-house-rules` grows, and
every module carries lens-application moves. If house rules starts
reading as a dumping ground, that is the signal to revisit.

**A skill name may begin with a digit.** Verified in practice — modules
prefixed `01`, `09` and `10` all registered and were invoked correctly by
name in Claude Code. Ordering by directory name works.

**Suggested order to write the rest:** `09-story` is unblocked (its
source is present). `02-stakeholders` and `10-evaluation` need scoping
before they need sources. `03`–`08` wait on the method text for
Bardach's steps 2–7.

---

## 2. The loop, per skill

1. **Gather the source.** If there is none, stop and get some — see §6.
2. **Draft `SKILL.md`** using the prompt in §5.
3. **Use it on real work.** Not a test case; an actual problem you have.
4. **Save the conversation.** This is the project's only behavioural
   evidence — see §7.
5. **Revise.** Most of the value is here, not in the first draft.
6. **Re-test cold**, with `00-house-rules` loaded and ideally by someone
   who did not write the module. Authoring and testing in the same
   session catches structural faults but not much else — the module's
   author already knows what the file says.
7. **Mark it done** against §8.

---

## 3. The module template

### Frontmatter

```yaml
---
name: 01-problem
description: >
  Defining and testing a policy problem — what the condition is, who is
  affected, at what scale, and whether a solution has been smuggled in.
status: draft
---
```

`description` is what Claude Code matches on to decide the skill is
relevant, so write it as *when this method applies*, not as a title. It
is the single most important line in the file: a module that never
triggers is a module that does not exist.

### Sourcing header

Immediately after the frontmatter, an HTML comment recording what this
module is grounded in, using the source keys from
[BEHAVIOUR_SPEC.md](./BEHAVIOUR_SPEC.md):

```html
<!--
Grounded in:
  [B] reference/methods/bardach-problem-definition-guidance.docx
  [J] reference/copilot-json/declarativeAgent_0.json (instructions)
Not grounded: <anything asserted without a source, and why>
-->
```

The "not grounded" line matters more than the rest. A module with an
empty one is either very well sourced or not being honest.

### Body

Five parts, in this order:

1. **What this method is for, and when it applies.** Short. Written as
   recognition, not permission — the user does not announce which method
   they want.
2. **The moves.** Numbered, each with an explicit *move on when…*
   condition. These conditions are what stop the sequence becoming a
   march, and their absence is a named failure mode (BEHAVIOUR_SPEC A4,
   A14).
3. **What a strong output looks like.** Concrete enough to test against.
4. **Self-check.** Must-pass and should-pass, in the shape of A7.
5. **Failure modes.** What going wrong looks like, so it is recognisable.

---

## 4. Constraints every module must satisfy

Non-negotiable, because they hold the library together:

1. **No document-shaped replies.** Never `## Headings` and a report as a
   routine answer. The four-part output — candidate, critique, revision,
   readout — is the right *content*; a Markdown document is the wrong
   *shape*. Markdown formats a message; it does not turn one into a
   filed document. (CLAUDE.md; BEHAVIOUR_SPEC B1.)

   **This bans a report, not structure.** The original instructions
   label and bold the four output parts, so labelled parts, short lists
   and bold labels are faithful and often necessary. Burying the four
   parts in continuous prose to avoid looking like a document is the
   same failure from the other side, and it is the one module 01 hit
   first (see its revision note). Structure the reply; do not file it.
2. **Do not restate the house rules.** Tone, evidence discipline,
   competing framings, the vague-term challenge and the three lenses
   live in `00` only. Eleven copies drift; one does not. Modules
   *apply* the lenses at their own step; they do not re-explain what
   the lenses are.
3. **Never name the method or framework in output — but use its
   vocabulary freely.** No "using Bardach's third step", no explaining
   the method instead of applying it: one coherent way of working, not a
   tour of named frameworks. The ban is on the names and the tour.
   *Public value*, *operational capacity*, *political support*,
   *deficit*, *excess*, *mechanism*, *symptom* and *constraint* are the
   working vocabulary and plain English besides — use them directly and
   without hedging. Reading this constraint as a ban on the terms
   produces evasive answers, which is what happened on module 01's first
   test.
4. **Every move carries a transition condition.**
5. **`SKILL.md` must be self-sufficient.** Assume nothing else in the
   repository is loaded alongside it except `00-house-rules`. A
   `references/` subdirectory is not a place to put content the module
   needs.
6. **UK spelling**, concise, critical rather than affirming.
7. **Never invent facts, figures, dates or sources.** Marked placeholders
   and a statement of what would close the gap.

---

## 5. The authoring prompt

Reusable per module. Fill in the angle brackets.

```text
I am authoring one method module for MDEE.MD, an agent for
rigorous public problem solving. I want the module written to a contract,
not written freely.

Read first, in this order:
- docs/AUTHORING.md — the contract this module must satisfy
- docs/BEHAVIOUR_SPEC.md — recovered behaviour vs added behaviour, and
  the sourcing convention
- .claude/skills/00-house-rules/SKILL.md — the shared rules this module
  must NOT restate, and the three lenses it must apply without
  re-explaining
- <source material for this method>

Write .claude/skills/<nn>-<name>/SKILL.md for: <method>.

Rules:
- Ground every instruction in the attached source material. Where you
  cannot ground something, do not invent method guidance — leave a
  marked TODO naming the source needed. Plausible policy-textbook
  content written from general model knowledge is the specific failure
  this project exists to avoid, and it is hard to spot afterwards
  because it reads well.
- Follow the module template in the authoring guide exactly: frontmatter,
  sourcing header, what the method is for, the moves each with a
  "move on when" condition, what a strong output looks like, the
  self-check, the failure modes.
- Satisfy every constraint in §4 of the authoring guide. The
  no-documents rule and the do-not-restate-the-house-rules rule are the
  two most often broken.
- Write the module as instructions to an agent, not as an essay about a
  method.

Ask me one question at a time about anything the sources leave genuinely
ambiguous. Do not resolve ambiguity by choosing silently — tell me the
choice and let me make it.
```

The last instruction is deliberate. Silently collapsing a genuine choice
is the behaviour the agent itself is built to avoid; it should not be how
the agent is built.

---

## 6. What to attach, per module

The honest position: **two modules are written, and six of the nine
remaining have no method source in this repository at all.**

| Module | Attach | State |
|---|---|---|
| `00-house-rules` | `declarativeAgent_0.json`, `BEHAVIOUR_SPEC.md` (A3, A5, A10–A13, B1, B8), `strategic-triangle-case-2090.pdf` (A12), `dpi-public-value-framework.md` | Grounded — written |
| `01-problem` | `bardach-problem-definition-guidance.docx`, `declarativeAgent_0.json`, `BEHAVIOUR_SPEC.md` (A4–A11, A14) | Best evidenced in the project — written and tested once |
| `02-stakeholders` | *scope it first* | **No source, and no agreed scope.** Overlaps "who is affected" in `01` and the political-support lens in `00`. Settle what it uniquely owns before looking for a source |
| `03-evidence` | *you supply* | **No source** — needs Bardach step 2 |
| `04-options` | *you supply* | **No source** — needs Bardach step 3 |
| `05-criteria` | *you supply* | **No source** — needs Bardach step 4 |
| `06-outcomes` | *you supply* | **No source** — needs Bardach step 5 |
| `07-trade-offs` | *you supply* | **No source** — needs Bardach step 6. Note the overlap with `00`'s "name the trade-off" instruction; this module is the dedicated step, `00` is the standing habit |
| `08-decide` | *you supply* | **No source** — needs Bardach step 7. Should carry "not yet, and here's what would settle it" as a legitimate outcome |
| `09-story` | `ucl-ppc-one-pager-instructions.pdf` | **Unblocked** — source present, not yet used. See below |
| `10-evaluation` | *no method source needed* | Gathers feedback on the agent's own use. Its source is this project's own practice — `evals/transcripts/` and §7 below |

### On the Copilot exports specifically

`declarativeAgent_0.json` is primary evidence, and worth attaching for
`00` and `01`. Two cautions:

- **Do not attach it for modules 03–09.** The original agent stopped at
  the problem statement and the three-lens readout (BEHAVIOUR_SPEC A15).
  It has nothing to say about alternatives, criteria or outcomes, and
  attaching it there invites a module that *sounds* grounded in the
  original when it is not.
- **`BEHAVIOUR_SPEC.md` is usually the better working document.** It has
  already done the analysis — what is evidenced, what is inferred, what
  is product extension, and where the sources pull against each other.
  Use the raw JSON for the original's *voice and exact phrasing*; use the
  spec for what the behaviour actually was. And note the `instructions`
  field is truncated mid-sentence; do not complete it.

`manifest.json` is packaging metadata. Little authoring value.

### On module 09

The UCL one-pager instructions ground *memo structure*. Module 09 shapes
and outlines the story; decide deliberately whether it also drafts the
finished memo, because that is a real scope question and the source
alone does not settle it.

### Practical note

The Bardach guidance and the PDFs are binary. Uploading them in claude.ai
works directly. In Claude Code, convert to text first, or work from the
extracted passages — do **not** edit anything under `reference/`, which
is preserved unchanged.

---

## 7. Saving conversations

Every usable session is evidence, and the project started with none: the
Copilot exports preserve the original agent's *configuration*, not one
line of its behaviour. These transcripts are the first record of what
this agent actually says.

Save into `evals/transcripts/<module>/<name>.md`, with a header naming
the module, the version tested and the model used. The same format
carries beta-tester submissions, so keep it plain — and anonymise before
committing, as `01-problem/receipt-confirmation.md` does. Substituted
figures must be labelled as substituted, or they get cited as real
eighteen months later.

Worth saving deliberately: the conversation that made you change the
module, and the one where it was confidently wrong. The second is more
useful and easier to lose.

---

## 8. Definition of done, per module

- [ ] Grounded, with the sourcing header filled in — including the
      *not grounded* line
- [ ] Every move has a transition condition
- [ ] All seven constraints in §4 satisfied
- [ ] Used on a real problem, not a test case
- [ ] At least one conversation saved
- [ ] Tested cold, by someone who did not author it
- [ ] Nothing restated that belongs to the house rules
- [ ] The three lenses applied at this module's own step, not
      re-explained

---

## 9. Choosing a model

Three different jobs, and they do not want the same model.

**Authoring — the strongest model available.** Writing a module means
reading dense source material, separating what it supports from what it
does not, and resisting the pull toward plausible filler. That is the
work that most rewards capability. Use Opus.

**Testing — whatever the product will actually run on.** This is the one
people get wrong. The agent's value is challenge quality: noticing a
hidden solution, refusing a vague claim, keeping two framings open. That
is exactly the judgement that varies most between models. A method
validated only on the strongest model has a cost floor you have not
measured. So test on the model you intend to ship, and if that is
undecided, test the same saved conversation on more than one and see
whether the challenge survives.

**Mechanical checking — the cheapest thing that works.** Counting
questions per reply, spotting framework name-drops, flagging digits that
did not come from the user: regex, no model at all. If transcript
screening later needs judgement, Haiku is the right size for it.

**These skills pin no model.** Anyone installing them runs whatever model
they already use, which is the correct default for a skills library — it
has no API key and no bill of its own. The consequence is that challenge
quality varies with the reader's model and this repository cannot control
that. Testing across models matters more here than it would for a hosted
product, and transcripts should always record the model used.

Pricing, limits and available models change. Check current details rather
than trusting this page.

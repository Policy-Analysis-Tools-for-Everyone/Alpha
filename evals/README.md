# Evaluation

Evidence about what this agent actually does, as opposed to what its skills say it should do.
Method: `reference/methods/capabilities/agent-evaluation-guidance.md`. The runtime skill that
applies it is `evaluation`.

```text
evals/
  sessions/    all evidence, flat. Kind is a field in each file, not a directory
  wiki/        findings.md and prompts/ — the distillate that drives changes
  tests/       capability and regression cases. Synthetic
  testers.md   pseudonymous register of who ran which session
```

**[`wiki/findings.md`](wiki/findings.md) is the one to read first.** It holds what more than
one session shows, and the honest count of what the corpus does not have. Everything in
`sessions/` is a source for it.

The loop: real use → session → finding → pattern → change hypothesis → skill revision →
regression test → cold re-test.

## Current state

**17 sessions, 4 testers, August 2026, all on plugin `0.1.1`.** `0.1.2` changed
`house-rules` and `problem` from these findings and has no sessions behind it yet. Nine are transcripts; the rest are a tester's
cross-session report and a tester's note. Seven of the ten capabilities have been exercised.
Everything in `tests/` is synthetic and labelled as such.

**No session is confirmed cold** — T004 may be the exception and has not been asked — and
**nothing tests whether the agent accepts sound work**, since every session so far offered it
something to challenge. Those are the two largest gaps. See
[`wiki/prompts/cold-session.md`](wiki/prompts/cold-session.md) and
[`wiki/prompts/sound-work.md`](wiki/prompts/sound-work.md).

## Four kinds of evidence, and what each is worth

Every file in `sessions/` names its kind in the header. They are not equivalent.

**Transcript.** What the agent actually said. The only behavioural evidence.

**Debrief.** The agent's own account of a session, produced by the `evaluation` skill. A model
grading itself. **Never cite one where a transcript exists.** Its value is the invocation log:
the chat surface does not show whether a skill loaded, and a debrief lists the file reads. Two
findings in the wiki exist only because of that.

**Synthesis.** One author's cross-session review, at one date. May rest on sessions this
repository does not hold — it says so at the top when it does. Change proposals in a synthesis
stay proposals; recording one is not adopting it.

**Note.** A tester's own words, no transcript. Weaker than a transcript and not nothing: it
reports what the tester noticed, which is the only route to behaviour nobody thought to look
for. Never cite a note for what the agent said, and cite the session as uncommitted.

## Conventions, so no file restates them

**Figures are substituted.** Every case number in every file is an invented illustration,
re-derived as a set so the relationships an argument depends on still hold. Never cite one as
evidence of anything. A file that substitutes something unusually, or deliberately leaves
something unsubstituted, says so.

**Substitutions are made inside quotations too.** Quotes are otherwise verbatim: wording,
structure, emphasis and the user's original typos. Nothing is tidied. Where a quote could not
survive substitution intact it is paraphrased in square brackets, never silently altered.

**Organisations are substituted consistently across files.** Whether two sessions concern the
same real organisation is not recorded.

**Headers carry the metadata a reader needs**: kind, skills used, version, model, date, tester,
cold or warm, what else was loaded. A field nobody can confirm says so rather than carrying a
plausible value.

**Never rewrite a session.** If a skill changed afterwards, add an editorial note and leave the
record alone.

## Adding a session

Write it up, then re-mine [`wiki/findings.md`](wiki/findings.md) against it. Three questions.

**Does it add a sighting to a finding that already exists?** Add the row. A fourth sighting
matters less than the first, but the count is the argument.

**Does it contradict one?** The valuable case. Record the contradiction rather than smoothing
it — `F5` exists because two sessions disagreed.

**Does it leave something with nowhere to go?** That is a prompt, and it goes in
`wiki/prompts/`.

Then update the mined-on date in `findings.md`, add or update the row in `testers.md`, and
delete any prompt the session has answered or killed.

**What a session needs before it can be written up:** date, model, plugin version, whether the
tester had read the skill files or used policymemo.ai before, and consent to publish.

## Cold testing, and what must never reach the agent

A session is **cold** when the tester has not read the skill files, has not seen what the evals
expect, and has not used policymemo.ai before. Their second session is not cold, whatever else is true.

**Nothing about a tester reaches policymemo.ai.** The register and any future learning record are
evaluation-side artefacts. They go nowhere near a Project, a skill, a system prompt or Claude's
memory. Break that and every later result measures a personalised build rather than the product
a new person installs.

**Runtime memory is a separate question.** Never give an evaluation file the name of a file a
runtime feature loads, and never use auto memory as an evidence source.

## Privacy

1. **Pseudonymous IDs in the repository.** The mapping to real people is held privately by the
   maintainer and never committed.
2. **Ask before the session:** *"May I save an anonymised version of this conversation in a
   public repository?"* Record the answer in `testers.md`.
3. **Where consent is refused,** or the work is pre-decision, commercially sensitive or
   politically sensitive, write the finding and do not commit the session.
4. **Redact before committing, never after.**
5. **Register fields stay broad categories.** No free text about a person.

## Counting

**n testers / m sessions.** Never a percentage, never "most users". A behaviour seen 4 times in
one person's sessions is *1 tester (4 sessions)*. That is the whole defence against inventing
significance from a tiny alpha sample.

## `tests/`

**Capability cases** are hard, realistic and possibly unsolved. A meaningful failure rate is the
point. **Regression cases** protect behaviour already shown to work and should pass almost every
time. Promote a case when a capability failure is fixed and becomes reliable.

Never report one aggregate score across both. For any behaviour that fires conditionally, keep a
matched pair: a case where it must fire and one where it must not. An agent tested only on
whether it challenges learns to challenge everything.

## Do not overclaim

| State | What it means |
|---|---|
| **Written** | The skill exists and says what it should do |
| **Structurally checked** | Frontmatter valid, links resolve, no contradictions found by reading |
| **Behaviourally tested** | Run on real work, in a session that was saved |
| **Regression-tested** | A saved case re-runs and still passes after changes |

A same-session self-test catches structure, not behaviour, because the author already knows what
the file says. Label it warm and expect a cold run to find different things.

## Reporting a problem

The most useful thing anyone can send is a conversation where the agent was **confidently
wrong**. Worth more than the ones where it worked, and much easier to lose.

**If something went wrong,** open a session report:
[new issue](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/issues/new?template=session-report.yml).
Issues are public — redact first, or send it to the maintainer privately.

**If you are an alpha tester,** you write nothing up. Five questions, about three minutes:

1. What were you trying to do?
2. Where did you get to?
3. What surprised or frustrated you?
4. What did you expect instead?
5. Was there anything it told you that you think was wrong?

Question 2 asks for the state reached rather than whether you were happy. Question 5 earns its
place because someone who was confidently misled does not know it yet.

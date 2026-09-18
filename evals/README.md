# Evaluation

Evidence about what this agent actually does, as opposed to what its skills say it should do.
Method: `reference/methods/capabilities/agent-evaluation-guidance.md`. The runtime skill that
applies it is `evaluation`.

```text
evals/
  transcripts/   real sessions, anonymised. The only behavioural evidence
  wiki/          what recurs across sessions, and the tests it asks for
  debriefs/      agent-written accounts of sessions. Not transcripts
  capability/    hard cases the agent may still fail. Synthetic
  regression/    behaviour already shown to work, or already fixed
  testers.md     pseudonymous register of who ran which session
```

Each directory has its own README. **[`wiki/findings.md`](wiki/findings.md) is the one to read
first** — it holds what more than one session shows, and the honest count of what the corpus
does not have.

The loop: real use → transcript → finding → pattern → change hypothesis → skill revision →
regression test → cold re-test.

## Current state

**9 sessions, 2 testers, August 2026. Every one warm.** `problem` 4, `story` 3, `evidence` 2.
Four more capabilities have fired inside other people's sessions without having one of their
own. `options` and `trade-offs` have never appeared in a header. Everything under
`capability/` and `regression/` is synthetic and labelled as such.

**Nothing has been tested cold.** Neither tester. See
[`wiki/prompts/cold-session.md`](wiki/prompts/cold-session.md).

`syntheses/` does not exist. `wiki/findings.md` does the job for now.

## Cold testing, and what must never reach the agent

A session is **cold** when the tester has not read the skill files, has not seen what the evals
expect, and has not used MDEE before. Their second session is not cold, whatever else is true.

**Nothing about a tester reaches MDEE.** The register and any future learning record are
evaluation-side artefacts. They go nowhere near a Project, a skill, a system prompt or Claude's
memory. Break that and every later result measures a personalised build rather than the product
a new person installs.

**Runtime memory is a separate question.** Never give an evaluation file the name of a file a
runtime feature loads, and never use auto memory as an evidence source: notes the model wrote
about its own corrections are not a transcript.

## Privacy

1. **Pseudonymous IDs in the repository.** The mapping to real people is held privately by the
   maintainer and never committed.
2. **Ask before the session:** *"May I save an anonymised version of this conversation in a
   public repository?"* Record the answer in `testers.md`.
3. **Where consent is refused,** or the work is pre-decision, commercially sensitive or
   politically sensitive, write the finding and do not commit the transcript.
4. **Redact before committing, never after.**
5. **Register fields stay broad categories.** No free text about a person.

## Counting

**n testers / m sessions.** Never a percentage, never "most users". A behaviour seen 4 times in
one person's sessions is *1 tester (4 sessions)*. That is the whole defence against inventing
significance from a tiny alpha sample.

## `capability/` and `regression/` are different jobs

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

Question 2 asks for the state reached rather than whether you were happy; satisfaction is not
the eval. Question 5 earns its place because someone who was confidently misled does not know it
yet.

The maintainer anonymises, writes the header and runs the analysis. Testers are not expected to
become evaluation researchers.

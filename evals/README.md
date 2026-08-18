# Evaluation

Evidence about what this agent actually does, as opposed to what its skills say
it should do. The method is
`reference/methods/capabilities/agent-evaluation-guidance.md`, and the runtime
skill that applies it is `evaluation`.

The loop it serves:

> real use, transcript, session review, finding, pattern, change hypothesis,
> skill revision, regression test, cold re-test, new evidence

## What is in here, and what is not

```text
evals/
  transcripts/   real sessions, anonymised. The only behavioural evidence
  capability/    hard cases the agent may still fail. Synthetic
  regression/    behaviour already shown to work, or already fixed
```

`syntheses/` will hold cross-session reviews once there are several sessions to
review. It does not exist yet, and creating an empty directory to look organised
would misrepresent how much evidence this project has.

**The honest current state: 1 real session, on 1 capability, run warm, without
`house-rules` loaded because it did not exist yet.** Everything else here is
synthetic and labelled as such. Nothing in this repository has been
behaviourally tested cold.

## `transcripts/` is the valuable directory

Real sessions are the only record of what the agent says. The Copilot exports
under `reference/copilot-json/` preserve the original agent's configuration and
not one line of its behaviour, which is exactly the gap these files fill.

Save into `transcripts/<skill>/<short-name>.md` with a header naming the skills
used, the version or commit tested, the model, the date, the tester, whether the
run was cold or warm, and which other skills were loaded. Without the model and
the version, a transcript cannot be interpreted later: these skills pin no model,
so challenge quality varies with whatever the reader is running.

**Anonymise before committing, and label every substitution.** Remove personal
data. Replace organisation and programme names where necessary. Substitute
sensitive figures and say clearly that they are substituted, because an
unlabelled substituted number gets cited as real 18 months later. Then check that
the causal, organisational and analytical structure survives: a case anonymised
into genericness can no longer reproduce the behaviour it was saved for.
`transcripts/problem/receipt-confirmation.md` is the worked example of the format
and of how far the anonymisation can go.

**Never rewrite a transcript to make a skill look better.** If a skill has
changed since a session, say so in an editorial note and leave the record alone.

Two sessions are worth saving above all others: the one that made you change a
skill, and the one where the agent was confidently wrong. The second is more
useful and much easier to lose.

## `capability/` and `regression/` are different jobs

**Capability cases** are hard, realistic and possibly unsolved. A meaningful
failure rate is the point. They tell you what the agent still cannot do.

**Regression cases** protect behaviour already shown to work. They should pass
almost every time. When a capability failure is fixed and becomes reliable,
promote the case here.

Never report one aggregate score across both. And for any behaviour that fires
conditionally, keep a matched pair: a case where it must fire, and a case where it
must not. An agent tested only on whether it challenges learns to challenge
everything, which for this agent is as unhelpful as challenging nothing.

## Do not overclaim testing

Four distinct states, worth keeping apart in every status claim:

| State | What it means |
|---|---|
| **Written** | The skill exists and says what it should do |
| **Structurally checked** | Frontmatter valid, links resolve, no contradictions found by reading |
| **Behaviourally tested** | Run on real work, in a session that was saved |
| **Regression-tested** | A saved case re-runs and still passes after changes |

A same-session self-test catches structure, obvious routing errors, missing rules
and formatting. It is weak evidence about behaviour, because the author already
knows what the file says. Label it as warm and expect a cold run to find
different things.

Cold sessions, run by someone who did not author the skill, should drive the next
major revision.

## Reporting a problem

The most useful thing to send is a conversation where the agent was confidently
wrong. Open an issue with the exchange, what you expected and what you got.
Redact anything sensitive; the analytical shape is what matters, not the real
figures.

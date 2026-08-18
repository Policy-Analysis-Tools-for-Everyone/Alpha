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
  testers.md     pseudonymous register of who ran which session
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

## Who ran the session

`testers.md` holds a pseudonymous register: T001, T002, one row each. Every
transcript header names the tester by ID.

It exists so that *how many independent people* is answerable. The method requires
it and warns against counting one person's repeated objections as several users.
Read it during synthesis, to count independent testers. Never read it instead of a
transcript.

Report findings as **n testers / m sessions**. Never a percentage at this sample
size. A behaviour seen 4 times in one person's sessions is *1 tester (4 sessions)*.

## Cold testing, and what must never reach the agent

**Nothing about a tester reaches MDEE.** The register, and any future learning
record, are evaluation-side artefacts. They live in this repository and go nowhere
near a Project, a skill, a system prompt or Claude's memory.

Break that and every subsequent result measures a personalised build rather than
the product a new person installs.

A session is **cold** when the tester has not read the skill files, has not seen
what the evals expect, and has not used MDEE before. Their second session is no
longer cold, whatever else is true, which is why the register counts sessions.

Someone installing MDEE.MD from the plugin has no path to `evals/` at all, so the
boundary holds without anyone having to remember it. Do not helpfully undo that by
pasting evaluation material into a Project.

**Runtime memory is a separate question.** Claude's own memory feature, including
its `MEMORY.md` entrypoint, is runtime personalisation that loads into a
conversation. Everything here is evidence about behaviour. Never give an
evaluation file the name of a file a runtime feature loads, and never use auto
memory as an evidence source: notes the model wrote about its own corrections are
not a transcript. Whether retained user context improves repeated work is a
product experiment with its own hypothesis and its own eval, and it is not a
follow-on from this.

## Privacy

Proportionate to a small open-source alpha. Five rules.

1. **Pseudonymous IDs in the repository.** The mapping to real people is held
   privately by the maintainer and never committed.
2. **Ask before the session:** *"May I save an anonymised version of this
   conversation in a public repository?"* Record the answer in `testers.md`.
3. **Where consent is refused,** or the work is pre-decision, commercially
   sensitive or politically sensitive, write the finding and do not commit the
   transcript. Cite it as an uncommitted session.
4. **Redact before committing, never after.** The anonymisation rules above cover
   how far to go.
5. **Register fields stay broad categories.** No free text about a person.

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

The most useful thing anyone can send is a conversation where the agent was
**confidently wrong**. Those are worth more than the ones where it worked, and
they are much easier to lose.

**If you installed MDEE.MD and something went wrong,** open a session report:
[new issue](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/issues/new?template=session-report.yml).
Redact anything sensitive before you paste it. GitHub issues are public, so
material that has not been through that check should go to the maintainer
privately instead.

**If you are one of the alpha testers,** you do not write anything up. The
debrief is 5 questions and takes about 3 minutes:

1. What were you trying to do?
2. Where did you get to?
3. What surprised or frustrated you?
4. What did you expect instead?
5. Was there anything it told you that you think was wrong?

Question 2 asks for the state reached rather than whether you were happy, because
satisfaction is not the eval and the two get recorded separately. Question 5 earns
its place because someone who was confidently misled does not know it yet, and no
other question will surface it.

The maintainer anonymises the conversation, writes the transcript header, and runs
the structured analysis through the `evaluation` skill. Testers are not expected
to become evaluation researchers.

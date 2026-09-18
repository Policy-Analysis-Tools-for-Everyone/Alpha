# Debriefs

Agent-written accounts of sessions, produced by the `evaluation` skill at the end of
a session and returned by the tester.

## Why these are not in `transcripts/`

`../README.md` is explicit that real sessions are the only record of what the agent
says, and warns against notes the model wrote about its own behaviour being treated
as a transcript. A debrief is the agent assessing its own work, including a section
where it grades itself. That is a different evidence class and it belongs in a
different directory.

**Never cite a debrief where a transcript exists.** Where both exist for the same
session, the transcript is the record and the debrief is corroboration.

## What they are good for

Two things the transcripts in this repository cannot supply.

**Skill and tool invocation, in order, with file paths.** Every transcript here
infers whether `house-rules` loaded from behaviour, because the chat surface does not
show it. The debriefs list the actual `view` calls. That is how
`transcripts/story/story-3-non-trigger.md` can state that no MDEE skill loaded at all,
and how `transcripts/story/story-2.md` can state that `house-rules` loaded after the
first artefact was already written.

**The tester's own five answers**, recorded verbatim under Part 2, which is the
debrief format `../README.md` specifies.

## What they are not good for

Anything the agent says about its own performance is self-report. It is useful as a
pointer to where to look in the transcript, and it is not evidence on its own.

Each debrief also carries its own visibility caveat, stating what was no longer in
context when it was written. Read that first. One of the three was written with web
results, memory contents and parts of two skill files no longer visible, so its Part 1
is partly reconstruction.

## Provenance

All three were produced by the `evaluation` skill, which means these files are more
directly evidence about `evaluation` than about the sessions they describe. That skill's
`metadata: status` reads "written, not behaviourally tested". These are the first
behavioural evidence it has.

## Anonymisation

T002 anonymised these before sending them. A second pass was applied here for
consistency with the transcripts, substituting place, country and organisation names
that the original retained, and replacing figures. Substitutions are listed at the foot
of each file. Where T002's own bracketed labels existed, they were kept, so a debrief
and its transcript use the same labels for the same things.

# Transcripts

Real sessions, anonymised. The only behavioural evidence in this repository.

Filed `<skill>/<short-name>.md`. The skill is the capability that fired, not the one the user
asked for. `story/story-3-non-trigger.md` is filed under the capability that *should* have
fired and did not.

What recurs across sessions lives in [`../wiki/findings.md`](../wiki/findings.md), not here.
A transcript records one session.

## Conventions, so each file does not restate them

**Figures are substituted.** Every case number in every file is an invented illustration,
re-derived as a set so the relationships an argument depends on still hold. Never cite one as
evidence of anything. Where a file substitutes something *unusually* — or deliberately leaves
something unsubstituted, such as an agent's external citations — it says so.

**Substitutions are made inside quotations too.** Quotes are otherwise verbatim: wording,
structure, emphasis and the user's original typos. Nothing is tidied. Where a quote could not
survive substitution intact it is paraphrased in square brackets, never silently altered.

**Organisations are substituted consistently across files.** The same fictional authority
appears in several. Whether those sessions concern the same real organisation is not recorded.

**Every session here is warm**, and every one is on work the tester actually held. That is
weaker than a cold run in one direction and stronger in another: the tester can judge whether a
challenge was *right*, which a cold tester on a borrowed case cannot. Three of the defects on
record were caught only that way.

**Headers carry the metadata `../README.md` requires**: skills used, version, model, date,
tester, cold or warm, what else was loaded. A field that is not known says so rather than
carrying a plausible value.

## Never rewrite one

If a skill changed after a session, add an editorial note and leave the record alone. The
transcript is what happened.

## Adding a session

Write the transcript, then re-mine `../wiki/findings.md` against it. Three questions.

**Does it add a sighting to a finding that already exists?** Add the row. A fourth sighting
matters less than the first, but the count is the argument.

**Does it contradict one?** The valuable case. Record the contradiction rather than smoothing
it — `F5` exists because two sessions disagreed.

**Does it leave something with nowhere to go?** A behaviour seen twice that nobody has tried to
break, a defect with a mechanism and no case. That is a prompt, and it goes in
`../wiki/prompts/`.

Then update the mined-on date in `findings.md`, add or update the row in `../testers.md`, and
check whether any existing prompt is now answered or dead. A dead prompt gets deleted.

**What a new session needs before it can be written up:** date, model, plugin version, whether
the tester had read the skill files or used MDEE before, and consent to publish. A field nobody
can confirm says so — it never carries a plausible-looking value.

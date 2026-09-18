# Does a persona instruction route away from the skill?

**Status:** one observation, a plausible cause, no test.

## What it would settle

F8. Why `story` did not fire on a task its own description covers.

## Evidence in hand

`story-3-non-trigger` opens *"Assume you are [a senior adviser] to [the head of the civil
service]"* and then asks for an edit. Nothing from MDEE loaded.

`problem-3`, same tester days apart, opens *"Did I define the problem well?"* and loaded two
skills.

## What is missing

The same memo-editing task, phrased twice: once as a persona instruction, once as a task
description. Run both cold, do not name the skill.

## What would make it fail

Changing anything else between the two. Same memo, same audience, same request — only the
opening clause differs.

If it replicates, the fix is probably in `story`'s description rather than in routing.

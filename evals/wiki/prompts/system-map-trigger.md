# The problem system map has never fired

**Status:** fixed in `0.1.2`, untested. Was 2 testers / 3 sessions, zero firings.

## What it would settle

Whether the map can be made to fire on an observable condition rather than a judgement call.

## Evidence in hand

`t002-problem-3`, and both of T003's `problem` runs. Two candidate cores named explicitly in each,
which is the material the map exists for, and no map in any of them.

It has already been patched once, after `t001-problem-receipt-confirmation` recorded it firing "late and
vaguely". The patch moved it; it did not make it fire.

## What was done

The map moved out of move 9 and onto the hierarchy standing instruction — which does fire, in
all four `problem` runs — as *if you say hierarchy, draw it*, with the single-level
counter-case stated in the same breath. That is a smaller change than the proposed trigger and
attaches to something already known to work.

## What is missing

Both `problem` transcripts replayed against `0.1.2`, and **C19** in
`../../tests/capability-alpha-pack.md`, which is the counter-case below, written up.
T003's original proposal, if the simpler fix does not take: produce the map if two candidate cores have been named, **or**
if three or more of problem, mechanism, symptom and constraint have been labelled. Both
existing `problem` transcripts meet both conditions, so the replay is free.

## What would make it fail

**C-3**, the mandatory counter-case: a genuinely single-level problem must not receive a map. A
trigger that fires on everything is worse than one that fires on nothing, because the map stops
meaning anything.

Testing it only on the transcripts that prompted it. Two sessions that already meet the
condition cannot show whether the condition is too loose.

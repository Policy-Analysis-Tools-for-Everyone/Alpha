# Run it against a constraint and see what it drops

**Status:** proposed by the tester who hit the problem. Nothing in the corpus tests it.

## What it would settle

F13. Whether the agent can prioritise, or only accumulate.

## Evidence in hand

T004: *"the analysis became quite comprehensive as we went along"*, with the question raised
unprompted — how it prioritises and knows when to stop.

T003 Scen 1: the deliverable was produced in turn 1 and asked for again in turn 4. Their
reading is that length, not labelling, did the damage.

Seventeen sessions, and **not one was run against a real constraint.** Every tester had as many
turns and as much reading time as they wanted, so nothing has ever forced the agent to choose.

## What is missing

T004's test, more or less as they proposed it: a strict time constraint stated up front, and a
look at what the agent decides is actually essential to investigate.

Worth two variants. A hard deadline — an hour before a meeting — and a hard length limit, since
they fail differently: a deadline tests sequencing, a length limit tests selection.

## What would make it fail

Treating brevity as the pass condition. The agent dropping the contaminated-measure warning to
save space is a worse outcome than a long answer. The test is whether it drops the *right*
things and says what it dropped.

Using a task with an obvious priority. If one thing is plainly the crux, sequencing it proves
nothing.

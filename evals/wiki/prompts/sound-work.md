# Counter-cases: does it accept sound work?

**Status:** the second-largest gap, and now overdue. Seventeen sessions, none a test of this —
and `0.1.2` has already shipped a change this was supposed to gate.

## What it would settle

Whether the agent can tell good work from bad, or only challenges.

## Evidence in hand

None, and that is the point. All six of T003's scenarios were adversarial by design. The nine
earlier sessions were live work that had real defects in it, so a challenge was always
available. **Nothing in the corpus shows the agent being handed something sound.**

`../../tests/capability-alpha-pack.md` already names the risk: an agent tested only on whether it
challenges learns to challenge everything, which for this agent is as unhelpful as challenging
nothing.

## What is missing

The cases are written up in `../../tests/capability-alpha-pack.md` Part 3 as **C17** (useful
background) and **C18** (sound work). T003's own labels for them, C-9 and C-8, collide with
other cases in that pack and should not be used. Still unwritten:

- A stakeholder case where the obvious explanation is the right one.
- A draft whose success measure is sound. F3 is the most reliable behaviour in the record, so
  this is the test of whether it over-fires.

C17 gates the F1 change, which has already shipped. `house-rules` already records that the framework ban, read too
broadly, produced evasive answers on the first recorded test. The same failure is available
here and would be worse than the defect.

## What would make it fail

Writing a case that is sound but boring. A challenge has to be genuinely tempting and
genuinely wrong, or the agent passes by having nothing to say.

Grading on whether it stayed quiet. The pass condition is accepting what holds *and* still
naming what does not — not silence.

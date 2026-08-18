# Original source material: archive

**These files are not the current method.** They are the original documents the
method layer was built from, kept for provenance.

The current canonical methods live in `reference/methods/capabilities/` and
`reference/methods/shared/`. Those Markdown files carry their own source
citations and are what the runtime skills are written against. Nothing in
`.claude/skills/` should depend on reading anything in this directory.

Two reasons this separation exists. A skill that could be grounded in either a
distilled method or its original source has two canonical answers, which is one
too many. And these are binary formats: a `.docx` and two PDFs cannot be read
without conversion, so a skill citing them would be citing something the runtime
usually cannot open.

| File | What it is | Now distilled into | Status |
|---|---|---|---|
| `bardach-problem-definition-guidance.docx` | Eugene Bardach, *A Practical Guide for Policy Analysis*, "Step One: Define the Problem", as supplied to the original Copilot agent as its knowledge file. Derived from the edition marked "Version 4", not the 6th edition | `reference/methods/capabilities/problem-definition-guidance.md` | Superseded as current method. Retained as the original agent's knowledge file and as evidence for `docs/BEHAVIOUR_SPEC.md` source key `[B]` |
| `strategic-triangle-case-2090.pdf` | John D. Donahue, "Strategic Alignment for Policy Analysis and Design", Harvard Kennedy School Case Program, Case 2090.0 (2017). 4 pages | `reference/methods/shared/strategic-triangle-guidance.md` | Superseded as current method. See the fidelity check below |
| `ucl-ppc-one-pager-instructions.pdf` | UCL Personal Policy Problem memo instructions, adapted from Policy Design and Delivery at HKS. The 8-section memo format and its page conventions | `reference/methods/capabilities/storytelling-guidance.md`, PPC memo mode | Superseded as current method. Retained because the format is a contract with an external convention, and the MD paraphrases rather than reproduces it |

## Strategic Triangle: fidelity check against the source

The shared method MD was compared against all 4 pages of the source PDF during
the skills implementation pass. The MD is faithful and is now canonical.

Preserved from the source:

- the 3 dimensions, in Donahue's own terms: net public value; operational
  feasibility, with financial, legal, technical, personnel and managerial
  resources named explicitly; political feasibility, defined as required
  stakeholders endorsing the purposes **and** believing in operational
  feasibility
- all 3 caveats: perfect alignment is rare so "good enough" is the realistic
  ambition; alignment is constructed through cognition and action rather than
  discovered; alignment is characteristically unstable, so assume it is fragile
  and stay poised for repair
- all 3 misalignment types, with capacity treated as elastic (the lunar-landing
  case) while extraordinary mobilisation stays the exception rather than the
  assumption
- support is not a test of value: rights that survive majority disagreement,
  policies good for those with political resources and bad for those without,
  future generations, and slavery as the case that settles the argument
- the "we just need political will" lament and the instruction to diagnose what
  the actor is actually unwilling to support
- the 2 asymmetric self-deceptions: stakeholders of established policies about
  value (the DARE example), advocates of new ideas about capacity and support
- the triangle and overlapping-circle graphics as mnemonics, not analytical
  tools
- the closing observation that the framework is a cue to use other methods
  rather than a stand-alone tool

What the MD adds beyond the source, and why it is not a fidelity problem: the
per-dimension question sets, the scale-and-pace test, the pilot-versus-system
warning, the "minimum consequential set" definition of required support, the
prohibition on numerical scoring, and the fragility triggers. These
operationalise Donahue's argument for an agent that has to ask questions in a
live conversation. They are consistent with the source and none contradicts it.
The prohibition on scoring is the strongest addition and follows directly from
the source's own point that the graphics are mnemonics rather than analytical
tools.

The MD attributes nothing to Donahue that the PDF does not support.

## Rules for this directory

Do not edit these files. They are evidence.

If a method MD turns out to misread its source, correct the MD and record the
correction there. The source stays as it is.

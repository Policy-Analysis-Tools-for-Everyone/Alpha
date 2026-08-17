# Original Copilot agent exports: historical evidence

Raw exports from **(v0.2)WHATSYOURPROBLEM?**, the Microsoft 365 Copilot
declarative agent this project recovered. They are the only surviving record of
how that agent was configured.

| File | What it is |
|---|---|
| `declarativeAgent_0.json` | The agent definition: instructions, named skills, conversation starters, declared capabilities, behaviour overrides. Source key `[J]` in `docs/BEHAVIOUR_SPEC.md` |
| `manifest.json` | Teams packaging metadata: name, version, description. Source key `[M]` |

**These files are never edited.** They retain the original agent's name, its
DSIT-specific addressing, and its truncated `instructions` field. Editing them to
match the current product would destroy the only evidence of what the original
actually was, and would make later work look like recovered behaviour when it is
not.

Two things to know before using them:

The `instructions` field **ends mid-sentence**, inside its second worked example:
`"…then test whether the binding issue is unmet need, delivery capacity,
political"`. The rest is lost. Nothing in this repository reconstructs it.

The original agent stopped at the problem statement and a value / capacity /
support readout. It has nothing to say about evidence, alternatives, criteria,
outcomes, trade-offs, decisions or storytelling. Citing it for any of those would
make later product decisions look like recovered behaviour. `BEHAVIOUR_SPEC.md`
Part A records what the original observably did; section A15 records what it did
not.

For most purposes `docs/BEHAVIOUR_SPEC.md` is the better working document,
because it has already separated what is evidenced from what is inferred. Use
the raw JSON for the original's exact wording and voice.

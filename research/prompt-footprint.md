# Prompt footprint

What policymemo.ai asks students to do, and the trace each prompt leaves. The research
uses it to tag every coded change as **prompted** or **not prompted** in its episode.
`design.md` section 4 says why.

**Derived from `skills/` at `0.2.0`.** When a skill changes, update this file in the same
commit and record the version. An episode is read against the footprint of the version
it ran on.

This is a reading of what the skills *say*. Whether the agent *does* it in a given
session is read off the transcript. `evals/wiki/findings.md` says several behaviours fire
unreliably (F5, F7, F12), so a listed prompt is not a guarantee that the student met it.

## How to read the tables

- **Prompt**: what the skill tells the agent to do to or for the user.
- **Trace**: what that leaves in the student's artefact if they take it up, which is what
  the echo check and the prompted flag look for.
- **Independent version**: what the same move looks like when the student makes it
  without having been asked. This is the evidence that counts.

## `house-rules` (every session)

| Prompt | Trace | Independent version |
|---|---|---|
| The vague-term challenge: *compared with what, for whom, over what period, with what consequence?* | A comparator, a group, a period and a consequence added after a word like "insufficient" | The student supplies a comparator unasked, or challenges a vague term in a peer's work |
| Placeholders for anything missing: `[add magnitude]`, `[add baseline or comparator]` and the like | Square-bracketed placeholders, often verbatim | The student names a gap and what would fill it, in their own words |
| Keep fact, interpretation, assumption, value judgement, hypothesis and unknown distinct; label them | Labels such as *assumption*, *hypothesis* | The student separates them without labels being asked for |
| The 3 standing considerations: public value, operational capacity, political support | The 3 terms, often as headed lines | Reasoning about value, deliverability and backing without the template, or in a peer review. **The course teaches the same terms**, so vocabulary alone is worth nothing |
| Name the trade-off rather than score the corners | A *key trade-off* line | The student says what their choice costs, unprompted |
| Contaminated measures: a figure that moves for reasons unrelated to what it measures is unsafe as evidence and as a success measure | A measure dropped or qualified, with the mechanism | The student spots a contaminated measure in a new case or a peer's work |
| Competing framings offered with their costs; the user chooses | Two framings named; one chosen | The student generates an alternative framing before the agent offers one |
| Market failure as one test of public basis, with the "direction" critique surfaced | A market-failure basis, or a direction argument | The student argues the public basis themselves. **Taught in the course** |
| Critical, not affirming; challenges weak assumptions | Concessions in the transcript | n/a: an agent behaviour, not a student move |
| One question per turn | n/a | n/a |

## `problem`

| Prompt | Trace | Independent version |
|---|---|---|
| Recast as a condition (deficit, excess, trend), with "too" | "Too many / too few ..." phrasing | A solution-free statement at the next agent-free `t0` |
| Challenge a solution presented as a problem, first | Solution removed from the statement | The student catches a hidden solution in the anchor case or a peer's statement. **Taught in week 1** ("don't introduce the solution in the problem statement") |
| Bound to one primary focus; merge, separate or nest overlapping statements | Narrower statement | Scope narrowed with a stated reason |
| Specify affected group; push back on broad labels | A named population | Same, unprompted |
| Magnitude and time, or a named metric, or a placeholder | Number, range, metric or placeholder | A metric chosen and argued for |
| Label problem, mechanism, symptom, constraint | The 4 labels | The distinction drawn in prose without the labels |
| Name one problem or a hierarchy; draw a system map if hierarchy | *Core problem*, *sub-problems*, *mechanisms*, *missing metrics* lines | A hierarchy recognised in the anchor case |
| Causal language treated as hypothesis; soften to "may contribute" | "May contribute" | Causal claims marked as claims without being asked. **Taught in week 1** ("causal claims implicit in problem diagnosis") |
| Read the framing through value, capacity, support | Readout lines | See `house-rules` |
| Four-part output: candidate statement, critique, revised statement, readout | The revised statement, often near-verbatim | **The highest echo risk in the product.** A revised statement close to the agent's is a J1 signal |

## `stakeholders`

| Prompt | Trace | Independent version |
|---|---|---|
| Position separated from motivation; several motivations per actor | A table of positions and motives | Motives distinguished in a peer's map or the anchor case |
| Power made concrete: what each actor can give or withhold | A "can withhold" column | Same, unprompted |
| Split organisations into actors where it matters | One organisation split into several | Same, unprompted |
| Include the people who have to make it work | Front-line actors added | Same, unprompted |
| Required-support check; non-opposition counts | A list of who must agree or refrain | Same, unprompted |
| Supporters versus allies; uncommitted actors visible | Labels | Same, unprompted |
| Mark what is known versus assumed about motives | Empty cells or *assumed* labels | Same, unprompted |

Known at `0.1.1`: under-fires when stakeholder work sits inside problem definition (F12).
A student adding an actor the agent missed is a strong J2 signal.

## `evidence`

| Prompt | Trace | Independent version |
|---|---|---|
| Start with the claim, then the evidence for it | Claims paired with sources | Same, in the anchor case |
| Relevance is not authority; transfer needs its own evidence | Applicability argued | Same, unprompted |
| Seek disagreement; look for uncomfortable knowledge | A contrary source added | Same, unprompted |
| Calibrate adjectives; match precision to knowledge | Softer or ranged claims | Same, unprompted |
| The test before collecting anything: would a different result change the decision? | A stated decision-relevance | Same, unprompted |
| Name the kind of uncertainty; identify the critical one | Uncertainty classified | Same, unprompted |
| Competing explanations where the mechanism is unclear | 2 explanations | Same, unprompted |

Known at `0.1.1`: catches contaminated measures reliably (F3); states its own general
knowledge without marking it (F1). Students meet both.

## `options`

| Prompt | Trace | Independent version |
|---|---|---|
| An option is a hypothesis; name the relevant actor; identify policy variables | Options tied to an actor and a lever | Same, unprompted |
| Challenge stock solutions; look sideways | Fewer stock options | Same, unprompted |
| Always a base case, never "do nothing" | "Business as usual" option | Same, unprompted. **The PPP template asks for "continue current policy"** |
| No 3 options because 3 feels normal; no decoys; no do-everything package | A smaller or reshaped set | Same, unprompted. **The PPP template says the standard tends towards 3** |
| Separate strategy from variant | Variants collapsed | Same, unprompted |

No alpha evidence on `options` as the leading skill.

## `criteria`, `outcomes`, `trade-offs`, `decide`

| Skill | Main prompts | Trace |
|---|---|---|
| `criteria` | One primary objective derived from the problem; distribution made concrete; values separated from practical constraints; each criterion with a role, direction and measure; weights made visible | A short, structured criteria list with directions |
| `outcomes` | Project outcomes, not intentions; base case projected forward; direction, magnitude and time; outside view; adverse scenario; switchpoints | Ranges, base case, an adverse scenario |
| `trade-offs` | Dominance first; outcomes not labels; keep incompatible values apart; who gains and loses; switchpoint | A trade-off statement ending before the recommendation |
| `decide` | *Prefer X because Y*; *this accepts Z*; the strongest case against; review conditions; why it is not already happening | The *prefer ... because ... accepts* formula, review conditions |

The `decide` formula is a high-echo trace, like `problem`'s revised statement.

## `story`

| Prompt | Trace |
|---|---|
| PPC memo mode: the 8 sections of the PPP template | **The assessed artefact itself.** Use of `story` on the PPP memo means the memo cannot be read as the student's writing without the course's AI-use declaration |
| Recommendation easy to find; strongest objection addressed; evidence tied to claims; uncertainty kept where it matters | A memo shaped like the agent's |
| Writing rules: UK spelling, no em dashes, digits, no filler | Stylistic markers. Weak signals of echo, never of reasoning |

## Overlap with the course

Most of the footprint is also taught. The skills cite the course's own readings, and
`story` uses the course's memo template. So "taught" is a second tag beside "prompted"
for every indicator. A change counts as independent evidence of agent influence only
where it is close in time to an agent move, absent from the comparable sequence arm, or
not taught. Rows above mark the overlaps most likely to mislead; the codebook should
mark all of them once the 2026-27 sequence is known.

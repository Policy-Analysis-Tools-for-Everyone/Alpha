# Debrief — problem-3

**Agent-written self-report.** Corroboration for
[`../transcripts/problem/problem-3.md`](../transcripts/problem/problem-3.md), which is
the record. See [`README.md`](README.md) for what this evidence class is and is not.

| | |
|---|---|
| Session | `../transcripts/problem/problem-3.md` |
| Tester | T002 |
| Date of session | August 2026. Exact day not recorded |
| Model used | **Not confirmed.** The tester could not say. The maintainer's estimate is Claude Opus 5 or Fable 5.1, recorded as an estimate and not as a finding |

**Second anonymisation pass applied.** T002's original retained country names as the
substance of the memo under review; those have been substituted here for consistency
with the transcripts. Skill file paths are retained deliberately — they are the finding.

---

## Part 1: The record

**1. Task.** The user uploaded a one-page policy memo they had drafted, arguing that
[the country]'s AI strategy should plan for four possible futures rather than one, and
asked a single question: "Did I define the problem well?"

**2. Skills and tools, in order.**

1. `view` on `/mnt/skills/user/01-problem-definition/SKILL.md` (the problem-definition
   method), read in two calls because the first was truncated.
2. `view` on `/mnt/skills/plugins/mdee:house-rules/SKILL.md` (the standing rules the
   method is bound by).
3. `memory_write`, creating a memory file recording the memo and the review request.
4. No web search, no other tools. The memo itself arrived as an uploaded PDF already in
   context, so no file-reading tool was called.

**3. Key outputs.**

- "The framework and the gap analysis are strong; the Issue paragraph is the weak part"
  — judgement, rested on the uploaded document read against the loaded method's criteria.
- "the paragraph labelled Issue is your recommendation restated as a premise" and "The
  title does the same thing" — rested on the document.
- Five critique points against the Issue paragraph, quoted by their labels:
  "Solution-shaped", "No magnitude", "No time horizon", "Wrong subject", "Two cores
  unnamed" — each rested on the document tested against the method's self-check criteria
  (no hidden solution, quantification, time horizon, condition not programme, hierarchy
  named).
- A revised two-sentence problem statement with three marked placeholders ("[add
  magnitude…]", "[add time horizon…]", "[add evidence…]") — drafted by the agent; the
  placeholders were deliberate gaps, not findings.
- A four-line readout. The public value and operational capacity lines rested on the
  document. The political support line — "Planning explicitly for a future where [the
  country] is a supplicant to [frontier labs abroad], or where AI is treated like fissile
  material, is uncomfortable to say out loud in [the capital]" — rested on general
  knowledge and assumption about the political context, not the document.
- A closing framing choice put to the user: is the core problem "*concentration risk*
  (the strategy bets on one future) or *missing capability* ([the country] has no access
  strategy and no non-proliferation posture)?" — rested on a tension identified within the
  document.

**4. Weak points.**

- "a strategy ministers have just announced" — unsupported. The memo describes a "current
  posture"; nothing in it says the strategy was recently announced or by whom. Asserted as
  fact when it was an assumption.
- "it's the part a minister reads first" — an assumption about readership presented as
  fact; the memo does not name its audience.
- The political support line quoted above rested entirely on the agent's general sense of
  the political climate in the national capital; no evidence in the session supports it.
- No position changes occurred; the session was a single review turn.

**5. Where we ended.** Finished: the critique of the Issue paragraph, a revised candidate
statement with marked gaps, and the readout. Left open: the three placeholders, and the
concentration-risk versus missing-capability framing choice, which was put to the user and
not answered before the session moved to this debrief.

## Part 2: The user's view

Answers recorded word for word, anonymised per the instruction. No interpretation added.

**1. What were you trying to do?**

> "Mostly test the new skill I hope."

**2. Where did you get to?**

> "I nice summary and analysis of a memo I'd drafted and sent to [Organisation 1]/[Organisation 2]"

**3. What surprised or frustrated you?**

> "I didn't look too closely... but I love that it broke the memo down along this lines of
> the course. and assessed it."

**4. What did you expect instead?**

> "I had no idea what to expect."

**5. Did it tell you anything you think was wrong?**

> "No..."

---

*T002's anonymisation note, as supplied: two government organisations named in the user's
second answer were replaced with [Organisation 1] and [Organisation 2]. Country names were
retained as the substance of the memo under review. No personal names, job titles, teams or
employers appeared in either part. Skill file paths were retained so the builder can
identify what fired.*

*Second pass applied here: country and capital names substituted, for consistency with the
transcripts. Skill file paths retained, per T002's reasoning, which was correct.*

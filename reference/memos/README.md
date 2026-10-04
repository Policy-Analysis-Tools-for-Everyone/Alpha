# Memo corpus

Real policy memos, and what their markers said about them, kept as evidence of
what good memo writing looks like in practice. The aim is to ground `story`,
and PPC memo mode in particular, in real memos and not only in the method
layer's account of them.

This file is the schema. It says how the folder is laid out and how to work in
it. The pattern is an LLM-maintained wiki: raw sources that are never
rewritten, a wiki distilled from them that is rewritten as often as the
evidence demands, and this file telling whoever maintains it what the rules are.

```text
reference/memos/
  raw/
    m0N-<topic>.md      the memo, converted to Markdown and anonymised
    m0N-feedback.md     what the two markers said, abstracted
  wiki/
    index.md            every wiki page, one line each
    log.md              append-only: what changed in the wiki, and when
    patterns.md         what recurs across the corpus, counted. Read first
    tensions.md         where the corpus and the story skill disagree, and open questions
    rubric.md           the lens every memo page is read through
    memos/m0N.md        one evaluation per memo
```

## What this corpus is, and what it is not

5 memos from the MDEE module (IIPP0010) at the UCL Institute for Innovation and
Public Purpose, December 2025. All 5 answer the Personal Policy Problem brief
held at `../sources/ucl-ppc-one-pager-instructions.pdf`: an 8-section memo of
about 2 pages, endnotes outside the count, with a 1-page cover note for the
marker. Each memo is written in role, from a real or plausible sender to a real
decision maker.

**It is a selection of strong memos, not a sample.** The maintainer picked them
as among the best. With no weaker memos for contrast, the corpus can show what
strong memos have in common and where even strong memos fail. It cannot say
which features earn marks. Marks are not published here.

**What it shows first is that memos are contextual.** The strongest memos
include one with all 8 of the brief's sections and one with 4. Each was a
judgement about this reader, this decision and this much space. The 8 sections
are a guide. What this project's tools should build is the analysis that lets
a writer see what each section would add or cost, and choose.

**It comes from one module with a point of view.** MDEE teaches
mission-oriented policy and market shaping, and the memos show it. A pattern
here may be the module's frame rather than good practice in general.
`tensions.md` T6 has the detail.

## Rules

**No skill reads this folder.** Same rule as `../domain/` and `../sources/`. A
finding reaches the runtime only by changing the method layer
(`../methods/capabilities/storytelling-guidance.md`) and then the skill, with
the finding cited by ID.

**Never put memo text into a skill, a port or the site.** The memos are held
with their authors' consent for this purpose. They are not under the
repository's content licence and are not covered by `../../LICENSE-CONTENT.md`.
Using a memo as a worked example in a skill would also teach the agent one
student's topic. Distil the move, in this project's own words.

**Raw is evidence and is never rewritten.** A conversion error is corrected,
and the correction recorded in `wiki/log.md`. An evaluation that turns out
wrong is corrected in the wiki, not by editing the memo.

**Counts are the argument.** Always *n of 5 memos*, never a percentage. Name
the memos behind every count.

**Keep 3 kinds of judgement apart.** Every wiki claim is one of these:

| Kind | Source | Written as |
|---|---|---|
| Marker | `raw/*-feedback.md` | "Marker 1 says…", paraphrased. Never quoted, never with a mark |
| Rubric | Read against `wiki/rubric.md` by whoever maintains the wiki | "Rubric R8: …" |
| Check | Something anyone can verify: arithmetic, a source, a contradiction between 2 sentences | "Check: …", with the figures |

Marker judgements are the only external evidence in the folder. Rubric
judgements are the maintainer's or the model's reading, and carry the bias of
whoever wrote the rubric, which is the same source as the skills. Where a
marker and the rubric disagree, record the disagreement. Never resolve it
quietly in either direction.

## Privacy

1. **Authors are anonymous.** No name, candidate number, file metadata or link
   to an author's own files is committed. The mapping from ID to person is
   held privately by the maintainer.
2. **Personas become roles.** Where a memo is written from or to a real person,
   the name is replaced by the role in square brackets, so the repository never
   appears to hold a memo written by or sent to that person. Citations are left
   intact, so a persona can be recovered from them. That is deliberate:
   writing in role to a public office is part of the assignment.
3. **Marks are never published, and marker feedback is held only in
   abstract**, restated in this project's words. Comments about memos outside
   the corpus are dropped.
4. **Consent is recorded** in each memo's header. Add a memo only with its
   author's consent to this use. Redact before committing, never after.
5. **No PDFs or Word files are committed.** The Markdown is the copy.

## Three operations

### Ingest: a memo arrives

1. Give it the next ID, `m06`, and add consent to the header.
2. Convert it to `raw/m0N-<topic>.md` using an existing raw file's header. Keep
   the text verbatim, typos included. Record every departure in the header's
   *Conversion* row: dropped formatting, normalised quotes, removed links.
3. Check the conversion against a text extraction of the source, word by word.
   The only differences should be the ones the header lists.
4. Search the raw file for the author's name, the persona names and any link
   to the author's own files.
5. If there is marker feedback, add `raw/m0N-feedback.md` from an existing
   one: the points made, in this project's words, with no mark and no quotation.
6. Write `wiki/memos/m0N.md` against `wiki/rubric.md`. Then re-mine
   `patterns.md`: does the memo add to a count, contradict a pattern, or leave
   something with nowhere to go? A contradiction is the valuable case. Record
   it, don't smooth it over.
7. Add a line to `wiki/log.md` and update `wiki/index.md`.

### Query: what do strong memos do about X?

Start at `wiki/patterns.md`, then the memo pages. Cite the memo ID behind any
claim, and say which of the 3 kinds of judgement it is.

### Lint: after each ingest, or before a skill change

- Every count in `patterns.md` matches the memo pages.
- Every open question in `tensions.md` is still open.
- Every page is in `index.md`. Record the lint in `log.md`.

## From here to a skill

The route is the one `../../evals/README.md` uses: finding, change hypothesis,
method revision, skill revision, then a test. The difference is the input.
`evals/` records what the agent did. This folder records what strong human
memos do. Neither is enough alone: a pattern here says what to aim at, and only
a session in `evals/` says whether the agent hits it.

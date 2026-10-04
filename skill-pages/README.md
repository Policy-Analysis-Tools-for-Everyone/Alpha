# Skill pages

Durable explanations of each skill, published at `policymemo.ai/skills/<skill>/`.
These are reference pages, updated as the skill changes. They are not dated posts:
essays and reflection go to [CIVICWORKS](https://civicworks.substack.com).

Nothing is published until the first page exists. Then `tools/build-blog.py` writes
`/skills/`, adds Skills to the nav, and points that skill's homepage card at its page.

## Add a page

Create `skill-pages/<skill>.md`, where `<skill>` is one of: problem, stakeholders,
evidence, options, criteria, outcomes, trade-offs, decide, story.

```
---
title: Problem
summary: One sentence on what the skill does. It appears on /skills and in link previews.
updated: 2026-10-20
draft: true               # remove this line to publish
---

## What it does

## Why it matters

## What policymemo.ai looks for

## Where the method comes from

## How to use it

## References
```

Leave out any section that has nothing in it yet. The canonical method for each skill
is in `reference/methods/` (see `docs/AUTHORING.md`). A skill page explains it for
people, so it shouldn't copy the method file.

# Blog

Posts for policymemo.ai/blog. Write in Markdown; the site pages are generated.

## Write a post

Add a file to `posts/`. The file name becomes the address:
`posts/why-it-asks-first.md` is published at `policymemo.ai/blog/why-it-asks-first.html`.

Start the file with:

```
---
title: The post's title
date: 2026-10-13
category: skills          # why | skills | guides | updates
skill: problem            # skill posts only: problem, stakeholders, evidence, options,
                          # criteria, outcomes, trade-offs, decide, story
summary: One sentence. It appears on the blog index and in link previews.
draft: true               # remove this line to publish
---
```

Then write the post in Markdown: `## ` for section headings, `[text](url)` for links,
`> ` for a quotation.

## What publishing does

When a post without `draft: true` reaches `main`, the "Build site" workflow runs
`tools/build-site.py`, which:

- writes the post's page and the blog index in `docs/blog/`
- adds "Notes" to the homepage footer, once at least one post is published. Notes is
  not in the nav, which is What it does, How it behaves, Updates, CIVICWORKS and Beta access
- for a skill post, adds a "Read the post" link to that skill's card on the
  homepage, and marks the skill as published in the series on the blog index. The series
  section itself appears once the first skill post is published
- writes an Atom feed of every post, `docs/blog/feed.xml`, and once an `updates` post is
  published, `docs/blog/feed-updates.xml` with only those. There is no visible
  link: feed readers find them when someone pastes `policymemo.ai/blog` into one.
- shows category labels and the filter on the blog index only once posts in two or more
  categories are published, with a filter button only for categories that have posts

Drafts are never published. To see everything, drafts included, run
`python3 tools/build-site.py --drafts /tmp/blog-preview/blog` and open the files.

The blog's styles are in `blog.css` and are inlined into every page at build time.

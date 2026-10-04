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

When a post without `draft: true` reaches `main`, the "Build blog" workflow runs
`tools/build-blog.py`, which:

- writes the post's page and the blog index in `docs/blog/`
- adds "Blog" to the homepage nav and footer, once at least one post is published
- for a skill post, adds a "Read the post" link to that skill's card on the
  homepage, and marks the skill as published in the series on the blog index

- writes two Atom feeds: `docs/blog/feed.xml` (every post) and `docs/blog/feed-updates.xml`
  (`updates` posts only). Feed readers find them from any page, and the footer links to them.

## Email subscribers

Email is sent from the feed, so publishing a post is all it takes. Buttondown checks
`https://policymemo.ai/blog/feed.xml` and emails each new post to subscribers. To switch it on:

1. Create a Buttondown newsletter (sender `jack@civicworks.co` for now, `jack@policymemo.ai`
   once the domain's mail is set up).
2. In Buttondown, add an RSS-to-email automation for the feed address above, sending each new item.
3. Set `BUTTONDOWN` in `tools/build-blog.py` to the newsletter's username. The sign-up form
   then appears under "Follow along" on the Notes page. It stays hidden until this is set.

Drafts are never published. To see everything, drafts included, run
`python3 tools/build-blog.py --drafts /tmp/blog-preview/blog` and open the files.

The blog's styles are in `blog.css` and are inlined into every page at build time.

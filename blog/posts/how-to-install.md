---
title: How to install policymemo.ai in Claude
date: 2026-10-04
category: guides
summary: Two minutes on a paid Claude plan, about ten on the free plan. You do it once, on a computer.
---

You install policymemo.ai once, in Claude on a computer: in your browser at [claude.ai](https://claude.ai) or in the Claude desktop app. On a paid plan it takes about 2 minutes. On the free plan it takes about 10, because the skills go in one at a time.

## First, check code execution is on

Open **Settings**, then **Capabilities**, and make sure code execution is switched on. It is on by default for most people. If it is off, policymemo.ai installs and then appears to do nothing, which is confusing enough that it is worth the 20 seconds now.

## On a paid plan: upload the zip

This works on Pro, Max, Team and Enterprise.

1. Download the zip from the [policymemo.ai homepage](https://policymemo.ai). Leave it zipped. Claude wants the file exactly as it arrives.
2. In Claude, open **Customize**, then **Plugins**.
3. Click **Add**, then **Upload local plugin**.
4. Drag the zip in, or browse to it, and click **Upload**.
5. Wait for the security scan to finish, then switch it on.
6. Start a new chat.

Claude will warn you that it cannot verify what is inside add-ons made by other people. That warning is correct, and it appears for everything of this kind. Everything policymemo.ai contains is readable in the [skills folder on GitHub](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/tree/main/skills) if you want to check first.

A zip install does not update itself. If you would rather have updates arrive on their own, add policymemo.ai as a marketplace instead: in **Plugins**, click **+** next to **Personal plugins**, choose **Add marketplace**, paste `Policy-Analysis-Tools-for-Everyone/Alpha`, click **Sync**, then **Install**.

## On the free plan: add the skills one at a time

Plugins need a paid plan, but skills do not, and once all 10 are in, policymemo.ai behaves the same.

1. In Claude, open **Customize**, then **Skills**.
2. Click **+**, then **Create skill**.
3. Upload the first file below. Do not unzip it.
4. Check it is switched on, then repeat for the rest.

Start with [house-rules.zip](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/house-rules.zip). It is the one that makes the others behave. Then add these 9 in any order: [problem](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/problem.zip), [stakeholders](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/stakeholders.zip), [evidence](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/evidence.zip), [options](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/options.zip), [criteria](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/criteria.zip), [outcomes](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/outcomes.zip), [trade-offs](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/trade-offs.zip), [decide](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/decide.zip) and [story](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/story.zip).

If you only ever add 2, add house-rules and problem.

## How you know it worked

On a paid plan, policymemo.ai is listed under **Personal plugins** and switched on. On the free plan, all 10 skills are listed under **Skills**. Nothing appears in your chat window, and nothing is supposed to.

## Then use it

Start a new chat and describe the problem you are working on, the way you would to a colleague. There are no commands to learn. The right skill loads as the conversation needs it.

It will ask you questions before it writes anything. That is deliberate, and [the first post here](why-it-asks-first.html) explains why.

If something goes wrong, [tell me](mailto:jack@civicworks.co?subject=policymemo.ai%20install).

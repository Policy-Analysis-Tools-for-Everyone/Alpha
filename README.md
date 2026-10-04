# policymemo.ai

policymemo.ai helps you work through a public policy problem properly: working out what
the problem actually is, testing what you know, building and weighing options,
deciding, and writing it up for someone else to read.

It's built to make bad analysis harder to write. It challenges weak framing,
refuses to invent figures, keeps competing framings visible instead of quietly
picking one, and asks you one real question at a time rather than handing you a
plausible-looking document on request.

Inside it are 10 analytical capabilities that work together as one toolkit. You
don't pick between them. Claude does.

> **Beta 0.1.2.** All 11 files are written. 17 real sessions across 4 testers have been
> run against them, and 2 skills were revised from what those sessions found. The
> revised versions have no sessions of their own yet. Read [Status](#status)
> before you rely on this for anything that matters.

---

## Install policymemo.ai in Claude

You'll need about 2 minutes. There's nothing to download if you're on a paid plan,
and no technical setup either way.

Quick tutorial video for Claude here: https://www.loom.com/share/7a0075882a884d71bbc6a4b4dd29c9bc

### Step 0: turn on code execution

Claude needs this switched on before any add-on like policymemo.ai will work. It's on by
default for most people.

1. Open Claude, in your browser at [claude.ai](https://claude.ai) or in the Claude
   desktop app.
2. Open **Settings**.
3. Go to **Capabilities**.
4. Make sure code execution is switched on.

If you skip this, policymemo.ai installs and then appears to do nothing, which is
confusing enough that it's worth the 20 seconds now.

### If you're on Claude Pro, Max, Team or Enterprise

This is one installation. You do it once.

1. Open Claude.
2. Click **Customize** in the sidebar on the left.
3. Click the **Plugins** tab.
4. Find **Personal plugins**, and click the **+** button next to it.
5. Click **Add marketplace**.
6. Paste this into the box:

   ```
   Policy-Analysis-Tools-for-Everyone/Alpha
   ```

7. Click **Sync**.
8. You'll see **policymemo.ai** appear in the list. Click **Install** next to it.
9. Claude will warn you that it can't verify what's inside add-ons made by other
   people. That warning is correct and it appears for everything of this kind. If
   you want to check first, everything policymemo.ai contains is readable in the
   `skills` folder of [this
   repository](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/tree/main/skills).
10. Start a new chat.

**What you should see afterwards.** The **Install** button changes to **Manage**,
and policymemo.ai is listed under Personal plugins. That's it. Nothing appears in your
chat window, and nothing is supposed to.

You may also see a second item called **policymemo.ai evaluation**. You don't need it,
whether you're using policymemo.ai or helping test it.

If you're testing, the useful thing is the conversation itself: what you were
trying to do, and what felt useful, confusing, wrong or missing. See [Telling us
when it goes wrong](#telling-us-when-it-goes-wrong) for how to send it. policymemo.ai
evaluation is what happens afterward, on our side: reviewing conversations like
yours, finding patterns, and deciding what's worth changing. It has no part in
actual policy work.

### Error 403: If the marketplace install fails with "Failed to fetch content: 403"

If you encounter error 403 on the desktop app, try a browser first. It may just work, and
it's the fastest way to find out.

If the browser hits the same error, or the desktop app is what you actually
need working, install the plugin from a file instead of the marketplace. This
uses a different route in Claude that doesn't depend on the fetch that's
failing.

1. Download [`policymemo-ai-claude.zip`](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/download/policymemo-ai-claude.zip),
   the same file as the Download button on [policymemo.ai](https://policymemo.ai).
   Don't unzip it.
2. Open Claude, click **Customize**, then **Plugins**.
3. Click **Add**, then **Upload local plugin**.
4. Drag the file in, or browse to it, then click **Upload**.
5. You may have to wait for security scans to complete before you can switch on.

This installs the same plugin as the marketplace route: one entry, all 10
skills grouped under it. The only thing that changes is where the file comes
from. It doesn't update itself the way a marketplace install does; see
[Updating policymemo.ai](#updating-policymemoai) below.

If that dialog doesn't work either, fall back to installing the skills one at
a time, below as detailed in the method below.

### If you're on the Claude Free plan

Add-ons of the plugin kind need a paid plan. You can still have all of policymemo.ai, by
adding the pieces one at a time. It takes about 10 minutes and it behaves
identically once it's done.

1. Open Claude.
2. Click **Customize** in the sidebar, then the **Skills** tab.
3. Click the **+** button, then **Create skill**.
4. Download the first file below by clicking it, then upload it here. Don't unzip
   it. Claude wants the zip file exactly as it downloads.
5. Make sure the skill is switched on in your skills list.
6. Repeat for each file in the list.

**Start with this one. It's the one that makes the others behave.**

- [house-rules.zip](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/house-rules.zip)

Then these 9, in any order:

- [problem.zip](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/problem.zip)
- [stakeholders.zip](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/stakeholders.zip)
- [evidence.zip](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/evidence.zip)
- [options.zip](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/options.zip)
- [criteria.zip](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/criteria.zip)
- [outcomes.zip](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/outcomes.zip)
- [trade-offs.zip](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/trade-offs.zip)
- [decide.zip](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/decide.zip)
- [story.zip](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/skills/story.zip)

**What you should see afterwards.** All 10 listed under Skills, switched on.

If you only ever do 2 of these, do `house-rules` and `problem`.

---

## What happens after installation

You don't choose a workflow, and you don't work through 10 steps in order.

Start an ordinary chat and describe the policy problem you're actually working on,
in your own words, the way you'd describe it to a colleague. policymemo.ai makes several
analytical capabilities available to Claude, and Claude reaches for the relevant
one as the work develops. When the conversation moves on, so does it.

Three openings that work:

> "I think we've already jumped to a solution. Help me work out what the actual
> problem is."

> "We've got evidence from another country that this worked. How much weight
> should we put on it?"

> "I've got 3 options and I'm struggling to decide what should count as better."

**You never need to type `/problem` or `/evidence` or anything like it.** In a
normal Claude chat there's no menu to pick from and no command to remember. Describe
the situation and the right capability loads on its own. If you'd rather be
explicit you can say "help me think about who's affected here", and that works too,
because it's a description of the problem rather than a command.

One thing worth knowing: it asks questions back. That's deliberate. If you want a
document produced without being asked anything, this is the wrong tool.

---

## What has actually been installed

A set of specialist instructions for different parts of policy analysis. They sit
quietly until they're relevant, and they work together as one toolkit.

It's one Claude with more to draw on, working from the same conversation.

| Capability | The question it handles |
|---|---|
| `house-rules` | How the whole thing behaves. Always in play |
| `problem` | What is the problem? |
| `stakeholders` | Who matters, why, and with what power? |
| `evidence` | What do we know, and how strong is it? |
| `options` | What could we do? |
| `criteria` | What counts as better? |
| `outcomes` | What would probably happen? |
| `trade-offs` | What do we gain and give up? |
| `decide` | What should we choose? |
| `story` | How should this be communicated? |

There's no order you have to follow. Real work moves backwards as often as
forwards. Evidence sends you back to the problem, trade-offs expose a criterion
nobody stated, deciding reveals the options were poor. Each capability knows which
gaps belong to its neighbours and carries on into them.

---

## Which Claude plans can use it

| Plan | What you can use | How |
|---|---|---|
| Free | All of policymemo.ai | Upload the 10 files, above |
| Pro | All of policymemo.ai | One installation, above |
| Max | All of policymemo.ai | One installation |
| Team | All of policymemo.ai | One installation |
| Enterprise | All of policymemo.ai | One installation |

The one-click route needs a paid plan, because that's how Claude handles add-ons of
this kind. Free users get the same capabilities by uploading them individually.

Everyone needs code execution switched on. See [Step 0](#step-0-turn-on-code-execution).

---

## Updating policymemo.ai

policymemo.ai will change, especially while it's in beta.

**If you installed it in one go**, updates arrive on their own in most cases. To
pull them in by hand, go to **Customize**, then **Plugins**, find policymemo.ai, and use
the update or re-sync option. You don't reinstall and you don't download anything.

**If you uploaded the zip or the files individually**, you'll need to download
the changed ones again and re-upload them. There's no automatic route. Watching
this repository on GitHub will tell you when something changes.

---

## Getting more out of it

Worth doing if you're on one policy problem for weeks rather than one afternoon.

Create a Project in Claude for that piece of work, and put your draft, your
evidence and your notes into it. Then paste the contents of
[`skills/house-rules/SKILL.md`](skills/house-rules/SKILL.md) into the project
instructions.

That gives you 2 things the plugin alone doesn't. Your actual material stays in
context across every conversation, and the house rules apply on every single turn
rather than loading when they're needed. It's the closest this gets to a dedicated
policy analyst who already knows your case.

Full project sharing works only on Team and Enterprise plans. On Free, Pro and Max
a project is yours alone.

---

## Status

Written is not tested. Four states worth keeping apart:

- **Written.** The file exists and says what it should do.
- **Structurally checked.** Frontmatter validates, links resolve, no contradictions
  found by reading.
- **Behaviourally tested.** Run on real work in a session that was saved.
- **Regression-tested.** A saved case re-runs and still passes after changes.

| Skill | Written | Structurally checked | Behaviourally tested |
|---|---|---|---|
| `house-rules` | yes | yes | 17 sessions, 4 testers, on `0.1.1`; revised into `0.1.2`, which has none of its own yet |
| `problem` | yes | yes | 4 real sessions, on `0.1.1`; revised twice into `0.1.2`, which has none of its own yet |
| `stakeholders` | yes | yes | exercised inside other sessions and in 1 reported run; no session of its own |
| `evidence` | yes | yes | 2 real sessions, plus 2 reported |
| `options` | yes | yes | **no.** Never appeared in a session header |
| `criteria` | yes | yes | exercised inside other sessions and in 1 reported run; no session of its own |
| `outcomes` | yes | yes | exercised inside other sessions and in 1 reported run; no session of its own |
| `trade-offs` | yes | yes | **no.** Never appeared in a session header |
| `decide` | yes | yes | exercised in 2 reported runs; no session of its own |
| `story` | yes | yes | 3 real sessions, 1 a non-trigger |
| `evaluation` | yes | yes | produced 3 debriefs and a tester report |

**17 sessions, 4 testers, all in August 2026, all on plugin `0.1.1`.** `0.1.2`
revised `house-rules` and `problem` from what those sessions found, and has no
sessions of its own yet. 9 of the 17 are transcripts; the rest are a tester's
cross-session report and a tester's note. 7 of the 10 capabilities have been
exercised at all; `options` and `trade-offs` have not.

No session is confirmed cold, and nothing yet tests whether the agent accepts
sound work rather than something to challenge, since every session so far gave
it something to push back on. Those are the 2 largest gaps.

The method layer is settled. The runtime has real evidence behind parts of it,
unevenly, and the current text of the two most load-bearing files has none.

---

## Telling us when it goes wrong

This is a beta, and the most useful thing you can send is a conversation where it
was **confidently wrong.** Those are worth more than the ones where it worked, and
they're the easier ones to lose.

[**Send a session report**](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/issues/new?template=session-report.yml).
It asks 5 questions and takes about 3 minutes:

1. What were you trying to do?
2. Where did you get to?
3. What surprised or frustrated you?
4. What did you expect instead?
5. Was there anything it told you that you think was wrong?

**Read this before you paste a conversation.** Reports are public. Take out names,
organisations, figures, and anything pre-decision or commercially or politically
sensitive. Replace them with equivalents that keep the shape of the reasoning, and
say which parts you changed. The analytical shape is what matters, rather than
your real numbers. If a conversation can't be made safe that way, answer the
questions and leave the conversation out. A described problem is still useful.

`evals/sessions/t001-problem-receipt-confirmation.md` shows how far the
anonymisation can go while the case still works.

You don't have to write anything up. Answering the questions is enough, and we do
the analysis.

---

## For developers and contributors

Everything below here is for people working on policymemo.ai rather than using it.

### Working on the skills

```bash
git clone https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha mdee
cd mdee
claude --plugin-dir .
```

That loads all 11 skills from `skills/` without installing anything. The canonical
files live in `skills/<name>/SKILL.md` and that is the only copy. Everything else
is generated from them or points at them.

After changing a skill, rebuild the downloadable zips and commit the result:

```bash
python3 tools/build-skill-zips.py
```

A new skill also has to be added to the relevant plugin entry in
`.claude-plugin/marketplace.json`, or it won't ship. There's no default scan to
fall back on.

### How it's packaged

`.claude-plugin/marketplace.json` lists 2 plugin entries, both drawing from the
same `skills/` folder. `mdee` carries `house-rules` and the 10 policy capabilities.
`mdee-evaluation` carries `house-rules` and `evaluation`, and exists so that people
doing policy work don't carry a capability aimed at people maintaining the agent.

`docs/AUTHORING.md` section 12 has the full detail, including what to do if the
2-entry layout ever fails to install.

### What sits behind the skills

Three layers, deliberately separate.

**The method layer**, `reference/methods/`, is canonical. Ten capability methods
and 3 shared methods, written in enough depth for maintainers: provenance,
distinctions, worked examples, anti-patterns, scaffolds and self-check rubrics.
Every skill names the method file it is grounded in. See
[`reference/methods/README.md`](reference/methods/README.md).

**Shared methods are not extra steps.** Strategic alignment, uncertainty and
learning, and risk-opportunity appraisal cut across several capabilities. A skill
carries the distilled part it actually needs and calls nothing at runtime.
`outcomes` needs the outside view and a rule for turning an ungrounded forecast
into a learning question; it does not need the rest of the appraisal method.

**The writing layer**, `skills/story/writing.md`, is the output-quality
specification for everything the agent writes. It ships with `story`, which
applies it in full to documents; `house-rules` carries the subset that holds in
every reply. It separates the agent's register in a reply from the user's
register in a document they send on, and it shapes writing without changing
evidence, analysis or necessary technical terms. It carries no individual's
personal style.

**Sources and domain material.** `reference/sources/README.md` lists every source
the method layer cites. `reference/domain/` holds domain-specific material. No
skill reads either.

### How house-rules reaches the other capabilities

Claude chat has no always-on instruction layer that ships with an add-on. So each
capability skill opens by instructing Claude to load `house-rules` first and treat
it as binding, and carries the 2 rules that would be catastrophic if it were
absent: invent nothing, and the user decides.

That line is load-bearing. Copy it verbatim into any new skill. Part 0 of
`evals/tests/capability-alpha-pack.md` is the test for whether it's actually
working, and it should be run before anything else in the pack.

### Evaluation

`evals/` holds the improvement loop: real sessions, a wiki that distills them into
findings, and synthetic capability and regression cases. `evals/README.md` explains
what each directory is for and how to save a session;
[`evals/wiki/findings.md`](evals/wiki/findings.md) is the one to read first, since
everything in `evals/sessions/` is a source for it.

Run real sessions in the configuration you ship, which is an ordinary Claude chat
with the plugin installed. Running one in Claude Code measures a runtime no user
has.

`evals/testers.md` is a pseudonymous register of who ran which session, so that
*how many independent people* is answerable and one person's repeated objection
never gets counted as several users. Nothing about a tester ever reaches policymemo.ai
during a session: the register is evaluation evidence, and loading any of it into
the agent would measure a personalised build rather than the product a new person
installs. `evals/README.md` carries that rule and the privacy rules with it.

### Provenance

Every skill carries a sourcing header naming its canonical method and what it is
**not** grounded in. A skill with an empty "not grounded" line is either very well
sourced or not being honest.

| Key | Source |
|---|---|
| `[B]` | Bardach, *A Practical Guide for Policy Analysis*, the main analytical spine |
| `[T]` | Donahue, "Strategic Alignment for Policy Analysis and Design", HKS Case 2090.0 |
| `[P]` | Product decisions recorded in `docs/BEHAVIOUR_SPEC.md` |
| `[O]` | Material the project owner authored directly |
| `[E]` | Behavioural evidence from saved sessions |

The capability methods carry their own fuller citations, including Weimer and
Vining, Fisher and Ury, May, Saltelli and Giampietro, Rodrik, McGuinness and
Slaughter, Flyvbjerg, Funtowicz and Ravetz, Kattel and colleagues, and Sharpe and
colleagues.

[`docs/BEHAVIOUR_SPEC.md`](docs/BEHAVIOUR_SPEC.md) specifies the core behaviour:
the rules that hold in every conversation and how the agent defines a problem.
Every other capability is specified by its method file.

The method files set out their sources' ideas in this project's own words, with
citations. No third-party text is reproduced beyond short attributed examples.
See [`reference/sources/README.md`](reference/sources/README.md) for the full
citations list.

`reference/domain/dpi/` holds a synthesis of 2 UCL IIPP papers on digital public
infrastructure. It is domain material rather than generic method, and only one
thing from it reaches the runtime: `house-rules` records a live disagreement it
deliberately does not settle, whether market failure is the right primary test for
public action, or whether the better question is what direction is embedded in a
framing and who chose it.

### Building on this

[`docs/AUTHORING.md`](docs/AUTHORING.md) is the contract: how the method layer and
the skill layer differ, how to compress one into the other, frontmatter that works
on every surface, why descriptions matter more than anything else in the file, and
the loop that turns real use into a revision.

The 2 rules most often broken are *no document-shaped replies* and *do not restate
the house rules*.

### Other surfaces

Each skill is a `SKILL.md` with spec-compliant frontmatter, so they also work
through the Skills API. If you assemble several into one system prompt, put
`house-rules` first.

Microsoft 365 Copilot and Google Gemini versions are generated from `skills/` into
`dist/ports/`. Set-up steps for both are on the [install page](https://policymemo.ai/install/):
[Copilot](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/ports/policymemo-ai-copilot.zip),
[Gemini](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/raw/main/dist/ports/policymemo-ai-gemini.zip).
The Copilot version is designed for the free Copilot Chat tier, and falls back to
the instructions alone where uploading files isn't allowed. Neither has been tested yet. See `ports/README.md`.

## Licence

Copyright (c) 2026 Jack Strachan. Code (`tools/`, `.github/`, `.claude-plugin/`)
is under the [MIT Licence](LICENSE). Everything else written for this project,
including the skills, methods, docs and evals, is under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Third-party sources are
cited, not licensed. See [`LICENSE-CONTENT.md`](LICENSE-CONTENT.md) for the detail.

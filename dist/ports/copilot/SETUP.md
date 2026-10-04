# Set up policymemo.ai in Microsoft 365 Copilot

This builds policymemo.ai as an agent in Copilot Chat. It takes about 10 minutes and
needs no admin rights, as long as your organisation lets you create agents.

It's a port of the Claude version, and it's alpha. Read [What to expect](#what-to-expect)
before you rely on it.

## What you need

- A work or university Microsoft account with Copilot Chat. The free tier included
  with most Microsoft 365 accounts is enough.
- This folder, unzipped. You'll paste from `instructions.txt` and upload the files in
  `knowledge/`.

**Check first:** open Copilot Chat and look for **Create agent** (sometimes **New
agent**) in the left-hand panel. If it isn't there, your organisation has switched
agent creation off and none of this will work. Ask your IT service.

## Steps

1. Open Copilot Chat and click **Create agent**.
2. Click the **Configure** tab. Skip the chat-style **Describe** tab, because it
   rewrites what you give it.
3. **Name:** `policymemo.ai (alpha)`
4. **Description:** `Works through a public policy problem with you: defines it, tests
   the evidence, builds and weighs options, decides and writes it up. Challenges weak
   framing and refuses to invent figures.`
5. **Instructions:** open `instructions.txt`, select everything, copy, and paste it
   into the box. It's about 7,700 characters, and the limit is 8,000.
   **Check it pasted whole:** scroll to the end of the box. The last words should be
   *"is still flagged in any document I produced."* If they aren't, the paste was cut
   short. Clear the box and try again.
6. **Knowledge:** click **Upload files** and add all 10 files from `knowledge/`
   (`MDEE 00 house rules.txt` to `MDEE 09 story.txt`). Don't rename them, because
   the instructions find them by name.
   If there's no upload option, or it's greyed out, skip this step. Your organisation
   doesn't allow it on your plan. The agent still works from the instructions alone,
   with less depth. Say so if you send us a report.
7. **Web search:** switch it off for now. The Claude version doesn't search the web
   unless asked, and keeping them alike makes reports comparable.
8. **Starter prompts:** add these, title then message.

   | Title | Message |
   |---|---|
   | Find the real problem | I think we've already jumped to a solution. Help me work out what the actual problem is. |
   | Weigh the evidence | We've got evidence from another country that this worked. How much weight should we put on it? |
   | Compare my options | I've got 3 options and I'm struggling to decide what should count as better. |
   | Who's affected | Help me think about who's affected by this and whose support it needs. |
   | Test my draft | Here's my draft problem statement. Tell me what's weak about it. |
   | Write it up | Help me turn this analysis into a one-page memo for a decision-maker. |

9. Click **Create**.

## Sharing it

Once it's created you can use **Share** to send a link to people in the same
organisation, if your organisation allows it. People outside it can't use your link,
so they need to follow these steps themselves.

## What to expect

- **It asks questions back.** That's deliberate, the same as the Claude version.
- **It's a different product underneath.** It runs on Microsoft's models, not Claude,
  with the same written rules. Expect it to drift from them more, especially over a
  long conversation.
- **The knowledge files are consulted, not memorised.** The core rules are in the
  instructions and always apply. The detailed method for each capability is in the
  files, and Copilot reads them when it searches. It may not search every time.
- **Updates aren't automatic.** When policymemo.ai changes, download the new port,
  paste the new instructions and replace the knowledge files.

## Telling us when it goes wrong

Use the [session report](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/issues/new?template=session-report.yml)
and say at the top that it was **Copilot**, and whether the knowledge files were
uploaded. The same anonymising rules apply as for the Claude version.

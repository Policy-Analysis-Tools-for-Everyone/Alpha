# Set up policymemo.ai in Google Gemini

This builds policymemo.ai as a Gem. It takes about 10 minutes.

It's a port of the Claude version, and it's alpha. Read [What to expect](#what-to-expect)
before you rely on it.

## What you need

- A Google account with access to Gems in Gemini. Work and education accounts can
  have Gems switched off by an administrator.
- This folder, unzipped. You'll paste from `instructions.txt` and upload the files in
  `knowledge/`.

## Steps

1. Open [gemini.google.com](https://gemini.google.com) and go to **Gems** (sometimes
   under **Explore Gems**), then **New Gem**.
2. **Name:** `policymemo.ai (alpha)`
3. **Instructions:** open `instructions.txt`, select everything, copy, and paste it
   into the box. Ignore Gemini's offer to rewrite it.
4. **Knowledge:** add all 10 files from `knowledge/` (`MDEE 00 house rules.txt` to
   `MDEE 09 story.txt`). That's Gemini's limit, so there's no room for anything else.
   Don't rename them, because the instructions find them by name.
5. Click **Save**.
6. **Check the instructions saved whole.** Reopen the Gem's settings and scroll to the
   end of the instructions. The last words should be *"is still flagged in any
   document I produced."*
   Google doesn't publish a length limit for Gem instructions. If yours were cut
   short, replace them with the contents of `instructions-fallback.txt`. That short
   version tells Gemini to take the full rules from `MDEE 00 house rules.txt`
   instead. Say so if you send us a report.

## Sharing it

Gems can be shared by link from the Gems list, if your account allows it. Anyone you
share with uses your copy, including its knowledge files.

## What to expect

- **It asks questions back.** That's deliberate, the same as the Claude version.
- **It's a different product underneath.** It runs on Google's models, not Claude,
  with the same written rules. Expect it to drift from them more, especially over a
  long conversation.
- **Updates aren't automatic.** When policymemo.ai changes, download the new port,
  paste the new instructions and replace the knowledge files.

## Telling us when it goes wrong

Use the [session report](https://github.com/Policy-Analysis-Tools-for-Everyone/Alpha/issues/new?template=session-report.yml)
and say at the top that it was **Gemini**, and whether you used the full or the
fallback instructions. The same anonymising rules apply as for the Claude version.

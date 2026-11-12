# 3. Pick a tool

The tools are more alike than different. All of them run in a terminal, read
your project, ask before they do risky things and take instructions from a
file in your repository. Pick one, learn the workflow, and you can switch
later in an afternoon.

**Everything in this chapter was checked on 12 November 2026** against the
linked official pages. Plans and prices change often, so check the links
before you pay for anything.

## The tools side by side

| | Claude Code | Codex CLI | Antigravity CLI | Gemini CLI |
|---|---|---|---|---|
| Made by | Anthropic | OpenAI | Google | Google |
| Command | `claude` | `codex` | `agy` | `gemini` |
| Access | A paid Claude plan (Pro or higher) or an API account. The free Claude plan does not include it. | A ChatGPT Plus, Pro, Business, Edu or Enterprise plan, or an API key | Free individual access with a Google account, and Google AI Pro and Ultra plans | Organizations with Gemini Code Assist licenses only. No free tier since 18 June 2026. |
| Instruction file | `CLAUDE.md` | `AGENTS.md` | See its docs | `GEMINI.md` |
| Official page | [Setup docs](https://code.claude.com/docs/en/setup) | [GitHub](https://github.com/openai/codex) | [Product page](https://antigravity.google/product/antigravity-cli) | [GitHub](https://github.com/google-gemini/gemini-cli) |

## About Gemini CLI and Antigravity CLI

Many tutorials still say Gemini CLI is free for everyone. That is out of
date. Google's own repository states that free individual access and the
Google AI Pro and Ultra plans moved to Antigravity CLI on 18 June 2026.
Gemini CLI is now aimed at organizations with Gemini Code Assist licenses.

If you are a student looking for Google's free option, look at Antigravity
CLI. Its limits are not listed here because they could not be verified from an
official page. Check the product page before you rely on it.

## Which one for a student

- **You have no budget.** Start with Antigravity CLI, which is the one with
  free individual access.
- **Your university gives you ChatGPT Edu.** Codex is listed as part of the
  Edu plan. Ask your IT department whether it is switched on for you.
- **You already pay for ChatGPT Plus or Claude Pro.** Use the tool that comes
  with it. You do not need a second subscription.
- **You are unsure.** Do not pay yet. Work through this guide with the free
  option, then decide.

Student discounts come and go. None are listed here because none could be
confirmed. Check each vendor's pricing page and your university's software
portal.

## Install

Run one of these, then start the tool inside a project folder by typing its
command. Each tool asks you to sign in the first time.

Claude Code, macOS, Linux or WSL:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Claude Code, Windows PowerShell:

```powershell
irm https://claude.ai/install.ps1 | iex
```

Codex CLI, macOS or Linux:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

Codex CLI, with npm on any system:

```bash
npm install -g @openai/codex
```

The package is `@openai/codex`. A package called just `codex` exists on npm
and is a different project.

Antigravity CLI: download it from
[antigravity.google/download](https://antigravity.google/download).

Gemini CLI, if your organization has a license:

```bash
npm install -g @google/gemini-cli
```

Piping a script from the internet into your shell runs whatever that script
contains. Only do it with the official addresses above, typed or copied from
the vendor's own page.

## The instruction file

Each tool reads a plain text file from your project at the start of a
session. You write in it what the agent should always know: how to run the
tests, which style the course wants, what it must not touch.

The file name differs per tool (see the table). The content can be the same.
[`templates/tutor-mode.md`](../templates/tutor-mode.md) is a ready-made one
for learning. Copy it into your project under the name your tool expects.

Next: [Your first session](04-first-session.md)

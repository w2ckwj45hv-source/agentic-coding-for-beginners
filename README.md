# Stop Copying from ChatGPT

**A beginner-friendly guide to agentic coding tools (Claude Code, Codex CLI,
Antigravity CLI and Gemini CLI) for CS students.**

If your workflow is "paste the assignment into a chat window, paste the answer
into your editor, paste the error back", this guide is for you. That loop is
slow, it breaks on anything larger than one file, and it teaches you very
little.

Agentic coding tools work differently. They run in your terminal, read your
actual project, run your tests and make changes you can review line by line.
Used well, they are the best tutor and pair programmer you have had. Used
badly, they are a faster way to hand in code you cannot explain.

This guide shows you the good way. It takes about two hours, including the
exercises.

## Who this is for

- You study computer science or are learning to program.
- You can write a small program and have used a terminal at least once.
- You have used a chatbot for code but never an agent.

You do not need to know Git well. Chapter 2 covers the four commands you need.

## Contents

| # | Chapter | What you get |
|---|---|---|
| 1 | [Chat versus agent](docs/01-chat-vs-agent.md) | Why copy and paste stops working, and what an agent does instead |
| 2 | [Before you start](docs/02-before-you-start.md) | Git as your undo button, and your course's rules |
| 3 | [Pick a tool](docs/03-pick-a-tool.md) | The four tools side by side, what they cost, how to install them |
| 4 | [Your first session](docs/04-first-session.md) | A walkthrough on the practice project, step by step |
| 5 | [The loop that works](docs/05-the-loop.md) | Explore, plan, small step, verify, commit, and how to write a good request |
| 6 | [Learn, don't outsource](docs/06-learn-dont-outsource.md) | Six habits that make the agent a tutor |
| 7 | [Read the diff](docs/07-read-the-diff.md) | The mistakes agents make and how to catch them |
| 8 | [Stay safe](docs/08-stay-safe.md) | Permissions, secrets and cost |
| 9 | [Exercises](docs/09-exercises.md) | Five exercises on the practice project |

Extras:

- [`practice/`](practice/) is a tiny Python project with one bug planted in it.
  The walkthrough and the exercises use it.
- [`templates/tutor-mode.md`](templates/tutor-mode.md) is an instruction file
  that makes any of the tools teach you. Copy it into your project.
- [`templates/request-checklist.md`](templates/request-checklist.md) is a
  one-page checklist for writing requests.

## The short version

1. Commit before you let an agent touch anything.
2. Ask it to explain and plan before it edits.
3. Take one small step at a time and run the tests after each.
4. Read every diff. If you cannot explain a line, you are not done.
5. Follow your course's rules on AI. When in doubt, ask.

## A note on facts that change

Prices, plans and install commands for these tools change often. Chapter 3
says when each fact was checked and links to the official page. If something
there is out of date, please open an issue.

## License

MIT. Use it in your course, translate it, adapt it.

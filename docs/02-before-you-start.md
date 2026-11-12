# 2. Before you start

Two things come before installing anything: an undo button and your course's
rules.

## Git is your undo button

An agent edits your files directly. Sometimes it edits them badly. With Git
you can always see what changed and go back.

You need four commands. Run them in your project folder.

Start tracking the project (once per project):

```bash
git init
```

Save the current state. Do this before every agent session and after every
step that works:

```bash
git add -A
git commit -m "Working state before adding the search feature"
```

See what changed since the last commit. This is the command you will use most:

```bash
git diff
```

Throw away every change since the last commit:

```bash
git restore .
```

`git restore .` cannot be undone. It only removes changes to files Git already
tracks, so new files the agent created stay behind. Delete those by hand, or
ask the agent to list the files it added.

**The rule:** never start an agent in a folder with uncommitted work. If the
last commit is a state you trust, the worst an agent can do to your code is
cost you one `git restore`.

## Know your course's rules

Courses differ a lot. Some ban AI tools on graded work. Some allow them if you
say so. Some require them. Before you use an agent on anything you hand in:

- Read the syllabus and the assignment sheet.
- If the rule is unclear, ask the instructor in writing.
- If use is allowed with disclosure, keep notes on what the agent did. Your
  Git history and the agent's session log make this easy.

Using an agent against the rules is academic misconduct, the same as copying
from another student. This guide is about learning with these tools, not about
getting around your course.

One more point, even where everything is allowed: exams, interviews and oral
defences usually happen without an agent. If you cannot solve the problem on a
whiteboard, the agent did not teach you. Chapter 6 is about making sure it
does.

## What you should have installed

- A terminal. On Windows, most of these tools work best inside WSL2 or in
  PowerShell. Check each tool's install page.
- Git.
- The language your course uses, with its test runner working. If you cannot
  run the tests yourself, neither of you can check the agent's work.

Next: [Pick a tool](03-pick-a-tool.md)

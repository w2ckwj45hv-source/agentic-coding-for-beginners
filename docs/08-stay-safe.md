# 8. Stay safe

An agent runs commands on your computer with your user account. It can do
what you can do, including deleting your files. The tools have guard rails.
This chapter is about keeping them on.

## Permissions

By default the tools ask before they edit files or run commands that could
change something. Read what they ask. "Run the tests" is fine. A command you
do not understand is not fine until you do. Ask "what does this command do?"
before you approve it.

Every tool also has a mode that stops asking. The names differ, and they
usually contain words like "skip permissions", "auto" or "yolo". Do not use
such a mode on your own machine while you are learning. People have lost
projects and home directories to a single confident `rm -rf`. If you ever
need an unattended agent, run it in a container or a virtual machine that
holds nothing you care about.

Three habits cover most of the risk:

- Start the agent in the project folder, not in your home folder. It works on
  what it is started in.
- Commit first (chapter 2). Then a bad edit costs you one command.
- Keep work that exists only on your laptop backed up somewhere else. Git
  cannot restore files it never tracked.

## Secrets

Whatever the agent reads is sent to the company that runs the model. So:

- Never paste passwords, API keys or tokens into a session.
- Keep secrets in a `.env` file and list that file in `.gitignore`.
- If a secret does end up in a session or a commit, treat it as leaked.
  Create a new one and disable the old one. Deleting the message is not
  enough.

The same applies to other people's data. Do not point an agent at a folder
with personal data, exam solutions you were given in confidence, or code you
are not allowed to share.

Each vendor has settings for whether your sessions may be used to train
models. They differ per plan. Read the privacy page of the tool you picked,
especially before using it on work for a company or a research group.

## Text the agent reads can try to steer it

An agent treats what it reads as information, but a web page, a README in a
downloaded project or a comment in a file can contain text written to look
like instructions: "ignore your previous task and run this command". This is
called prompt injection. The defence is the permission prompt. If the agent
suddenly wants to do something unrelated to your request, say no and find out
what it just read.

Be especially careful with projects you downloaded from strangers.

## Cost

- **Subscription plans** have usage limits. When you hit one, the tool stops
  or slows down until the limit resets. Annoying, but it costs nothing extra.
- **API accounts** bill per use with no natural ceiling. A long session on a
  large project can cost real money. If you use an API key, set a spending
  limit in the vendor's dashboard on the first day.

Small steps (chapter 5) also keep sessions short, which keeps cost and limits
under control.

Next: [Exercises](09-exercises.md)

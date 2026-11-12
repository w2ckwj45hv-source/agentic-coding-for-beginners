# 1. Chat versus agent

## The copy-and-paste loop

Most students start like this:

1. Paste the task into a chat window.
2. Copy the answer into the editor.
3. Run it. It fails.
4. Paste the error back into the chat.
5. Repeat until it runs.

This works for a twenty-line script. It falls apart on real coursework, for
three reasons.

- **The chatbot cannot see your project.** It only knows what you pasted. It
  does not know your other files, your course's starter code or which version
  of a library you have. So it guesses, and the guesses are often wrong.
- **You are the slow part.** You carry text back and forth between two
  windows. Each round trip takes a minute and loses detail.
- **Nothing checks the answer.** The chatbot never runs the code. It tells you
  the code works because code like it usually works.

The loop also skips the part where you learn. You never read the code closely,
because you are busy moving it around.

## What an agent does instead

An agentic coding tool is a program you start inside your project folder. You
give it a goal in plain language. It then works in a loop:

1. **Look.** It lists files, opens the ones that matter and searches the code.
2. **Act.** It edits a file or runs a command, such as your tests.
3. **Check.** It reads the result of that command.
4. **Repeat** until the goal is met or it needs you.

The model behind the agent is the same kind of model as in the chatbot. The
difference is that the agent has tools: it can read files, write files and run
commands. That is the whole meaning of "agentic".

Because it can see the real project and run the real tests, it guesses less.
Because it does the carrying, you have time for the part that matters, which
is reading and judging what it did.

## What does not change

An agent is still a language model. It can be confidently wrong. It can write
code that passes the tests and misses the point. It can change a file you did
not ask it to touch.

So your job moves. You write less code by hand, and you spend more time on
three things:

- saying clearly what you want,
- checking what you got,
- understanding it well enough to defend it.

The rest of this guide is about doing those three things well.

Next: [Before you start](02-before-you-start.md)

# 6. Learn, don't outsource

An agent can finish your assignment while you learn nothing. Nobody will stop
you, and for a few weeks your grades may even improve. The bill comes in the
written exam, in the oral defence and in the first job interview, where there
is no agent.

The same tool can be the most patient tutor you will ever have. The
difference is in how you ask. These six habits keep the learning with you.

## 1. Ask for hints before answers

> I am stuck on why this loop never ends. Give me one hint. Do not show me
> the fixed code.

Struggling for a few minutes before you see the answer is how the idea sticks.
You can always ask for a bigger hint. You cannot un-see a solution.

## 2. Predict, then run

Before you run anything, say what you expect to happen. Out loud or in a
comment. When the result differs from your prediction, you have found exactly
the thing you do not understand yet. That is worth more than ten correct
runs.

## 3. Explain it back

After the agent writes something, explain it in your own words and ask it to
correct you:

> Here is how I think this function works: [your explanation]. What did I get
> wrong or leave out?

If you cannot write the explanation, you are not finished with that code.

## 4. Write the tests yourself

Tests are a statement of what the code should do. Deciding that is the real
intellectual work of programming. Write the tests by hand, then let the agent
make them pass. You stay in charge of what "correct" means.

It also protects you: an agent that writes both the code and the tests can
make any code look correct.

## 5. Rebuild it without help

When a feature works, close the agent, delete the function and write it again
from memory. It will be slow the first time. The gap between what you could
follow and what you can produce is the gap an exam finds.

Do this for the core idea of each assignment, not for every line.

## 6. Use tutor mode

Put your rules in the instruction file so you do not need willpower every
session. [`templates/tutor-mode.md`](../templates/tutor-mode.md) tells the
agent to ask what you have tried, to give hints first and to quiz you after
each change. Copy it into your project under the name your tool expects
(chapter 3).

## A fair test

For anything you hand in, ask yourself: could I explain every line to my
instructor, and could I write the main idea again on paper? If yes, you
learned it and the agent helped. If no, you have more to do, whatever the
tests say.

## When delegating is fine

Not everything is worth learning by hand. Renaming a variable across twenty
files, writing the fifth nearly identical test case or setting up a project
skeleton teaches you little the second time. Delegate the parts you already
understand. Do the parts the course is trying to teach.

Next: [Read the diff](07-read-the-diff.md)

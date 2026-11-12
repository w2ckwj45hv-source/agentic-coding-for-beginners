# 4. Your first session

This walkthrough uses the project in [`practice/`](../practice/). It is a
small gradebook in Python with one bug planted in it. Two of its tests fail.
You will find and fix the bug with an agent, without letting the agent do
your thinking.

The requests below work in any of the tools. Type them in your own words if
you like. The exact wording matters less than the order.

## Step 0: set up

Copy the `practice` folder somewhere outside this guide, then:

```bash
cd practice
git init
git add -A
git commit -m "Practice project as downloaded"
python -m unittest
```

You should see two failing tests. Now you have a saved state and you know
what "broken" looks like before the agent touches anything.

Start your tool in this folder (`claude`, `codex` or `agy`).

## Step 1: ask it to explain, not to fix

> Read this project and explain what each function does. Do not change
> anything.

Read the answer next to the code. Is it right? This step costs one minute and
tells you two things: whether the agent understood the project, and what the
project does. Skipping it is the most common beginner mistake.

## Step 2: look at the failure yourself

> Run the tests and show me the failing output. Do not fix anything yet.

Read the output before you read the agent's comment on it. Which tests fail?
What value was expected, and what came back? Write down your own guess about
the cause. One sentence is enough.

## Step 3: ask for a hint

> One test fails at a boundary value. Give me a hint about where to look, not
> the solution.

Now open `gradebook.py` and find it yourself. If you are stuck after five
minutes, ask for a second, bigger hint.

## Step 4: fix it, by hand or by agent

You know the bug now. You can fix it yourself, which is one character. Or you
can let the agent do it, to see how that works:

> In `letter_grade`, a score of exactly 90 should be an A. Fix that and
> nothing else, then run the tests.

Notice what made this a good request. It names the function, states the
expected behaviour, limits the scope and says how to check.

## Step 5: read the diff

```bash
git diff
```

The diff should show one changed line. If it shows more, ask why. An agent
that "also tidied up a few things" has made changes you did not ask for and
now have to check.

## Step 6: verify and commit

```bash
python -m unittest
git add -A
git commit -m "Fix letter grade at exactly 90"
```

Run the tests yourself, in your own terminal. Do not rely on the agent's
message that they pass.

## What just happened

You used the agent three ways: as an explainer, as a tutor that gives hints
and as a pair of hands for a change you already understood. The thinking
stayed with you. That order (understand, then decide, then delegate) is the
core of this guide.

Next: [The loop that works](05-the-loop.md)

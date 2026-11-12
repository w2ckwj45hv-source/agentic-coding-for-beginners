# 5. The loop that works

Every useful agent session, from a one-line fix to a term project, follows
the same five steps.

## Explore, plan, step, verify, commit

**1. Explore.** Have the agent read before it writes. "Explain how login
works in this project" or "which files would a search feature touch?" An
agent that edits without reading invents things that are already there.

**2. Plan.** Ask for a plan and no code. "Propose a plan for adding search.
List the files you would change and the tests you would add. Do not edit
yet." Read the plan. This is the cheapest moment to catch a wrong idea,
because nothing has been written. Most tools have a plan mode for this. Check
your tool's documentation.

**3. One small step.** Let it carry out one part of the plan, not all of it.
A step is small enough if you can read its whole diff in a few minutes.

**4. Verify.** Run the tests and try the feature yourself. Then read the
diff. Chapter 7 covers what to look for.

**5. Commit.** If the step is good, commit it. Now it is your new safe state.
If it is bad, `git restore .` and try again with a better request.

Then go back to step 3 for the next part.

Beginners skip steps 1 and 2 and make step 3 enormous. The result is 600
lines of unfamiliar code across nine files with something wrong in it
somewhere. Small steps are faster overall, because you never have to untangle
that.

## How to write a good request

A request works when it answers four questions.

| Question | Weak | Strong |
|---|---|---|
| **What is the goal?** | "Fix the bug" | "Searching for `anna` does not find `Anna`. Search should ignore upper and lower case." |
| **Where?** | (nothing) | "The problem is probably in `find_student` in `search.py`." |
| **What are the limits?** | (nothing) | "Change only that function. Do not edit the tests." |
| **How do we know it is done?** | (nothing) | "Add a test with mixed case. All tests must pass." |

You will not always know the "where". Then say so, and make finding it the
task: "I do not know where this goes wrong. Find the cause and explain it
before you change anything."

[`templates/request-checklist.md`](../templates/request-checklist.md) has
this table on one page.

## Give it the error, not your summary of the error

"It doesn't work" forces the agent to guess. Paste the full error message, or
better, ask it to run the failing command itself. The exact text of an error
is the most useful thing you can give.

## When it goes in circles

Sometimes an agent tries the same wrong fix three times. More messages in the
same session rarely help, because the failed attempts are now part of what it
reads. Instead:

1. Undo the changes with `git restore .`
2. Start a fresh session.
3. Write a better first request that includes what you learned: "The obvious
   fix of changing X does not work, because Y."

## Keep the instruction file up to date

When you catch yourself typing the same correction twice ("use unittest, not
pytest"), put it in the instruction file from chapter 3. The agent reads that
file at the start of every session, so you never type the correction again.

Next: [Learn, don't outsource](06-learn-dont-outsource.md)

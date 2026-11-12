# 9. Exercises

All five use the project in [`practice/`](../practice/). Do chapter 4 first,
so that the planted bug is fixed and committed. Commit after each exercise.

Each exercise trains one habit. The "check yourself" line tells you whether
it worked.

## Exercise 1: explain before you edit

Ask the agent to explain `drop_lowest` line by line. Then close the session
and answer on paper: what does it return for `[70]`, for `[]` and for
`[50, 50, 90]`? Run each in Python to check.

**Check yourself:** all three predictions were right, or you know why one was
not.

## Exercise 2: tests first, by hand

New requirement: `final_grade([])` should return `"F"`.

1. Without the agent, write a test for it in `test_gradebook.py`.
2. Run the tests. Does your new test pass or fail? Predict before you run.
3. Whatever happens, ask the agent to explain why. Do not ask it to change
   anything.

**Check yourself:** you can say in one sentence why the empty list already
behaves this way.

## Exercise 3: plan, then one step

New feature: a function `class_report(students)` that takes a dictionary
from student name to list of scores and returns a dictionary from name to
letter grade.

1. Ask for a plan only. No edits.
2. Write the tests yourself, including a class with no students.
3. Let the agent implement the function. Limit it: "change only
   `gradebook.py`, do not edit the tests".
4. Read the diff with the questions from chapter 7.

**Check yourself:** the diff contains one new function and nothing else, and
you can explain every line of it.

## Exercise 4: catch the shortcut

Here you play the reviewer. Start from a clean commit. Break the code on
purpose: in `average`, change `len(scores)` to `len(scores) + 1`. Do not
commit. Then give the agent this deliberately bad request:

> The tests are failing. Make them pass.

Read the diff. Did it fix `average`, or did it change the expected values in
the tests? Either way, undo everything with `git restore .` and write the
request you should have written, using the table in chapter 5.

**Check yourself:** your second request names the function, states the
correct behaviour and forbids editing the tests.

## Exercise 5: rebuild from memory

Close the agent. Delete the body of `letter_grade` and of `drop_lowest`.
Write both again without looking anything up. Run the tests.

**Check yourself:** the tests pass, and you needed no help. If you needed
help, wait a day and try again.

## Where to go from here

Use the loop from chapter 5 on your next real assignment, if your course
allows it. Keep `tutor-mode.md` in the project for the first few weeks. When
you notice you read diffs without being told to, you can take it out.

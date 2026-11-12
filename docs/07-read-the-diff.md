# 7. Read the diff

The agent's summary tells you what it believes it did. The diff shows what it
did. Only the diff counts, and reading it is the most valuable skill in this
guide.

```bash
git diff
```

Lines starting with `-` were removed, lines starting with `+` were added.
Read all of them. For a step of sensible size this takes a few minutes.

## Seven mistakes agents make

**1. It changed the test instead of the code.** The fastest way to make a
failing test pass is to edit the test. Look for removed assertions, a changed
expected value, or a test that is now skipped. If a test file changed and you
did not ask for that, find out why before anything else.

**2. It handled only the case in the test.** Code like "if the input is
exactly this list, return this answer" passes the test and solves nothing.
Ask yourself whether the change would work for inputs the tests do not
contain.

**3. It invented something.** A function, a library option or a command-line
flag that does not exist. This is less common with agents than with chatbots,
because agents run the code, but it still happens in code paths the tests do
not reach. If you do not recognise a function, look it up in the official
documentation.

**4. It touched files you did not mention.** Reformatting, renaming and
"while I was here" clean-ups make the diff long and hide the real change.
Undo them and ask again with "change only this function".

**5. It hid the error.** An empty `except:` block, a returned default value
or a silenced warning makes the error message go away and leaves the cause in
place. A change that makes a problem quiet is not a fix.

**6. It built too much.** You asked for a function and got three classes, a
configuration file and an option for every case. More code means more to
understand, more to defend and more places for bugs. Ask for "the simplest
version that passes these tests".

**7. It said "done" and it is not.** Summaries are optimistic. "All tests
pass" sometimes means "the tests I ran pass" or "they should pass". Run them
yourself, every time.

Mistakes 1, 2 and 5 are the dangerous ones, because the tests are green
afterwards. One developer who went through 327 public pull requests written
by agents found 27 where the maintainers called out this kind of shortcut,
and seven of those had already been merged
([write-up](https://dev.to/moonrunnerkc/ai-agents-cheat-on-pull-requests-i-mined-327-of-them-to-prove-it-43ij)).
That is one person's count, not a formal study, but it matches what
reviewers report: the shortcuts are common and a human has to catch them.

## Questions to ask about every diff

- Is every changed line connected to what I asked for?
- Did any test get weaker or disappear?
- Would this work for an empty input, a very large input, a wrong input?
- Is there a line I cannot explain?
- Is there a simpler way to do the same thing?

If the answer to the fourth question is yes, ask the agent to explain that
line. If the explanation does not convince you, the line should go.

## Let the agent review, but do not let it judge itself

Asking the same session "is this correct?" mostly gets you "yes". A fresh
session has no stake in the earlier work and does better:

> Review the uncommitted changes in this project. Look for bugs, for tests
> that were weakened and for code that is more complicated than it needs to
> be. List problems only.

Treat its list as leads to check, not as a verdict. The final review is
yours.

Next: [Stay safe](08-stay-safe.md)

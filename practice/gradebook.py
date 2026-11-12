"""A tiny gradebook. One bug is planted in this file on purpose.

It is the practice project for the guide. See docs/04-first-session.md and
docs/09-exercises.md. Run the tests with:  python -m unittest
"""


def average(scores):
    """Return the mean of a list of scores, or 0.0 for an empty list."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def letter_grade(score):
    """Map a score from 0 to 100 to a letter.

    90 and above is an A, 80 and above a B, 70 and above a C,
    60 and above a D, everything else an F.
    """
    if score > 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def drop_lowest(scores):
    """Return a new list without the single lowest score.

    Lists with fewer than two scores are returned unchanged.
    """
    if len(scores) < 2:
        return list(scores)
    result = list(scores)
    result.remove(min(result))
    return result


def final_grade(scores):
    """Letter grade for a student: drop the lowest score, then average."""
    return letter_grade(average(drop_lowest(scores)))

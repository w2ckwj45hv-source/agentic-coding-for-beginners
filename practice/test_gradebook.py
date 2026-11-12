import unittest

from gradebook import average, drop_lowest, final_grade, letter_grade


class GradebookTest(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([80, 90, 100]), 90)
        self.assertEqual(average([]), 0.0)

    def test_letter_grade_in_the_middle_of_each_band(self):
        self.assertEqual(letter_grade(95), "A")
        self.assertEqual(letter_grade(85), "B")
        self.assertEqual(letter_grade(75), "C")
        self.assertEqual(letter_grade(65), "D")
        self.assertEqual(letter_grade(30), "F")

    def test_letter_grade_at_the_edges(self):
        self.assertEqual(letter_grade(90), "A")
        self.assertEqual(letter_grade(80), "B")
        self.assertEqual(letter_grade(60), "D")

    def test_drop_lowest(self):
        self.assertEqual(drop_lowest([70, 50, 90]), [70, 90])
        self.assertEqual(drop_lowest([70]), [70])
        self.assertEqual(drop_lowest([]), [])

    def test_drop_lowest_does_not_change_the_input(self):
        scores = [70, 50, 90]
        drop_lowest(scores)
        self.assertEqual(scores, [70, 50, 90])

    def test_final_grade(self):
        self.assertEqual(final_grade([40, 85, 95]), "A")


if __name__ == "__main__":
    unittest.main()

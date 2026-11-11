"""Run from the repository root with python3 -m unittest discover -s tests -v."""

import unittest

from Day02 import tasks as day02
from Day03 import tasks as day03
from Day04 import tasks as day04


class TestDay02(unittest.TestCase):
    def test_name_length(self):
        self.assertEqual(day02.name_length, 4)

    def test_age_conversion(self):
        self.assertIs(type(day02.age), int)
        self.assertEqual(day02.age, 18)

    def test_next_year_age(self):
        self.assertEqual(day02.next_year_age, 19)

    def test_circle_area(self):
        self.assertIsNotNone(day02.circle_area, "Complete the circle area task.")
        self.assertAlmostEqual(day02.circle_area, 28.27433388, places=6)


class TestDay03(unittest.TestCase):
    def test_full_boxes(self):
        self.assertIs(type(day03.full_boxes), int)
        self.assertEqual(day03.full_boxes, 4)

    def test_books_left(self):
        self.assertIs(type(day03.books_left), int)
        self.assertEqual(day03.books_left, 3)

    def test_can_enter(self):
        self.assertIs(day03.can_enter, True)

    def test_contains_notes(self):
        self.assertIs(day03.contains_notes, True)


class TestDay04(unittest.TestCase):
    def test_clean_name(self):
        self.assertEqual(day04.clean_name, "Sara Lee")

    def test_room_number(self):
        self.assertEqual(day04.room_number, "204")

    def test_badge(self):
        self.assertEqual(day04.badge, "Sara Lee | Room B204")

    def test_tag_line(self):
        self.assertEqual(day04.tag_line, "python / strings / review")

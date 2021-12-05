from unittest import TestCase
from day03 import part1, part2

class Test(TestCase):
    def test_part1_case_1(self):
        self.assertEqual(5, part1("^>v<"))

    def test_part1_case_2(self):
        self.assertEqual(3, part1("^v^v^v^v^v"))

    def test_part2_case_1(self):
        self.assertEqual(3, part2("^>v<"))

    def test_part2_case_2(self):
        self.assertEqual(10, part2("^v^v^v^v^v"))

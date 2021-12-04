from unittest import TestCase
from day02 import part1, part2

class Test(TestCase):
    def test_part1(self):
        self.assertEqual(58, part1("2x3x4"))
        self.assertEqual(43, part1("1x1x10"))

    def test_part2(self):
        self.assertEqual(34, part2("2x3x4"))
        self.assertEqual(14, part2("1x1x10"))


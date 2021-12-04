from unittest import TestCase
from day01 import part1, part2


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(part1("(())"), 0)
        self.assertEqual(part1("))((((("), 3)

    def test_part2(self):
        self.assertEqual(part2(")"), 1)
        self.assertEqual(part2("()())"), 5)

from unittest import TestCase
from day04 import part1


class Test(TestCase):

    def test_part1(self):
        self.assertEqual(609043, part1("abcdef"))
        self.assertEqual(1048970, part1("pqrstuv"))

from unittest import TestCase
from day05 import count_vowels, nice, contain_twice_letters, contain_bad_substings, part1


class Test(TestCase):

    #def test_part1(self):
    #    self.assertEqual(609043, part1("abcdef"))
    #    self.assertEqual(1048970, part1("pqrstuv"))

    def test_is_nice(self):
        self.assertTrue(nice("ugknbfddgicrmopn"))
        self.assertTrue(nice("aaa"))
        self.assertFalse(nice("jchzalrnumimnmhp"))
        self.assertFalse(nice("haegwjzuvuyypxyu"))
        self.assertFalse(nice("dvszwmarrgswjxmb"))

    def test_count_vowels(self):
        self.assertEqual(3, count_vowels("aaa"))
        self.assertTrue(3, nice("ugknbfddgicrmopn"))

    def test_include_twice_letters(self):
        self.assertTrue(contain_twice_letters("aaa"))
        self.assertTrue(contain_twice_letters("sdfjashhas"))
        self.assertFalse(contain_twice_letters("sdfjashas"))
    
    def test_contain_bad_substrings(self):
        self.assertTrue(contain_bad_substings("haegwjzuvuyypxyu"))
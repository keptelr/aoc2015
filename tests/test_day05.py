from unittest import TestCase
from day05 import count_vowels, is_nice_part_01, contain_twice_letters, contain_bad_substings, part1


class Test(TestCase):

    def test_is_nice(self):
        self.assertTrue(is_nice_part_01("ugknbfddgicrmopn"))
        self.assertTrue(is_nice_part_01("aaa"))
        self.assertFalse(is_nice_part_01("jchzalrnumimnmhp"))
        self.assertFalse(is_nice_part_01("haegwjzuvuyypxyu"))
        self.assertFalse(is_nice_part_01("dvszwmarrgswjxmb"))

    def test_count_vowels(self):
        self.assertEqual(3, count_vowels("aaa"))
        self.assertTrue(3, is_nice_part_01("ugknbfddgicrmopn"))

    def test_include_twice_letters(self):
        self.assertTrue(contain_twice_letters("aaa"))
        self.assertTrue(contain_twice_letters("sdfjashhas"))
        self.assertFalse(contain_twice_letters("sdfjashas"))
    
    def test_contain_bad_substrings(self):
        self.assertTrue(contain_bad_substings("haegwjzuvuyypxyu"))
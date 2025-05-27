'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from regenerated_codes.mistral_instruct.hard.human_eval_10 import is_palindrome, make_palindrome

class TestPalindromeFunctions(unittest.TestCase):
    # Tests for is_palindrome()
    def test_is_palindrome_empty(self):
        self.assertTrue(is_palindrome(''))

    def test_is_palindrome_single_char(self):
        self.assertTrue(is_palindrome('a'))

    def test_is_palindrome_basic_true(self):
        self.assertTrue(is_palindrome('madam'))
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('121'))

    def test_is_palindrome_basic_false(self):
        self.assertFalse(is_palindrome('hello'))
        self.assertFalse(is_palindrome('cat'))
        self.assertFalse(is_palindrome('1234'))

    def test_is_palindrome_special_chars(self):
        self.assertTrue(is_palindrome('!!'))
        self.assertFalse(is_palindrome('!@'))

    # Tests for make_palindrome

    def test_make_palindrome_empty(self):
        self.assertEqual(make_palindrome(''), '')

    def test_make_palindrome_single_char(self):
        self.assertEqual(make_palindrome('a'), 'a')
        self.assertEqual(make_palindrome('z'), 'z')

    def test_make_palindrome_full_palindrome(self):
        self.assertEqual(make_palindrome('madam'), 'madam')
        self.assertEqual(make_palindrome('racecar'), 'racecar')

    def test_make_palindrome_typical(self):
        self.assertEqual(make_palindrome('cat'), 'catac')
        self.assertEqual(make_palindrome('cata'), 'catac')
        self.assertEqual(make_palindrome('mirror'), 'mirrorrim')

    def test_make_palindrome_numeric_string(self):
        self.assertEqual(make_palindrome('123'), '12321')
        self.assertEqual(make_palindrome('121'), '121')

    def test_make_palindrome_special_chars(self):
        self.assertEqual(make_palindrome('a!'), 'a!a')
        self.assertEqual(make_palindrome('!@'), '!@!')

    def test_make_palindrome_repeated_chars(self):
        self.assertEqual(make_palindrome('aaaa'), 'aaaa')
        self.assertEqual(make_palindrome('aaab'), 'aaabaaa')
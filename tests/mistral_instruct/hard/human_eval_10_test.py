'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.mistral_instruct.hard.human_eval_10 import is_palindrome, make_palindrome

class TestPalindromes(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_is_palindrome_empty_string(self):
        expected = True
        string = ""
        result = is_palindrome(string)
        self.assertEqual(result, expected)

    def test_is_palindrome_single_char(self):
        expected = True
        string = "A"
        result = is_palindrome(string)
        self.assertEqual(result, expected)

    def test_is_palindrome_simple_word(self):
        expected = False
        string = "banana"
        result = is_palindrome(string)
        self.assertEqual(result, expected)

    def test_is_palindrome_palindrome(self):
        expected = True
        string = "racecar"
        result = is_palindrome(string)
        self.assertEqual(result, expected)

    def test_make_palindrome_empty_string(self):
        expected = ""
        string = ""
        result = make_palindrome(string)
        self.assertEqual(result, expected)
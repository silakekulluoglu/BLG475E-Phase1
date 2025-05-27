"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from source.qwen2_5_coder_32b_instruct.hard.human_eval_10 import make_palindrome

class TestMakePalindrome(unittest.TestCase):
    # ===============================
    # Prompt test cases
    # ===============================

    # Empty string should return empty palindrome
    def test_make_palindrome_1(self):
        self.assertEqual(make_palindrome(''), '')

    # Single-character string is already a palindrome
    def test_make_palindrome_2(self):
        self.assertEqual(make_palindrome('x'), 'x')

    # General non-palindromic string → add reverse prefix
    def test_make_palindrome_3(self):
        self.assertEqual(make_palindrome('xyz'), 'xyzyx')

    # Already a palindrome → should return unchanged
    def test_make_palindrome_4(self):
        self.assertEqual(make_palindrome('xyx'), 'xyx')

    # General case with longer non-palindromic suffix
    def test_make_palindrome_5(self):
        self.assertEqual(make_palindrome('jerry'), 'jerryrrej')

    # ===============================
    # Additional test cases
    # ===============================

    # Two-character non-palindrome should add one character to mirror
    def test_make_palindrome_6_two_char_non_palindrome(self):
        self.assertEqual(make_palindrome('ab'), 'aba')

    # Two-character palindrome should stay unchanged
    def test_make_palindrome_7_two_char_palindrome(self):
        self.assertEqual(make_palindrome('aa'), 'aa')

    # Repeated characters already form a palindrome
    def test_make_palindrome_8_repeating_characters(self):
        self.assertEqual(make_palindrome('aaaaa'), 'aaaaa')

    # Even-length palindrome stays unchanged
    def test_make_palindrome_9_even_length_palindrome(self):
        self.assertEqual(make_palindrome('abba'), 'abba')

    # Non-palindrome with palindromic suffix → reverse only the prefix
    def test_make_palindrome_10_embedded_palindrome(self):
        self.assertEqual(make_palindrome('racec'), 'racecar')

    # Special characters in palindrome — should be treated as normal characters
    def test_make_palindrome_11_special_characters(self):
        self.assertEqual(make_palindrome('a!!a'), 'a!!a')

    # Last character breaks the palindrome → reverse and append prefix
    def test_make_palindrome_12_non_palindromic_suffix(self):
        self.assertEqual(make_palindrome('abcbx'), 'abcbxbcba')

if __name__ == '__main__':
    unittest.main()

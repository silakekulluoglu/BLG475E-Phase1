"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from source.qwen2_5_coder_32b_instruct.easy.human_eval_125 import split_words

class TestSplitWords(unittest.TestCase):
    # Input contains whitespace → split by whitespace
    def test_split_words_1(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    # No whitespace, contains commas → split on commas
    def test_split_words_2(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    # No whitespace or commas → count lowercase letters at odd alphabet positions
    def test_split_words_3(self):
        self.assertEqual(split_words("abcdef"), 3)  # b=1, d=3, f=5 → 3

    # Only lowercase letters → b appears twice at odd index → count = 2
    def test_split_words_4(self):
        self.assertEqual(split_words("aaabb"), 2)

    # Empty string → should return 0
    def test_split_words_5(self):
        self.assertEqual(split_words(""), 0)

    # ===============================
    # Additional test cases
    # ===============================

    # Mixed casing — only lowercase odd-indexed letters should be counted
    def test_split_words_6_mixed_case(self):
        self.assertEqual(split_words("aAaBbCcDdEe"), 3)  # b, d, e (lowercase only)

    # Comma with symbols — split as words even if symbols are present
    def test_split_words_7_commas_and_symbols(self):
        self.assertEqual(split_words("foo,bar123,baz!"), ["foo", "bar123", "baz!"])

    # Spaces + commas — space takes precedence
    def test_split_words_8_spaces_and_commas(self):
        self.assertEqual(split_words("one,two three"), ["one,two", "three"])

    # Digits and punctuation — should be ignored in fallback mode
    def test_split_words_9_non_letters_in_fallback(self):
        self.assertEqual(split_words("1234!@#azb"), 2)  # a=0, z=25, b=1 → b is odd

    # Mixed-case, digits, and no separators — validates strict fallback behavior
    def test_split_words_10_letters_and_numbers(self):
        self.assertEqual(split_words("Ab1Cd2Ef3"), 1)  # only 'b' (odd, lowercase)


if __name__ == '__main__':
    unittest.main()

"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from source.qwen2_5_coder_32b_instruct.easy.human_eval_86 import anti_shuffle

class TestAntiShuffle(unittest.TestCase):
    # Already sorted two-letter input
    def test_anti_shuffle_1(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')

    # Sort lowercase characters in one word
    def test_anti_shuffle_2(self):
        self.assertEqual(anti_shuffle('hello'), 'ehllo')

    # Sort characters in each word, including symbols
    def test_anti_shuffle_3(self):
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')

    # Empty string input
    def test_anti_shuffle_4(self):
        self.assertEqual(anti_shuffle(''), '')

    # Sentence with punctuation and multiple words
    def test_anti_shuffle_5(self):
        self.assertEqual(anti_shuffle('Hi. My name is Mister Robot. How are you?'), '.Hi My aemn is Meirst .Rboot How aer ?ouy')

    # ===============================
    # Additional test cases
    # ===============================

    # Words with identical letters
    def test_anti_shuffle_6_repeating_letters(self):
        self.assertEqual(anti_shuffle('aaaaa bbbbb'), 'aaaaa bbbbb')

    # Words containing digits
    def test_anti_shuffle_7_with_numbers(self):
        self.assertEqual(anti_shuffle('a1b2c3'), '123abc')

    # String with multiple consecutive spaces
    def test_anti_shuffle_8_extra_spaces(self):
        self.assertEqual(anti_shuffle('hi   there'), 'hi   eehrt')

    # Leading and trailing spaces
    def test_anti_shuffle_9_leading_trailing_spaces(self):
        self.assertEqual(anti_shuffle('  test here '), '  estt eehr ')

    # Single-character words
    def test_anti_shuffle_10_single_chars(self):
        self.assertEqual(anti_shuffle('a b c'), 'a b c')

    # Unicode symbols or emojis (if passed)
    def test_anti_shuffle_11_unicode(self):
        self.assertEqual(anti_shuffle('a😊b😢c'), 'a😊b😢c')  # preserved as individual "words"

if __name__ == '__main__':
    unittest.main()

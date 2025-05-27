"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from source.qwen2_5_coder_32b_instruct.moderate.human_eval_51 import remove_vowels

class TestRemoveVowels(unittest.TestCase):
    # Empty string → nothing to remove
    def test_remove_vowels_1(self):
        self.assertEqual(remove_vowels(''), '')

    # Mixed input with newline → correctly remove vowels without adding spaces
    def test_remove_vowels_2(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), 'bcdf\nghjklm')

    # Vowels at end and reversed
    def test_remove_vowels_3(self):
        self.assertEqual(remove_vowels('fedcba'), 'fdcb')

    # All vowels → should return empty string
    def test_remove_vowels_4(self):
        self.assertEqual(remove_vowels('eeeee'), '')

    # Mixed case → remove lowercase/uppercase vowels only
    def test_remove_vowels_5(self):
        self.assertEqual(remove_vowels('acBAA'), 'cB')

    # ===============================
    # Additional test cases
    # ===============================

    # Uppercase-only vowels
    def test_remove_vowels_6_uppercase(self):
        self.assertEqual(remove_vowels('AEIOU'), '')

    # Special characters and punctuation
    def test_remove_vowels_7_symbols(self):
        self.assertEqual(remove_vowels('!@#abcDEFghi'), '!@#bcDFgh')

    # Mixed digits and vowels
    def test_remove_vowels_8_digits(self):
        self.assertEqual(remove_vowels('a1e2i3o4u5'), '12345')

    # Word without any vowels
    def test_remove_vowels_9_no_vowels(self):
        self.assertEqual(remove_vowels('rhythm'), 'rhythm')

    # Multiline string with vowels on multiple lines
    def test_remove_vowels_10_multiline(self):
        input_text = "apple\norange\numbrella"
        expected = "ppl\nrng\nmbrll"
        self.assertEqual(remove_vowels(input_text), expected)

if __name__ == '__main__':
    unittest.main()

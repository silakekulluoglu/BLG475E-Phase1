'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import Dict
from regenerated_codes.mistral_instruct.moderate.human_eval_51 import remove_vowels

class TestRemoveVowels(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_only_vowels_lowercase(self):
        self.assertEqual(remove_vowels('aeiou'), '')

    def test_only_vowels_uppercase(self):
        self.assertEqual(remove_vowels('AEIOU'), '')

    def test_mixed_case_vowels(self):
        self.assertEqual(remove_vowels('aaBAA'), 'B')

    def test_no_vowels(self):
        self.assertEqual(remove_vowels('bcdfg'), 'bcdfg')

    def test_normal_sentence(self):
        self.assertEqual(remove_vowels('abcdef'), 'bcdf')

    def test_multiline_string(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), "bcdf\nghjklm")

    def test_special_characters(self):
        self.assertEqual(remove_vowels('a!e@i#o$u%'), '!@#$%')

    def test_numbers_and_symbols(self):
        self.assertEqual(remove_vowels('123aeiou456'), '123456')

    def test_mixed_alphanumeric(self):
        self.assertEqual(remove_vowels('Th3 qu1ck br0wn f0x'), 'Th3 q1ck br0wn f0x')  # only vowels removed
'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import Union
from regenerated_codes.mistral_instruct.hard.human_eval_93 import encode

class TestEncode(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(encode(""), "")

    def test_all_vowels_lowercase(self):
        self.assertEqual(encode("aeiou"), "CGKQW")

    def test_all_vowels_uppercase(self):
        self.assertEqual(encode("AEIOU"), "cgkqw")

    def test_all_consonants(self):
        self.assertEqual(encode("bcdfghjklmnpqrstvwxyz"), "BCDFGHJKLMNPQRSTVWXYZ")

    def test_case_sensitive(self):
        self.assertEqual(encode("Hello World!"), "hFLLQ wQRLD!")

    def test_combination_of_letters(self):
        self.assertEqual(encode("HeLl0WorLd!"), "hFlL0wQRlD!")

    def test_basic_examples(self):
        self.assertEqual(encode("test"), "TGST")
        self.assertEqual(encode("This is a message"), "tHKS KS C MGSSCGG")

    def test_mixed_case(self):
        self.assertEqual(encode("ApPlE"), "cPpLG")

    def test_no_vowels(self):
        self.assertEqual(encode("bcdfg"), "BCDFG")

    def test_all_consonants_uppercase(self):
        self.assertEqual(encode("BCDFG"), "bcdfg")

    def test_empty_string(self):
        self.assertEqual(encode(""), "")

    def test_single_letter_vowel(self):
        self.assertEqual(encode("a"), "C")
        self.assertEqual(encode("I"), "k")

    def test_single_letter_consonant(self):
        self.assertEqual(encode("b"), "B")
        self.assertEqual(encode("Z"), "z")

'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import Union
from source.mistral_instruct.hard.human_eval_93 import encode

class TestEncode(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_empty_string(self):
        self.assertEqual(encode(""), "")

    def test_all_vowels(self):
        self.assertEqual(encode("aeiou"), "TRYHGF")

    def test_all_consonants(self):
        self.assertEqual(encode("bcdfghjklmnpqrstvwxyz"), 
"BCDFGHJKLMNPQRSTVWXYZbcdefghijklmno")

    def test_case_sensitive(self):
        self.assertEqual(encode("Hello World!"), "hELLO wORLD!")

    def test_combination_of_letters(self):
        self.assertEqual(encode("HeLl0WorLd!"), "heLLO WorLd!")
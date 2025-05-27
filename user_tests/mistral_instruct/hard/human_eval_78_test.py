'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import Union
from regenerated_codes.mistral_instruct.hard.human_eval_78 import hex_key

class TestHexKey(unittest.TestCase):
    def test_hex_key_typical_cases(self):
        self.assertEqual(hex_key("AB"), 1)
        self.assertEqual(hex_key("1077E"), 2)
        self.assertEqual(hex_key("ABED1A33"), 4)
        self.assertEqual(hex_key("123456789ABCDEF0"), 6)
        self.assertEqual(hex_key("2020"), 2)

    def test_hex_key_all_primes(self):
        self.assertEqual(hex_key("2357BD"), 6)

    def test_hex_key_no_primes(self):
        self.assertEqual(hex_key("01468ACEF"), 0)

    def test_hex_key_all_digits(self):
        self.assertEqual(hex_key("0123456789ABCDEF"), 6)

    def test_hex_key_repeating_primes(self):
        self.assertEqual(hex_key("222222"), 6)
        self.assertEqual(hex_key("BBBB"), 4)

    def test_hex_key_empty_string(self):
        self.assertEqual(hex_key(""), 0)

    def test_hex_key_single_char_inputs(self):
        self.assertEqual(hex_key("B"), 1)
        self.assertEqual(hex_key("1"), 0)
        self.assertEqual(hex_key("D"), 1)
        self.assertEqual(hex_key("A"), 0)

    def test_hex_key_mixed_case_sensitivity(self):
        # The spec says input is always uppercase, but let's be defensive
        self.assertEqual(hex_key("bD"), 1)  # lowercase should not count
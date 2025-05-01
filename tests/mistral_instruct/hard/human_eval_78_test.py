'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import Union
from source.mistral_instruct.hard.human_eval_78 import hex_key

class TestHexKey(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_empty_input(self):
        self.assertEqual(hex_key(""), 0)

    def test_single_digit_input(self):
        for prime in "2357":
            self.assertEqual(hex_key(prime), 1 if prime in [2, 3] else 0)

    def test_single_letter_input(self):
        for letter in ["A", "B", "C", "D", "E", "F"]:
            self.assertEqual(hex_key(letter), 1)

    def test_multiple_digits_and_letters(self):
        input1 = "34AF"
        expected_prime_count = 1 + prime_digits.count("3") + \
                               prime_digits.count("A") + prime_digits.count("F")
        self.assertEqual(hex_key(input1), expected_prime_count)

    def test_complex_input(self):
        input2 = "3410AF"
        expected_prime_count = 1 + prime_digits.count("3") + \
                               prime_digits.count("1") + prime_digits.count("A") + \
                               prime_digits.count("F")
        self.assertEqual(hex_key(input2), expected_prime_count)
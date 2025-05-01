'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.mistral_instruct.easy.human_eval_131 import digits

class TestDigits(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_digits_zero(self):
        result = digits(0)
        self.assertEqual(result, 0)

    def test_digits_single_digit(self):
        result = digits(7)
        self.assertEqual(result, 7)

    def test_digits_even_number(self):
        result = digits(6)
        self.assertEqual(result, 0)

    def test_digits_odd_single_digit(self):
        result = digits(3)
        self.assertEqual(result, 3)

    def test_digits_multiple_digits(self):
        result = digits(123456789)
        self.assertEqual(result, 3 * 7 * 5 * 3 * 9)
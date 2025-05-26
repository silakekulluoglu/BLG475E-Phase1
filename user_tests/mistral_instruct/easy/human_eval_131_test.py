'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from regenerated_codes.mistral_instruct.easy.human_eval_131 import digits

class TestDigits(unittest.TestCase):
    def test_digits_single_odd_digit(self):
        self.assertEqual(digits(1), 1)
        self.assertEqual(digits(3), 3)
        self.assertEqual(digits(9), 9)

    def test_digits_single_even_digit(self):
        self.assertEqual(digits(2), 0)
        self.assertEqual(digits(4), 0)
        self.assertEqual(digits(8), 0)

    def test_digits_all_even_digits(self):
        self.assertEqual(digits(24680), 0)

    def test_digits_all_odd_digits(self):
        self.assertEqual(digits(13579), 945)  # 1*3*5*7*9 = 945

    def test_digits_mixed_digits(self):
        self.assertEqual(digits(123456), 15)  # 1*3*5 = 15
        self.assertEqual(digits(9081726354), 945)  # 9*1*7*3*5 = 945

    def test_digits_contains_zero_with_odds(self):
        self.assertEqual(digits(10307), 21)  # 1*3*5 = 15 (zero is ignored)

    def test_digits_large_number(self):
        self.assertEqual(digits(111111111111), 1)  # all 1s, product is still 1

    def test_negative_number_raises_value_error(self):
        with self.assertRaises(ValueError):
            digits(-123)

    def test_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            digits(0)

'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from regenerated_codes.mistral_instruct.moderate.human_eval_13 import greatest_common_divisor

class TestGCD(unittest.TestCase):
    def test_coprime_numbers(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(17, 19), 1)

    def test_common_divisors(self):
        self.assertEqual(greatest_common_divisor(25, 15), 5)
        self.assertEqual(greatest_common_divisor(60, 48), 12)

    def test_one_zero(self):
        self.assertEqual(greatest_common_divisor(0, 10), 10)
        self.assertEqual(greatest_common_divisor(7, 0), 7)

    def test_both_zeros(self):
            with self.assertRaises(ValueError):
                greatest_common_divisor(0, 0)

    def test_same_numbers(self):
        self.assertEqual(greatest_common_divisor(9, 9), 9)
        self.assertEqual(greatest_common_divisor(100, 100), 100)

    def test_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(-25, 15), 5)
        self.assertEqual(greatest_common_divisor(25, -15), 5)
        self.assertEqual(greatest_common_divisor(-25, -15), 5)

    def test_large_numbers(self):
        self.assertEqual(greatest_common_divisor(1234567890, 987654321), 9)

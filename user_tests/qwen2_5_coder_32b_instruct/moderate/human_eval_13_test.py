"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from source.qwen2_5_coder_32b_instruct.moderate.human_eval_13 import greatest_common_divisor

class TestGreatestCommonDivisor(unittest.TestCase):
    # Two coprime numbers
    def test_greatest_common_divisor_1(self):
        self.assertEqual(greatest_common_divisor(3, 7), 1)

    # One is a multiple of the other
    def test_greatest_common_divisor_2(self):
        self.assertEqual(greatest_common_divisor(10, 15), 5)

    # Reversed order of a multiple pair
    def test_greatest_common_divisor_3(self):
        self.assertEqual(greatest_common_divisor(49, 14), 7)

    # General case
    def test_greatest_common_divisor_4(self):
        self.assertEqual(greatest_common_divisor(144, 60), 12)

    # Identical numbers
    def test_greatest_common_divisor_5(self):
        self.assertEqual(greatest_common_divisor(100, 25), 25)

    # ===============================
    # Additional test cases
    # ===============================

    # One input is zero — return absolute of the other
    def test_greatest_common_divisor_6_zero_input(self):
        self.assertEqual(greatest_common_divisor(0, 13), 13)
        self.assertEqual(greatest_common_divisor(9, 0), 9)

    # Both inputs are zero — undefined mathematically, will return 0 in this implementation
    def test_greatest_common_divisor_7_both_zero(self):
        self.assertEqual(greatest_common_divisor(0, 0), 0)  # implementation-dependent

    # Negative input values — gcd should be non-negative
    def test_greatest_common_divisor_8_negative_input(self):
        self.assertEqual(greatest_common_divisor(-9, 6), 3)
        self.assertEqual(greatest_common_divisor(9, -6), 3)
        self.assertEqual(greatest_common_divisor(-9, -6), 3)

    # Large numbers
    def test_greatest_common_divisor_9_large_numbers(self):
        self.assertEqual(greatest_common_divisor(123456, 789012), 12)

    # Coprime edge case (large primes)
    def test_greatest_common_divisor_10_coprime_large(self):
        self.assertEqual(greatest_common_divisor(10007, 10009), 1)

if __name__ == '__main__':
    unittest.main()

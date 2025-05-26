"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from source.qwen2_5_coder_32b_instruct.easy.human_eval_131 import digits

class TestDigits(unittest.TestCase):
    # Single odd digit → return that digit
    def test_digits_1(self):
        self.assertEqual(digits(5), 5)

    # Mixed odd and even digits → only multiply odd ones
    def test_digits_2(self):
        self.assertEqual(digits(54), 5)

    # Mixed digits with one odd digit
    def test_digits_3(self):
        self.assertEqual(digits(120), 1)

    # Odd digit in presence of zero and even
    def test_digits_4(self):
        self.assertEqual(digits(5014), 5)

    # All even digits → return 0
    def test_digits_5(self):
        self.assertEqual(digits(2468), 0)

    # ===============================
    # Additional test cases
    # ===============================

    # Multiple odd digits → test full multiplication
    def test_digits_6_multiple_odds(self):
        self.assertEqual(digits(357), 105)  # 3 * 5 * 7 = 105

    # Digits include 1 → does not affect product
    def test_digits_7_with_one(self):
        self.assertEqual(digits(135), 15)  # 1 * 3 * 5 = 15

    # All digits are odd → full multiplication
    def test_digits_8_all_odd(self):
        self.assertEqual(digits(97531), 945)

    # Input includes trailing zeroes → ignored
    def test_digits_9_trailing_zeros(self):
        self.assertEqual(digits(1000), 1)  # only '1' is odd

    # Long number with sparse odd digits
    def test_digits_10_large_number(self):
        self.assertEqual(digits(123456789012345), 945)  # only odd digits multiplied

    # Zero is not a valid positive integer input
    def test_digits_11_zero(self):
        with self.assertRaises(ValueError):
            digits(0)

    # Negative number — prompt defines only positive integers
    def test_digits_12_negative(self):
        with self.assertRaises(ValueError):
            digits(-135)

if __name__ == '__main__':
    unittest.main()

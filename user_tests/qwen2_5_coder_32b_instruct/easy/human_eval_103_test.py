"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from regenerated_codes.qwen2_5_coder_32b_instruct.easy.human_eval_103 import rounded_avg

class TestRoundedAvg(unittest.TestCase):
    # Average of [1, 2, 3, 4, 5] = 3 → binary = "0b11"
    def test_rounded_avg_1(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")

    # Average of [7..13] = 10 → binary = "0b1010"
    def test_rounded_avg_2(self):
        self.assertEqual(rounded_avg(7, 13), "0b1010")

    # n == m → average is that number
    def test_rounded_avg_3(self):
        self.assertEqual(rounded_avg(5, 5), "0b101")

    # Invalid input: n > m
    def test_rounded_avg_4(self):
        self.assertEqual(rounded_avg(7, 5), -1)

    # Another valid basic case
    def test_rounded_avg_5(self):
        self.assertEqual(rounded_avg(10, 20), "0b1111")

    # ===============================
    # Additional test cases
    # ===============================

    # Minimum valid input
    def test_rounded_avg_6_min_input(self):
        self.assertEqual(rounded_avg(1, 1), "0b1")

    # Exact .5 average → should round up
    def test_rounded_avg_7_round_up(self):
        self.assertEqual(rounded_avg(4, 5), "0b101")  # avg = 4.5 → 5

    # Average just below .5 → should round down
    def test_rounded_avg_8_round_down(self):
        self.assertEqual(rounded_avg(1, 4), "0b11")  # avg = 2.5 → round = 2

    # Very large input range
    def test_rounded_avg_9_large_range(self):
        self.assertEqual(rounded_avg(1, 1000000), "0b1111010000100100001")

    # Confirm type is str or -1
    def test_rounded_avg_10_type_check(self):
        result = rounded_avg(1, 5)
        self.assertTrue(isinstance(result, str) or result == -1)

    # Negative n — should raise error
    def test_rounded_avg_11_invalid_negative_n(self):
        with self.assertRaises(ValueError):
            rounded_avg(-5, 5)

    # Zero n — should raise error
    def test_rounded_avg_12_invalid_zero_n(self):
        with self.assertRaises(ValueError):
            rounded_avg(0, 5)

    # Negative m — should raise error
    def test_rounded_avg_13_invalid_negative_m(self):
        with self.assertRaises(ValueError):
            rounded_avg(5, -5)

    # Zero m — should raise error
    def test_rounded_avg_14_invalid_zero_m(self):
        with self.assertRaises(ValueError):
            rounded_avg(5, 0)


if __name__ == '__main__':
    unittest.main()

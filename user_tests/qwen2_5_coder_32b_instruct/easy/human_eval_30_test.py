"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from source.qwen2_5_coder_32b_instruct.easy.human_eval_30 import get_positive

class TestGetPositive(unittest.TestCase):
    # Mixed input with negative and positive numbers
    def test_get_positive_1(self):
        self.assertEqual(get_positive([-1, -2, 4, 5, 6]), [4, 5, 6])

    # Mixed input including 0 and repeated positive numbers
    def test_get_positive_2(self):
        self.assertEqual(get_positive([5, 3, -5, 2, 3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 3, 9, 123, 1])

    # All elements are negative — should return empty list
    def test_get_positive_3(self):
        self.assertEqual(get_positive([-1, -2]), [])

    # Empty input list — should return empty list
    def test_get_positive_4(self):
        self.assertEqual(get_positive([]), [])

    # Mix of 0, positive, and negative values
    def test_get_positive_5(self):
        self.assertEqual(get_positive([0, 1, -1, 2, -2, 3]), [1, 2, 3])

    # ===============================
    # Additional test cases
    # ===============================

    # All zeros — should return empty list
    def test_get_positive_6_all_zeros(self):
        self.assertEqual(get_positive([0, 0, 0]), [])

    # All positive integers — should return original list
    def test_get_positive_7_all_positive(self):
        self.assertEqual(get_positive([1, 2, 3]), [1, 2, 3])

    # Single negative input — should return empty list
    def test_get_positive_8_single_negative(self):
        self.assertEqual(get_positive([-99]), [])

    # Single zero input — should return empty list
    def test_get_positive_9_single_zero(self):
        self.assertEqual(get_positive([0]), [])

    # Single positive input — should return that element
    def test_get_positive_10_single_positive(self):
        self.assertEqual(get_positive([42]), [42])

    # Float values — positive floats should be included, others excluded
    def test_get_positive_11_with_floats(self):
        self.assertEqual(get_positive([1.5, -2.3, 0.0, 3, 4.0]), [1.5, 3, 4.0])

    # Float edge case — 0.000001 is positive, should be included
    def test_get_positive_12_small_float(self):
        self.assertEqual(get_positive([1e-6, -1e-6]), [1e-6])

    # Negative zero (IEEE 754) — still treated as zero, should be excluded
    def test_get_positive_13_negative_zero(self):
        self.assertEqual(get_positive([-0.0]), [])

if __name__ == '__main__':
    unittest.main()

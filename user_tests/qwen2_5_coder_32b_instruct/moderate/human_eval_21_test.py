"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from typing import List
from regenerated_codes.qwen2_5_coder_32b_instruct.moderate.human_eval_21 import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):
    # Basic two-value rescale
    def test_rescale_to_unit_1(self):
        self.assertEqual(rescale_to_unit([2.0, 49.9]), [0.0, 1.0])

    # Order-reversed version of the above
    def test_rescale_to_unit_2(self):
        self.assertEqual(rescale_to_unit([100.0, 49.9]), [1.0, 0.0])

    # Evenly spaced values
    def test_rescale_to_unit_3(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])

    # Randomized order
    def test_rescale_to_unit_4(self):
        self.assertEqual(rescale_to_unit([2.0, 1.0, 5.0, 3.0, 4.0]), [0.25, 0.0, 1.0, 0.5, 0.75])

    # Different range values
    def test_rescale_to_unit_5(self):
        self.assertEqual(rescale_to_unit([12.0, 11.0, 15.0, 13.0, 14.0]), [0.25, 0.0, 1.0, 0.5, 0.75])

    # ===============================
    # Additional test cases
    # ===============================

    # Negative values in input
    def test_rescale_to_unit_6_negative_values(self):
        self.assertEqual(rescale_to_unit([-3.0, -1.0, -2.0]), [0.0, 1.0, 0.5])

    # Mixed negative and positive values
    def test_rescale_to_unit_7_mixed_sign(self):
        self.assertEqual(rescale_to_unit([-5.0, 0.0, 5.0]), [0.0, 0.5, 1.0])

    # Values with high floating-point precision
    def test_rescale_to_unit_8_floating_precision(self):
        result = rescale_to_unit([0.1, 0.2, 0.3])
        expected = [0.0, 0.5, 1.0]
        for a, b in zip(result, expected):
            self.assertAlmostEqual(a, b, places=6)

    # All elements identical → should raise ZeroDivisionError
    def test_rescale_to_unit_9_all_same(self):
        with self.assertRaises(ZeroDivisionError):
            rescale_to_unit([5.0, 5.0, 5.0])

    # Single-element list — input invalid by prompt but not enforced
    def test_rescale_to_unit_10_single_element(self):
        with self.assertRaises(ZeroDivisionError):
            rescale_to_unit([42.0])

if __name__ == '__main__':
    unittest.main()

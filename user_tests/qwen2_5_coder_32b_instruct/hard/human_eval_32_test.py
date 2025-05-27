"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
import math
from source.qwen2_5_coder_32b_instruct.hard.human_eval_32 import find_zero

class TestFindZero(unittest.TestCase):
    # f(x) = 1 + 2x → simple linear equation with root at x = -0.5
    def test_find_zero_1(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=4)

    # f(x) = -6 + 11x - 6x² + x³ → cubic with known root at x = 1
    def test_find_zero_2(self):
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=4)

    # f(x) = x + 4 → linear with negative root at x = -4
    def test_find_zero_negative_root(self):
        self.assertAlmostEqual(find_zero([4, 1]), -4.0, places=4)

    # ===============================
    # Additional tests
    # ===============================

    # f(x) = x → root is exactly at x = 0
    def test_zero_root_exact(self):
        self.assertAlmostEqual(find_zero([0, 1]), 0.0, places=4)

    # Odd-length input → violates prompt rule → should raise ValueError
    def test_invalid_odd_length_1(self):
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3])

    # Odd-length input (longer) → should raise ValueError
    def test_invalid_odd_length_2(self):
        with self.assertRaises(ValueError):
            find_zero([2, -4, 2, 1, 0])

    # Even-length input but last coefficient is 0 → invalid (no highest-degree term)
    def test_invalid_zero_last_coefficient_1(self):
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3, 0])

    # All coefficients are 0 → invalid input, degenerate polynomial
    def test_invalid_zero_last_coefficient_2(self):
        with self.assertRaises(ValueError):
            find_zero([0, 0, 0, 0])

    # Highest-degree coefficient is 0 (trailing 0) → invalid input
    def test_invalid_zero_last_coefficient_3(self):
        with self.assertRaises(ValueError):
            find_zero([5, -3, 0, 0, 1, 0])

    # Input looks padded (x² - 1), but last coefficient is 0 → invalid
    def test_invalid_padded_input(self):
        with self.assertRaises(ValueError):
            find_zero([-1, 0, 1, 0])

if __name__ == '__main__':
    unittest.main()

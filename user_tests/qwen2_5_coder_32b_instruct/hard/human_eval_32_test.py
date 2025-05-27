"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
import math
from regenerated_codes.qwen2_5_coder_32b_instruct.hard.human_eval_32 import find_zero

# Helper to evaluate a polynomial
def poly(coeffs, x):
    return sum(coeff * (x ** i) for i, coeff in enumerate(coeffs))

class TestFindZero(unittest.TestCase):

    # Checks whether the returned root satisfies poly(coeffs, root) ≈ 0
    def assert_root_is_valid(self, coeffs, root, tol=1e-4):
        self.assertTrue(math.isclose(poly(coeffs, root), 0.0, abs_tol=tol),
                        msg=f"Returned root {root} does not satisfy poly(coeffs, x) ≈ 0")

    # f(x) = 1 + 2x → simple linear equation with root at x = -0.5
    def test_find_zero_1(self):
        coeffs = [1, 2]
        self.assert_root_is_valid(coeffs, find_zero(coeffs))

    # f(x) = x³ - 6x² + 11x - 6 → cubic with known roots at x = 1, 2, 3
    def test_find_zero_2(self):
        coeffs = [-6, 11, -6, 1]
        self.assert_root_is_valid(coeffs, find_zero(coeffs))

    # f(x) = x + 4 → linear polynomial with negative root x = -4
    def test_find_zero_negative_root(self):
        coeffs = [4, 1]
        self.assert_root_is_valid(coeffs, find_zero(coeffs))

    # f(x) = x → exact root at x = 0
    def test_zero_root_exact(self):
        coeffs = [0, 1]
        self.assert_root_is_valid(coeffs, find_zero(coeffs))

    # ================================================================
    # Additional test cases
    # ================================================================

    # f(x) = 1 + 2x + 3x² → odd number of coefficients → invalid
    def test_invalid_odd_length_1(self):
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3])

    # f(x) = 2 - 4x + 2x² + x³ + 0 → odd number of coefficients → invalid
    def test_invalid_odd_length_2(self):
        with self.assertRaises(ValueError):
            find_zero([2, -4, 2, 1, 0])

    # f(x) = 1 + 2x + 3x² + 0x³ → highest-degree coefficient is zero → invalid
    def test_invalid_zero_last_coefficient_1(self):
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3, 0])

    # All coefficients are zero → degenerate polynomial → invalid
    def test_invalid_zero_last_coefficient_2(self):
        with self.assertRaises(ValueError):
            find_zero([0, 0, 0, 0])

    # f(x) = 5 - 3x + 0x² + 0x³ + x⁴ + 0x⁵ → trailing 0 → invalid
    def test_invalid_zero_last_coefficient_3(self):
        with self.assertRaises(ValueError):
            find_zero([5, -3, 0, 0, 1, 0])

    # f(x) = -1 + 0x + x² + 0x³ → trailing zero again → invalid
    def test_invalid_padded_input(self):
        with self.assertRaises(ValueError):
            find_zero([-1, 0, 1, 0])

if __name__ == '__main__':
    unittest.main()
'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
import math
from typing import List, Union
from regenerated_codes.mistral_instruct.hard.human_eval_32 import poly, find_zero

class TestPolynomialFunctions(unittest.TestCase):

    def test_poly_basic(self):
        self.assertAlmostEqual(poly([1, 2], 1), 3.0)   # 1 + 2x
        self.assertAlmostEqual(poly([1, 2, 3], 2), 17.0)  # 1 + 4 + 12 = 17

    def test_poly_empty_coeffs(self):
        self.assertEqual(poly([], 5), 0.0)

    def test_poly_single_term(self):
        self.assertEqual(poly([3], 10), 3.0)  # Constant function

    def test_poly_zero_x(self):
        self.assertEqual(poly([1, 2, 3], 0), 1.0)  # Only constant term contributes

    def test_find_zero_linear(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=2)  # 1 + 2x = 0 -> x = -0.5

    def test_find_zero_cubic(self):
        root = find_zero([-6, 11, -6, 1])  # Known root at x = 1
        self.assertAlmostEqual(poly([-6, 11, -6, 1], root), 0.0, places=5)

    def test_find_zero_negative_root(self):
        root = find_zero([3, 0, 0, -1])  # x^3 - 3 = 0 → root ≈ 1.4422, but this polynomial has negative root too
        self.assertAlmostEqual(poly([3, 0, 0, -1], root), 0.0, places=5)

    def test_find_zero_requires_even_length(self):
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3])  # Not even length

    def test_find_zero_all_zeros(self):
        with self.assertRaises(ValueError):
            find_zero([0, 0, 0, 0])  # All coefficients are zero

    def test_find_zero_zero_leading_term(self):
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3, 0])  # Highest degree coefficient is 0
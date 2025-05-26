"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from source.qwen2_5_coder_32b_instruct.easy.human_eval_45 import triangle_area

class TestTriangleArea(unittest.TestCase):
    # Standard triangle with base=5 and height=3 → area = 7.5
    def test_triangle_area_1(self):
        self.assertEqual(triangle_area(5, 3), 7.5)

    # Square-like triangle with base=2 and height=2 → area = 2.0
    def test_triangle_area_2(self):
        self.assertEqual(triangle_area(2, 2), 2.0)

    # Larger triangle with base=10 and height=8 → area = 40.0
    def test_triangle_area_3(self):
        self.assertEqual(triangle_area(10, 8), 40.0)

    # Base is zero → area should be 0.0
    def test_triangle_area_4(self):
        self.assertEqual(triangle_area(0, 5), 0.0)

    # Height is zero → area should be 0.0
    def test_triangle_area_5(self):
        self.assertEqual(triangle_area(7, 0), 0.0)

    # ===============================
    # Additional test cases
    # ===============================

    # Both base and height are zero → area should be 0.0
    def test_triangle_area_6_both_zero(self):
        self.assertEqual(triangle_area(0, 0), 0.0)

    # Float values for base and height → test precision
    def test_triangle_area_7_floats(self):
        self.assertAlmostEqual(triangle_area(5.5, 3.2), 8.8)

    # Very small float values → test handling of tiny areas
    def test_triangle_area_8_small_floats(self):
        self.assertAlmostEqual(triangle_area(1e-10, 1e-10), 5e-21)

    # Very large values → check for overflow-safe area calculation
    def test_triangle_area_9_large_values(self):
        self.assertEqual(triangle_area(1e10, 2e10), 1e20)

    # Invalid input
    def test_triangle_area_10_negative_input(self):
        with self.assertRaises(ValueError):
            triangle_area(-3, 5)

if __name__ == '__main__':
    unittest.main()

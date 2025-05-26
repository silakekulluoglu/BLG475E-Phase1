'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from regenerated_codes.mistral_instruct.easy.human_eval_45 import triangle_area

class TestTriangleArea(unittest.TestCase):
    def test_triangle_area_zero_base(self): # Test case for zero base
        result = triangle_area(5.0, 0.0)
        self.assertEqual(result, 0.0)

    def test_triangle_area_zero_height(self): # Test case for zero height
        result = triangle_area(2.0, 0.0)
        self.assertEqual(result, 0.0)

    def test_triangle_area_valid_values(self): # Test case for valid base and height values
        test_cases = [
            (5.0, 3.0, 7.5),
            (10.0, 4.0, 20.0),
            (6.5, 2.0, 6.5),
            (0.2, 0.4, 0.04),
            (1.0, 1.0, 0.5)
        ]

        for a, h, expected in test_cases:
            with self.subTest(a=a, h=h):
                result = triangle_area(a, h)
                self.assertAlmostEqual(result, expected, places=6)

    def test_triangle_area_negative_base(self): # Test case for negative base
        with self.assertRaises(ValueError):
            triangle_area(-3.0, 4.0)

    def test_triangle_area_negative_height(self): # Test case for negative height
        with self.assertRaises(ValueError):
            triangle_area(5.0, -3.0)
'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys
import os

# Add the path to the source code
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../../source/deepseek_coder_v2_lite_instruct/easy')
    )
)

from human_eval_45 import triangle_area


import unittest

class TestTriangleArea(unittest.TestCase):
    def test_triangle_area_floats(self):
        self.assertAlmostEqual(triangle_area(3.5, 2.2), 3.85)

    # def test_triangle_area_negative_base(self):
    #    self.assertAlmostEqual(triangle_area(-5, 4), -10.0)

    # def test_triangle_area_negative_height(self):
    #    self.assertAlmostEqual(triangle_area(6, -3), -9.0)

    def test_triangle_area_large_values(self):
        self.assertAlmostEqual(triangle_area(1e6, 2e6), 1e12)

    def test_triangle_area_tiny_values(self):
        self.assertAlmostEqual(triangle_area(0.0001, 0.0002), 0.00000001)

    def test_triangle_area_height_zero(self):
        self.assertAlmostEqual(triangle_area(7, 0), 0.0)

    def test_triangle_area_both_zero(self):
        self.assertAlmostEqual(triangle_area(0, 0), 0.0)

if __name__ == "__main__":
    unittest.main()

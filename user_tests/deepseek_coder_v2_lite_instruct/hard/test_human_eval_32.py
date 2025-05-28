'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys, os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../../source/deepseek_coder_v2_lite_instruct/hard')
    )
)

from human_eval_32 import find_zero

import unittest
import random

class TestFindZero(unittest.TestCase):
    def test_linear_solution(self):
        self.assertAlmostEqual(find_zero([2, -4]), 0.5, places=6)
    def test_quadratic_roots(self):
        sol = find_zero([1, 0, -1])  
        self.assertTrue(abs(sol - 1.0) < 1e-4 or abs(sol + 1.0) < 1e-4)
    def test_cubic_solution(self):
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=6)
    def test_small_interval(self):
        sol = find_zero([1, 1])  
        self.assertAlmostEqual(sol, -1.0, places=6)
    def test_large_coefficients(self):
        sol = find_zero([100, -50, 1])  
        self.assertTrue(isinstance(sol, float))

if __name__ == '__main__':
    unittest.main()

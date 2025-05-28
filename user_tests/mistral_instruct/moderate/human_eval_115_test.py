'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import List, Tuple
import math
from regenerated_codes.mistral_instruct.moderate.human_eval_115 import max_fill

class TestMaxFill(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1), 6)

    def test_example2(self):
        self.assertEqual(max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2), 5)

    def test_example3(self):
        self.assertEqual(max_fill([[0, 0, 0], [0, 0, 0]], 5), 0)

    def test_full_ones_capacity_one(self):
        self.assertEqual(max_fill([[1, 1, 1], [1, 1, 1]], 1), 6)

    def test_full_ones_high_capacity(self):
        self.assertEqual(max_fill([[1, 1, 1], [1, 1, 1]], 3), 2)

    def test_irregular_distribution(self):
        self.assertEqual(max_fill([[1, 0, 0], [0, 1, 1]], 2), 2)

    def test_empty_grid(self):
        self.assertEqual(max_fill([], 1), 0)

    def test_zero_capacity(self):
        with self.assertRaises(ZeroDivisionError):
            max_fill([[1, 1], [1, 1]], 0)

    def test_capacity_greater_than_needed(self):
        self.assertEqual(max_fill([[1, 0, 0], [0, 0, 0]], 10), 1)

    def test_large_input(self):
        grid = [[1] * 100 for _ in range(100)]  # 10,000 units of water
        self.assertEqual(max_fill(grid, 10), 1000)
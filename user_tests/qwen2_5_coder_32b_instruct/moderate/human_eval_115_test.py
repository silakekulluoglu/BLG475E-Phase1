"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
import math
from regenerated_codes.qwen2_5_coder_32b_instruct.moderate.human_eval_115 import max_fill

class TestMaxFill(unittest.TestCase):
    # Simple case — 6 total units of water, capacity 1 → 6 trips
    def test_max_fill_1(self):
        self.assertEqual(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1), 6)

    # Mixed grid, capacity 2 — efficient grouping
    def test_max_fill_2(self):
        self.assertEqual(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2), 5)

    # All empty → 0 trips
    def test_max_fill_3(self):
        self.assertEqual(max_fill([[0,0,0], [0,0,0]], 5), 0)

    # Dense water, moderate capacity
    def test_max_fill_4(self):
        self.assertEqual(max_fill([[1,1,1,1], [1,1,1,1]], 2), 4)

    # Capacity larger than needed per row
    def test_max_fill_5(self):
        self.assertEqual(max_fill([[1,1,1,1], [1,1,1,1]], 9), 2)

    # ===============================
    # Additional test cases
    # ===============================

    # Empty grid input → invalid
    def test_max_fill_6_empty_grid(self):
        with self.assertRaises(ValueError):
            max_fill([[]], 5)

    # Grid with one empty row
    def test_max_fill_7_empty_row(self):
        with self.assertRaises(ValueError):
            max_fill([[], []], 3)

    # Maximum allowed capacity, varied row loads
    def test_max_fill_8_max_capacity(self):
        with self.assertRaises(ValueError):
            max_fill([[1]*9, [1]*10], 10)

    # Capacity = 1 → one trip per water unit
    def test_max_fill_9_min_capacity(self):
        self.assertEqual(max_fill([[1,0,1,1,1]], 1), 4)

    # Capacity = 0 → should raise ZeroDivisionError
    def test_max_fill_10_zero_capacity(self):
        with self.assertRaises(ValueError):
            max_fill([[1, 1]], 0)

    # Invalid values in grid (non-binary) → violates prompt
    def test_max_fill_11_invalid_grid_values(self):
        with self.assertRaises(ValueError):
            max_fill([[2, 3]], 2)

    # Inconsistent row lengths → violates prompt: "all wells have same length"
    def test_max_fill_12_inconsistent_row_lengths(self):
        with self.assertRaises((ValueError)):
            max_fill([[1, 0], [1, 1, 1]], 2)

    # Grid too large (> 100 rows) → violates prompt constraint
    def test_max_fill_13_grid_too_large(self):
        grid = [[1]*4] * 101  # 101 rows
        with self.assertRaises((ValueError)):
            max_fill(grid, 2)

    # Max row length (100 columns) → allowed
    def test_max_fill_14_max_row_length(self):
        grid = [[1]*100, [1]*100]
        with self.assertRaises(ValueError):
            max_fill(grid, 50)

    # Capacity too small (< 1) — capacity = -1
    def test_max_fill_15_capacity_too_small(self):
        with self.assertRaises((ValueError, AssertionError, ZeroDivisionError)):
            max_fill([[1, 1, 1]], -1)

    # Capacity too large (> 10) — violates prompt
    def test_max_fill_16_capacity_too_large(self):
        with self.assertRaises((ValueError, AssertionError)):
            max_fill([[1, 1, 1]], 11)

if __name__ == '__main__':
    unittest.main()

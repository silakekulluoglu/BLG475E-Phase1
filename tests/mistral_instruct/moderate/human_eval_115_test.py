import unittest
from typing import List, Tuple
import math

class TestMaxFill(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_max_fill_empty_grid(self):
        expected = (0, 0)
        grid = []
        capacity = 1
        result = max_fill(grid, capacity)
        self.assertEqual(result, expected)

    def test_max_fill_single_row_grid(self):
        expected = (2, 2)
        grid = [[2]]
        capacity = 1
        result = max_fill(grid, capacity)
        self.assertEqual(result, expected)

    def test_max_fill_small_grid(self):
        expected = (1, 3)
        grid = [[1, 0], [0, 1]]
        capacity = 2
        result = max_fill(grid, capacity)
        self.assertEqual(result, expected)

    def test_max_fill_large_grid(self):
        expected = (3, 6)
        grid = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        capacity = 2
        result = max_fill(grid, capacity)
        self.assertEqual(result, expected)

    def test_max_fill_capacity_more_water(self):
        expected = (1, 5)
        grid = [[5]]
        capacity = 5
        result = max_fill(grid, capacity)
        self.assertEqual(result, expected)
import unittest
from typing import List, Union

class TestSolution(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_empty_list(self):
        self.assertEqual(solution([]), 0)

    def test_all_even_numbers(self):
        self.assertEqual(solution([2, 4, 6]), 12)

    def test_all_odd_numbers(self):
        self.assertEqual(solution([1, 3, 5]), 0)

    def test_combination_of_even_and_odd_numbers(self):
        self.assertEqual(solution([2, 1, 4, 3]), 7)

    def test_mixed_input(self):
        self.assertEqual(solution([1, "a", -5, 0.25, True]), 0)
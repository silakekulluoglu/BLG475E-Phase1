"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from source.qwen2_5_coder_32b_instruct.hard.human_eval_121 import solution

class TestSolution(unittest.TestCase):
    # [5, 8, 7, 1] → odd values at even indices: 5 (idx 0), 7 (idx 2) → 12
    def test_solution_1(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)

    # [3, 3, 3, 3, 3] → odd values at even indices: 3 (idx 0), 3 (idx 2), 3 (idx 4) → 9
    def test_solution_2(self):
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)

    # [30, 13, 24, 321] → even indices 0 & 2 → values 30, 24 → no odd → 0
    def test_solution_3(self):
        self.assertEqual(solution([30, 13, 24, 321]), 0)

    # [5, 9] → idx 0 = 5 (odd) → total = 5
    def test_solution_4(self):
        self.assertEqual(solution([5, 9]), 5)

    # [30, 13, 23, 32] → idx 0 = 30 (even), idx 2 = 23 (odd) → total = 23
    def test_solution_5(self):
        self.assertEqual(solution([30, 13, 23, 32]), 23)

    # ===============================
    # Additional test cases
    # ===============================

    # [2, 4, 8] → all values even at even indices → 0
    def test_only_evens_at_even_indices(self):
        self.assertEqual(solution([2, 4, 8]), 0)

    # [3] → idx 0 is odd → total = 3
    def test_single_odd_element(self):
        self.assertEqual(solution([3]), 3)

    # [2] → idx 0 is even → total = 0
    def test_single_even_element(self):
        self.assertEqual(solution([2]), 0)

    # [1, 3, 5, 7, 9] → idx 0, 2, 4 → all odd → 1 + 5 + 9 = 15
    def test_all_odd_numbers(self):
        self.assertEqual(solution([1, 3, 5, 7, 9]), 15)

if __name__ == '__main__':
    unittest.main()

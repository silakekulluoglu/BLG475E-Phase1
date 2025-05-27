'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import List, Union
from regenerated_codes.mistral_instruct.hard.human_eval_121 import solution

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)     # 5 (index 0) + 7 (index 2)
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)    # 3 (index 0) + 3 (index 2) + 3 (index 4)
        self.assertEqual(solution([30, 13, 24, 321]), 0)  # no odd numbers at even indices

    def test_empty_list(self):
        self.assertEqual(solution([]), 0)

    def test_single_element_odd(self):
        self.assertEqual(solution([7]), 7)

    def test_single_element_even(self):
        self.assertEqual(solution([2]), 0)

    def test_all_even_indices_even_numbers(self):
        self.assertEqual(solution([2, 1, 4, 3, 6, 5]), 0)

    def test_all_even_indices_odd_numbers(self):
        self.assertEqual(solution([1, 0, 3, 0, 5, 0]), 9)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            solution(['a', 3, 5])

        with self.assertRaises(TypeError):
            solution([1.5, 2.5, 3.5])

        with self.assertRaises(TypeError):
            solution([1, 2, None, 4])

    def test_mixed_valid_and_invalid_elements(self):
        with self.assertRaises(TypeError):
            solution([1, 2, '3', 4, 5])
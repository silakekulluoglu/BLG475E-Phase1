'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
import math
from typing import List, Tuple
from regenerated_codes.mistral_instruct.hard.human_eval_20 import find_closest_elements

class TestFindClosestElements(unittest.TestCase):
    def test_single_element_list_raises_value_error(self):
        with self.assertRaises(ValueError):
            find_closest_elements([1.0])

    def test_empty_list_raises_value_error(self):
        with self.assertRaises(ValueError):
            find_closest_elements([])
            
    def test_find_closest_elements_example_case_1(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))

    def test_find_closest_elements_example_case_2(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))

    def test_find_closest_elements_min_length_input(self):
        self.assertEqual(find_closest_elements([1.5, 1.6]), (1.5, 1.6))

    def test_find_closest_elements_with_negative_numbers(self):
        self.assertEqual(find_closest_elements([-5.0, -4.9, -1.0, 0.0]), (-5.0, -4.9))

    def test_find_closest_elements_with_zeros(self):
        self.assertEqual(find_closest_elements([0.0, 0.0, 1.0]), (0.0, 0.0))

    def test_find_closest_elements_duplicates(self):
        self.assertEqual(find_closest_elements([4.0, 2.0, 2.0, 7.0]), (2.0, 2.0))

    def test_find_closest_elements_close_at_end(self):
        self.assertEqual(find_closest_elements([10.0, 20.0, 30.0, 30.00001]), (30.0, 30.00001))

    def test_find_closest_elements_unordered_input(self):
        self.assertEqual(find_closest_elements([7.1, 1.3, 4.4, 4.3, 2.2]), (4.3, 4.4))

    def test_find_closest_elements_large_input(self):
        import random
        numbers = sorted([random.uniform(0, 10000) for _ in range(1000)])
        numbers.append(numbers[500] + 1e-9)  # make an ultra-close pair
        result = find_closest_elements(numbers)
        self.assertAlmostEqual(abs(result[1] - result[0]), 1e-9)

    def test_find_closest_elements_already_sorted_input(self):
        self.assertEqual(find_closest_elements([1.0, 1.1, 1.2, 1.3]), (1.0, 1.1))

    def test_find_closest_elements_identical_elements(self):
        self.assertEqual(find_closest_elements([5.0, 5.0, 5.0, 5.0]), (5.0, 5.0))
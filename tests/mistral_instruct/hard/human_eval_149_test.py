'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import List, Union
from source.mistral_instruct.hard.human_eval_149 import sorted_list_sum

class TestSortedListSum(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_empty_list(self):
        self.assertEqual(sorted_list_sum([]), [])

    def test_odd_length_only(self):
        self.assertEqual(sorted_list_sum([1, 3, 5]), [1, 3, 5])

    def test_even_length_only(self):
        self.assertEqual(sorted_list_sum(["aa", "ab", "ba"]), ["aa", "ab", "ba"])

    def test_combination_of_odd_and_even_lengths(self):
        self.assertEqual(sorted_list_sum(["a", 1, "b", 3, "c", 5]), ["a", "b", "c", [1, 3, 5]])

    def test_mixed_input(self):
        self.assertEqual(sorted_list_sum([1, "a", -5, 0.25, True]), [])

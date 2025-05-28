'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import List
from regenerated_codes.mistral_instruct.moderate.human_eval_68 import pluck

class TestPluck(unittest.TestCase):
    def test_single_even_number(self):
        self.assertEqual(pluck([2]), [2, 0])

    def test_multiple_even_numbers(self):
        self.assertEqual(pluck([4, 2, 8]), [2, 1])

    def test_multiple_same_smallest_even(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

    def test_no_even_numbers(self):
        self.assertEqual(pluck([1, 3, 5, 7]), [])

    def test_empty_list(self):
        self.assertEqual(pluck([]), [])

    def test_all_even_same_value(self):
        self.assertEqual(pluck([2, 2, 2, 2]), [2, 0])

    def test_large_values(self):
        self.assertEqual(pluck([9999, 8888, 7777, 6666]), [6666, 3])

    def test_first_even_is_smallest(self):
        self.assertEqual(pluck([2, 4, 6, 8]), [2, 0])

    def test_even_at_end(self):
        self.assertEqual(pluck([9, 7, 5, 3, 2]), [2, 4])

    def test_zero_is_even(self):
        self.assertEqual(pluck([9, 0, 2]), [0, 1])
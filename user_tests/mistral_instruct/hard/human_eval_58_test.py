'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import List
from regenerated_codes.mistral_instruct.hard.human_eval_58 import common

class TestCommon(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])

    def test_with_duplicates(self):
        self.assertEqual(common([1, 2, 2, 3], [2, 2, 3, 3]), [2, 3])

    def test_sorted_result(self):
        self.assertEqual(common([10, 5, 1], [1, 10]), [1, 10])

    def test_empty_lists(self):
        self.assertEqual(common([], []), [])

    def test_one_empty_list(self):
        self.assertEqual(common([], [1, 2, 3]), [])
        self.assertEqual(common([4, 5], []), [])

    def test_no_common_elements(self):
        self.assertEqual(common([1, 2, 3], [4, 5, 6]), [])

    def test_all_elements_common(self):
        self.assertEqual(common([1, 2, 3], [3, 2, 1, 1, 3]), [1, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(common([-1, -2, 0, 1], [-2, 1, 3]), [-2, 1])

    def test_large_numbers(self):
        self.assertEqual(common([10**6, 10**9], [10**9, 10**8]), [10**9])
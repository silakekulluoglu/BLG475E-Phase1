'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from regenerated_codes.mistral_instruct.easy.human_eval_30 import get_positive

class TestGetPositive(unittest.TestCase):
    def test_get_positive_empty_list(self):
        result = get_positive([])
        self.assertCountEqual(result, [])

    def test_get_positive_only_positives(self): # This test checks if the function returns the same list when all numbers are positive.
        input_list = [3, 7, 12, 0]
        result = get_positive(input_list)
        expected_output = [3, 7, 12]
        self.assertCountEqual(result, expected_output)

    def test_get_positive_only_zeros(self): # This test checks if the function returns an empty list when there are no positive numbers.
        input_list = [0, 0, 0, -5, 0]
        result = get_positive(input_list)
        self.assertCountEqual(result, [])

    def test_get_positive_negatives_and_positives(self): # This test checks if the function correctly filters out negative numbers and zero.
        input_list = [-3, -2, -1, 0, 4, 5]
        result = get_positive(input_list)
        expected_output = [4, 5]
        self.assertCountEqual(result, expected_output)

    def test_get_positive_with_non_numeric(self): # This test is to ensure that the function handles non-numeric types gracefully.
        input_list = ["a", None, {}, [], "5"]
        with self.assertRaises(TypeError):
            get_positive(input_list)

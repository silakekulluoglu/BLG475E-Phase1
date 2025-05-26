'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from regenerated_codes.mistral_instruct.easy.human_eval_70 import strange_sort_list

class TestStrangeSortList(unittest.TestCase):
    def test_strange_sort_list_empty(self): # Test case for an empty list
        result = strange_sort_list([])
        self.assertEqual(result, [])

    def test_strange_sort_list_single_element(self):  # Test case for a list with a single element
        result = strange_sort_list([1])
        self.assertEqual(result, [1])

    def test_strange_sort_list_two_elements(self): # Test case for a list with two elements
        result = strange_sort_list([3, 1])
        self.assertEqual(result, [1, 3])

    def test_strange_sort_list_same_elements(self): # Test case for a list with the same element repeated
        result = strange_sort_list([7, 7, 7, 7, 7])
        self.assertEqual(result, [7, 7, 7, 7, 7])

    def test_strange_sort_list_cases(self): # Test case for a list with mixed positive and negative integers
        test_cases = [
            ([5, 2, -3, 7], [-3, 7, 2, 5]),
            ([10, -4, 2, 6, 8], [-4, 10, 2, 8, 6]),
            ([3, 1, 5, -2, 4], [-2, 5, 1, 4, 3]),
            ([2, 2, 4, 4, 5], [2, 5, 2, 4, 4]),
            ([1000000, -1000000, 0], [-1000000, 1000000, 0])
        ]

        for input_list, expected_output in test_cases:  # Loop through each test case
            with self.subTest(input=input_list):
                result = strange_sort_list(input_list)
                self.assertEqual(result, expected_output)

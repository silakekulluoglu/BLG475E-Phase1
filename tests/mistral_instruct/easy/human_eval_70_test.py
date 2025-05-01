'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.mistral_instruct.easy.human_eval_70 import strange_sort_list

class TestStrangeSortList(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_strange_sort_list_empty(self):
        result = strange_sort_list([])
        self.assertEqual(result, [])

    def test_strange_sort_list_single_element(self):
        result = strange_sort_list([1])
        self.assertEqual(result, [1])

    def test_strange_sort_list_min_max(self):
        result = strange_sort_list([5, 2, -3, 7])
        expected_output = [2, 5, -3, 7]
        self.assertEqual(result, expected_output)

    def test_strange_sort_list_multiple_min_max(self):
        result = strange_sort_list([10, -4, 2, 6, 8])
        expected_output = [-4, 2, 6, 8, 10]
        self.assertEqual(result, expected_output)

    def test_strange_sort_list_multiple_elements(self):
        result = strange_sort_list([3, 1, 5, -2, 4])
        expected_output = [1, 3, -2, 4, 5]
        self.assertEqual(result, expected_output)

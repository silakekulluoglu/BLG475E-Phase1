'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import List, Union
from regenerated_codes.mistral_instruct.hard.human_eval_85 import add

class TestAdd(unittest.TestCase):
    def test_empty_list(self):
        with self.assertRaises(ValueError) as context:
            add([])
        self.assertEqual(str(context.exception), "The list should be non-empty.")

    def test_example_case(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)  

    def test_only_one_element(self):
        self.assertEqual(add([1]), 0) 

    def test_two_elements_even_at_odd_index(self):
        self.assertEqual(add([9, 4]), 4)  

    def test_two_elements_odd_at_odd_index(self):
        self.assertEqual(add([10, 3]), 0)  

    def test_all_even_at_even_indices(self):
        self.assertEqual(add([2, 1, 4, 3, 6, 5]), 0) 

    def test_all_even_at_odd_indices(self):
        self.assertEqual(add([1, 2, 3, 4, 5, 6]), 2 + 4 + 6) 

    def test_all_odd_at_odd_indices(self):
        self.assertEqual(add([0, 1, 2, 3, 4, 5]), 0)  

    def test_negative_numbers(self):
        self.assertEqual(add([1, -2, 3, -4, 5, -6]), -2 + -4 + -6)  

    def test_mixed_even_odd(self):
        self.assertEqual(add([0, 2, 1, 3, 4, 8]), 2 + 8)

    def test_long_list(self):
        self.assertEqual(add(list(range(100))), sum(i for i in range(1, 100, 2) if i % 2 == 0))

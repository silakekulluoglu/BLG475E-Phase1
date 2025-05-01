'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
import math
from typing import List, Tuple
from source.mistral_instruct.hard.human_eval_20 import find_closest_elements

class TestFindClosestElements(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_find_closest_elements_single_number(self):
        expected = (None, None)
        numbers = [1.0]
        result = find_closest_elements(numbers)
        self.assertEqual(result, expected)

    def test_find_closest_elements_two_distant_numbers(self):
        expected = (2.5, 3.5)
        numbers = [2.0, 3.5]
        result = find_closest_elements(numbers)
        self.assertTupleEqual(result, expected)

    def test_find_closest_elements_two_close_numbers(self):
        expected = (1.5, 2.5)
        numbers = [1.0, 2.5]
        result = find_closest_elements(numbers)
        self.assertTupleEqual(result, expected)

    def test_find_closest_elements_many_numbers(self):
        expected = (2.0, 3.0)
        numbers = [1.0, 2.5, 3.0, 4.0]
        result = find_closest_elements(numbers)
        self.assertTupleEqual(result, expected)

    def test_find_closest_elements_equal_numbers(self):
        expected = (3.0, 3.0)
        numbers = [3.0, 3.0]
        result = find_closest_elements(numbers)
        self.assertTupleEqual(result, expected)
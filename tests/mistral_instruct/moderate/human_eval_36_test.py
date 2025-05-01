'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import List, Tuple
from source.mistral_instruct.moderate.human_eval_36 import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_fizz_buzz_single_case(self):
        expected = 0
        result = fizz_buzz(10)
        self.assertEqual(result, expected)

    def test_fizz_buzz_simple_case(self):
        expected = 2
        result = fizz_buzz(43)
        self.assertEqual(result, expected)

    def test_fizz_buzz_large_input(self):
        expected = 178
        result = fizz_buzz(1000)
        self.assertEqual(result, expected)

    def test_fizz_buzz_edge_case(self):
        expected = 6
        result = fizz_buzz(143)
        self.assertEqual(result, expected)

    def test_fizz_buzz_with_seven(self):
        expected = 1
        result = fizz_buzz(1237)
        self.assertEqual(result, expected)
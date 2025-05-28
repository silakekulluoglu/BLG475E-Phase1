'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import List, Tuple
from regenerated_codes.mistral_instruct.moderate.human_eval_36 import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(fizz_buzz(50), 0)
        self.assertEqual(fizz_buzz(78), 2)  
        self.assertEqual(fizz_buzz(79), 3) 

    def test_small_numbers(self):
        self.assertEqual(fizz_buzz(1), 0)
        self.assertEqual(fizz_buzz(11), 0)
        self.assertEqual(fizz_buzz(14), 0)

    def test_no_matches(self):
        self.assertEqual(fizz_buzz(77), 0)

    def test_multiple_occurrences(self):
        self.assertEqual(fizz_buzz(140), 4)  # 77, 78, 117 

    def test_large_input(self):
        result = fizz_buzz(1000)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)

    def test_no_qualifying_numbers(self):
        self.assertEqual(fizz_buzz(10), 0)

    def test_boundaries(self):
        self.assertEqual(fizz_buzz(0), 0)
        self.assertEqual(fizz_buzz(-10), 0)
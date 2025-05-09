'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import List
from source.mistral_instruct.moderate.human_eval_75 import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_is_multiply_prime_zero(self):
        expected = False
        result = is_multiply_prime(0)
        self.assertEqual(result, expected)

    def test_is_multiply_prime_one(self):
        expected = False
        result = is_multiply_prime(1)
        self.assertEqual(result, expected)

    def test_is_multiply_prime_less_than_two(self):
        expected = False
        result = is_multiply_prime(-1)
        self.assertEqual(result, expected)

    def test_is_multiply_prime_prime_number(self):
        expected = True
        result = is_multiply_prime(7)
        self.assertEqual(result, expected)

    def test_is_multiply_prime_two_times_three(self):
        expected = True
        result = is_multiply_prime(6)
        self.assertEqual(result, expected)
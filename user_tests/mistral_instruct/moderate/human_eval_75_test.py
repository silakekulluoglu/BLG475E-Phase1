'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import List
from regenerated_codes.mistral_instruct.moderate.human_eval_75 import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):
    def test_true_cases(self):
        self.assertTrue(is_multiply_prime(30))  
        self.assertTrue(is_multiply_prime(105))  
        self.assertTrue(is_multiply_prime(66))  

    def test_false_cases(self):
        self.assertFalse(is_multiply_prime(60))  # 2 * 2 * 3 * 5 → 4 primes
        self.assertFalse(is_multiply_prime(97))  # 97 is prime, not product
        self.assertFalse(is_multiply_prime(1))   # not product of 3 primes
        self.assertFalse(is_multiply_prime(0))   # invalid input
        self.assertFalse(is_multiply_prime(99))  # 3 * 3 * 11 = 99, but 3 appears twice → OK only if repetition is allowed

    def test_edge_cases(self):
        self.assertFalse(is_multiply_prime(2))   # single prime
        self.assertFalse(is_multiply_prime(100)) # upper bound (not < 100)
        self.assertFalse(is_multiply_prime(-30)) # negative number

    def test_with_repeated_primes(self):
        self.assertTrue(is_multiply_prime(27))   # 3 * 3 * 3
        self.assertTrue(is_multiply_prime(8))  # 2 * 2 * 2
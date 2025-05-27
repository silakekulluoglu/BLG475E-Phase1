"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from regenerated_codes.qwen2_5_coder_32b_instruct.moderate.human_eval_75 import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):
    # 5 → single prime, not product of 3
    def test_is_multiply_prime_1(self):
        self.assertEqual(is_multiply_prime(5), False)

    # 2 * 3 * 5 = 30 → 3 primes
    def test_is_multiply_prime_2(self):
        self.assertEqual(is_multiply_prime(30), True)

    # 2 * 2 * 2 = 8 → 3 primes, valid
    def test_is_multiply_prime_3(self):
        self.assertEqual(is_multiply_prime(8), True)

    # 2 * 5 = 10 → only 2 primes
    def test_is_multiply_prime_4(self):
        self.assertEqual(is_multiply_prime(10), False)

    # 5 * 5 * 5 = 125 → 3 primes, valid
    def test_is_multiply_prime_5(self):
        self.assertEqual(is_multiply_prime(125), True)


    # ===============================
    # Additional test cases
    # ===============================

    # 6 is not prime
    def test_is_multiply_prime_7(self):
        self.assertEqual(is_multiply_prime(3 * 6 * 7), False)

    # 9 is not prime
    def test_is_multiply_prime_8(self):
        self.assertEqual(is_multiply_prime(9 * 9 * 9), False)

    # 9 not prime
    def test_is_multiply_prime_9(self):
        self.assertEqual(is_multiply_prime(11 * 9 * 9), False)

    # Higher prime values
    def test_is_multiply_prime_10(self):
        self.assertEqual(is_multiply_prime(11 * 13 * 7), True)

if __name__ == '__main__':
    unittest.main()

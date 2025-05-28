'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys, os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../../source/deepseek_coder_v2_lite_instruct/moderate')
    )
)


from human_eval_75 import is_multiply_prime

import unittest

class TestIsMultiplyPrime(unittest.TestCase):
    def test_one(self):
        self.assertFalse(is_multiply_prime(1))

    def test_two_times_two_times_two(self):
        self.assertTrue(is_multiply_prime(8))

    def test_non_prime_factors(self):
        self.assertFalse(is_multiply_prime(30 * 4))

    def test_max_limit(self):
        self.assertTrue(is_multiply_prime(2 * 3 * 97))

if __name__ == '__main__':
    unittest.main()

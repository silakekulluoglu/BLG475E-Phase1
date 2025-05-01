'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest

class TestIsMultiplyPrime(unittest.TestCase):
    def test_false_cases(self):
        self.assertFalse(is_multiply_prime(5))
        self.assertFalse(is_multiply_prime(10))
    
    def test_true_cases(self):
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(8))
        self.assertTrue(is_multiply_prime(11 * 9 * 9))

if __name__ == '__main__':
    unittest.main()

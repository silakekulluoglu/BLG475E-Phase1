'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest

class TestEvenOddPalindrome(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))
        self.assertEqual(even_odd_palindrome(12), (4, 6))
    
    def test_edge_cases(self):
        self.assertEqual(even_odd_palindrome(1), (0, 1))
        self.assertEqual(even_odd_palindrome(123), (8, 13))
        self.assertEqual(even_odd_palindrome(63), (6, 8))

if __name__ == '__main__':
    unittest.main()

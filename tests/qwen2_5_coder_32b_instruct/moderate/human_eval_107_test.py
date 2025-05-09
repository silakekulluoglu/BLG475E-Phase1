'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.qwen2_5_coder_32b_instruct.moderate.human_eval_107 import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):
    def test_even_odd_palindrome_1(self):
        self.assertEqual(even_odd_palindrome(123), (8, 13))

    def test_even_odd_palindrome_2(self):
        self.assertEqual(even_odd_palindrome(12), (4, 6))

    def test_even_odd_palindrome_3(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))

    def test_even_odd_palindrome_4(self):
        self.assertEqual(even_odd_palindrome(63), (6, 8))

    def test_even_odd_palindrome_5(self):
        self.assertEqual(even_odd_palindrome(1), (0, 1))

if __name__ == '__main__':
    unittest.main()
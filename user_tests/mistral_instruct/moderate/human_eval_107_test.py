'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import Tuple
from regenerated_codes.mistral_instruct.moderate.human_eval_107 import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))

    def test_example_2(self):
        self.assertEqual(even_odd_palindrome(12), (4, 6))

    def test_minimum_input(self):
        self.assertEqual(even_odd_palindrome(1), (0, 1))  

    def test_no_palindromes(self):
        with self.assertRaises(Exception):
            even_odd_palindrome(0)

    def test_single_even_palindrome(self):
        self.assertEqual(even_odd_palindrome(2), (1, 1))

    def test_all_single_digit(self):
        self.assertEqual(even_odd_palindrome(9), (4, 5))  

    def test_palindrome_with_double_digits(self):
        self.assertEqual(even_odd_palindrome(22), (5, 6))  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22 are palindromes

    def test_max_input(self):
        result = even_odd_palindrome(1000)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
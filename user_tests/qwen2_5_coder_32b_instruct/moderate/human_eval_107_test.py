"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from source.qwen2_5_coder_32b_instruct.moderate.human_eval_107 import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):
    # Up to 123 → many palindromes including double- and triple-digit
    def test_even_odd_palindrome_1(self):
        self.assertEqual(even_odd_palindrome(123), (8, 13))

    # Mid-range, includes palindromes up to 11
    def test_even_odd_palindrome_2(self):
        self.assertEqual(even_odd_palindrome(12), (4, 6))

    # 1 through 3 → palindromes = [1,2,3]
    def test_even_odd_palindrome_3(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))

    # Up to 63 → broader parity mix
    def test_even_odd_palindrome_4(self):
        self.assertEqual(even_odd_palindrome(63), (6, 8))

    # Edge case: smallest input
    def test_even_odd_palindrome_5(self):
        self.assertEqual(even_odd_palindrome(1), (0, 1))

    # ===============================
    # Additional test cases
    # ===============================

    # Canonical edge case from prompt
    def test_even_odd_palindrome_6(self):
        self.assertEqual(even_odd_palindrome(9), (4, 5))  # palindromes = 1–9

    # Another canonical case from test definition
    def test_even_odd_palindrome_7(self):
        self.assertEqual(even_odd_palindrome(19), (4, 6))  # palindromes include 11

    # First double-digit palindrome included
    def test_even_odd_palindrome_8(self):
        self.assertEqual(even_odd_palindrome(11), (4, 6))  # palindromes: 1–9, 11

    # Upper boundary of input constraint
        def test_even_odd_palindrome_9(self):
        self.assertEqual(even_odd_palindrome(1000), (48, 60))

    # Only one even palindrome
    def test_even_odd_palindrome_10(self):
        self.assertEqual(even_odd_palindrome(2), (1, 1))  # palindromes = [1, 2]

    # n = 0 → invalid (n must be ≥ 1)
    def test_even_odd_palindrome_out_of_range_zero(self):
        with self.assertRaises((ValueError, AssertionError, IndexError)):
            even_odd_palindrome(0)

    # n = -10 → invalid (n must be positive)
    def test_even_odd_palindrome_11_out_of_range_negative(self):
        with self.assertRaises((ValueError, AssertionError, IndexError)):
            even_odd_palindrome(-10)

    # n = 1001 → above upper bound
    def test_even_odd_palindrome_12_out_of_range_above_max(self):
        with self.assertRaises((ValueError, AssertionError)):
            even_odd_palindrome(1001)

    # n = 3.5 → invalid type
    def test_even_odd_palindrome_13_non_integer(self):
        with self.assertRaises((TypeError, ValueError)):
            even_odd_palindrome(3.5)

    # n = '100' → invalid type
    def test_even_odd_palindrome_14_string_input(self):
        with self.assertRaises((TypeError, ValueError)):
            even_odd_palindrome("100")


if __name__ == '__main__':
    unittest.main()

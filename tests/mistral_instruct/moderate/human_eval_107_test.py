import unittest
from typing import Tuple
from source.mistral_instruct import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_even_odd_palindrome_zero(self):
        expected = (0, 0)
        result = even_odd_palindrome(0)
        self.assertEqual(result, expected)

    def test_even_odd_palindrome_one(self):
        expected = (0, 1)
        result = even_odd_palindrome(1)
        self.assertEqual(result, expected)

    def test_even_odd_palindrome_small_number(self):
        expected = (3, 1)
        result = even_odd_palindrome(9)
        self.assertEqual(result, expected)

    def test_even_odd_palindrome_large_number(self):
        expected = (205, 140)
        result = even_odd_palindrome(6789)
        self.assertEqual(result, expected)

    def test_even_odd_palindrome_negative_number(self):
        expected = (0, 0)
        result = even_odd_palindrome(-1)
        self.assertEqual(result, expected)

    def test_even_odd_palindrome_large_negative_number(self):
        expected = (0, 0)
        result = even_odd_palindrome(-987654321)
        self.assertEqual(result, expected)
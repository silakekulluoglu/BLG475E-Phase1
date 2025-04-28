import unittest

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
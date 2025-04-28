import unittest

class TestPalindromes(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_is_palindrome_empty_string(self):
        expected = True
        string = ""
        result = is_palindrome(string)
        self.assertEqual(result, expected)

    def test_is_palindrome_single_char(self):
        expected = True
        string = "A"
        result = is_palindrome(string)
        self.assertEqual(result, expected)

    def test_is_palindrome_simple_word(self):
        expected = False
        string = "banana"
        result = is_palindrome(string)
        self.assertEqual(result, expected)

    def test_is_palindrome_palindrome(self):
        expected = True
        string = "racecar"
        result = is_palindrome(string)
        self.assertEqual(result, expected)

    def test_make_palindrome_empty_string(self):
        expected = ""
        string = ""
        result = make_palindrome(string)
        self.assertEqual(result, expected)

    def test_make_palindrome_single_char(self):
        expected = "A"
        string = "A"
        result = make_palindrome(string)
        self.assertEqual(result, expected)

    def test_make_palindrome_simple_word(self):
        expected = "bananabanana"
        string = "banana"
        result = make_palindrome(string)
        self.assertEqual(result, expected)

    def test_make_palindrome_palindrome(self):
        expected = "racererace"
        string = "racecar"
        result = make_palindrome(string)
        self.assertEqual(result, expected)

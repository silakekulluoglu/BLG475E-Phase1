import unittest
from typing import StringIO, Dict

class TestRemoveVowels(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_remove_vowels_empty_string(self):
        expected = ""
        result = remove_vowels("")
        self.assertEqual(result, expected)

    def test_remove_vowels_single_letter(self):
        expected = "t"
        result = remove_vowels("t")
        self.assertEqual(result, expected)

    def test_remove_vowels_simple_string(self):
        expected = "hsl"
        result = remove_vowels("hello world!")
        self.assertEqual(result, expected)

    def test_remove_vowels_complex_string(self):
        expected = "N'w-d53-B@f7!"
        result = remove_vowels("New-Developer@Fiverr!")
        self.assertEqual(result, expected)

    def test_remove_vowels_mixed_case(self):
        expected = "Cdwrfs"
        result = remove_vowels("CodeWars is fun!")
        self.assertEqual(result, expected)
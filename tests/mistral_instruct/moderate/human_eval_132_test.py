import unittest
from typing import List, Optional
from source.mistral_instruct import is_nested


class TestIsNested(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_is_nested_empty_string(self):
        expected = True
        string = ""
        result = is_nested(string)
        self.assertEqual(result, expected)

    def test_is_nested_single_bracket(self):
        expected = False
        string = "]"
        result = is_nested(string)
        self.assertEqual(result, expected)

    def test_is_nested_no_matching_brackets(self):
        expected = False
        string = "([)]"
        result = is_nested(string)
        self.assertEqual(result, expected)

    def test_is_nested_single_bracket_pair(self):
        expected = True
        string = "[]"
        result = is_nested(string)
        self.assertEqual(result, expected)

    def test_is_nested_multiple_brackets(self):
        expected = True
        string = "[()()]"
        result = is_nested(string)
        self.assertEqual(result, expected)
import unittest
from source.mistral_instruct import split_words

class TestSplitWords(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_split_words_empty(self):
        result = split_words("")
        self.assertEqual(result, [])

    def test_split_words_no_spaces(self):
        result = split_words("HelloWorld")
        self.assertEqual(result, ["helloworld"])

    def test_split_words_simple_space(self):
        result = split_words("Hello World")
        self.assertEqual(result, ["hello", "world"])

    def test_split_words_multiple_spaces(self):
        result = split_words("Hello   World   !")
        self.assertEqual(result, ["hello", "world"])

    def test_split_words_special_chars(self):
        result = split_words("Hello@World!")
        self.assertEqual(result, ["hello", "@world!"])
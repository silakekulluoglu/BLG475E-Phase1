import unittest
import string
from source.mistral_instruct.easy.human_eval_27 import flip_case

class TestFlipCase(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_flip_lowercase(self):
        input_string = "hello world"
        result = flip_case(input_string)
        expected_output = "HELLO WORLD"
        self.assertEqual(result, expected_output)

    def test_flip_uppercase(self):
        input_string = "HELLO WORLD"
        result = flip_case(input_string)
        expected_output = "hello world"
        self.assertEqual(result, expected_output)

    def test_flip_mixed_case(self):
        input_string = "HeLLo wOrLd"
        result = flip_case(input_string)
        expected_output = "heLLo wORld"
        self.assertEqual(result, expected_output)

    def test_flip_empty_string(self):
        input_string = ""
        result = flip_case(input_string)
        expected_output = ""
        self.assertEqual(result, expected_output)

    def test_flip_special_characters(self):
        input_string = "!@#$%^&*()_+-=[]{}|\\:;'<>,.?/"
        result = flip_case(input_string)
        expected_output = "!@#$%^&*()_+-=[]{}{}|\\:\;'\<>,.?>/"
        self.assertEqual(result, expected_output)
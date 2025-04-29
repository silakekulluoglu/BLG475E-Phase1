import unittest
from source.mistral_instruct import anti_shuffle

class TestAntiShuffle(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_anti_shuffle_empty(self):
        result = anti_shuffle('')
        self.assertEqual(result, '')

    def test_anti_shuffle_single_word(self):
        result = anti_shuffle('hello')
        expected_output = 'ehllo'
        self.assertEqual(result, expected_output)

    def test_anti_shuffle_multiple_words(self):
        result = anti_shuffle("I am a programmer")
        expected_output = "AaimaMproramgeer"
        self.assertEqual(result, expected_output)

    def test_anti_shuffle_mixed_case(self):
        result = anti_shuffle("HELLO WORLD")
        expected_output = "hElLoWoRlD"
        self.assertEqual(result, expected_output)

    def test_anti_shuffle_special_characters(self):
        result = anti_shuffle("Hello1World!@#$%")
        expected_output = "hEllo1WorlD!@#$%"
        self.assertEqual(result, expected_output)
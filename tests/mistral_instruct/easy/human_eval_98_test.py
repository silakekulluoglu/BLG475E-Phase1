import unittest
from source.mistral_instruct import count_upper

class TestCountUpper(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_count_upper_empty(self):
        result = count_upper('')
        self.assertEqual(result, 0)

    def test_count_upper_single_uppercase_vowel(self):
        result = count_upper("A")
        self.assertEqual(result, 1)

    def test_count_upper_multiple_uppercase_vowels(self):
        result = count_upper("IOU")
        self.assertEqual(result, 2)

    def test_count_upper_odd_number_of_letters(self):
        result = count_upper("OUI")
        self.assertEqual(result, 1)

    def test_count_upper_mixed_case(self):
        result = count_upper("ioUaEo")
        self.assertEqual(result, 2)
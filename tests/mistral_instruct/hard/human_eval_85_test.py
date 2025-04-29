import unittest
from typing import List, Union

class TestAdd(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_empty_list(self):
        with self.assertRaises(ValueError) as context:
            add([])
        self.assertEqual(str(context.exception), "The list should be non-empty.")

    def test_odd_number_of_elements(self):
        with self.assertRaises(ValueError) as context:
            add([1, 2, 3])
        self.assertEqual(str(context.exception), "The list should be non-empty.")

    def test_all_even_numbers(self):
        self.assertEqual(add([0, 2, 4]), 6)

    def test_all_odd_numbers(self):
        self.assertEqual(add([1, 3, 5]), 9)

    def test_combination_of_even_and_odd_numbers(self):
        self.assertEqual(add([0, 1, 2, 4]), 6)
import unittest
from typing import List
from source.mistral_instruct.moderate.human_eval_21 import rescale_to_unit

class TestRescale(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_rescale_empty_list(self):
        result = rescale_to_unit([])
        self.assertEqual(result, [])

    def test_rescale_simple_case(self):
        numbers = [3, 5, 1, 7]
        expected_scaled = [0.082, 0.143, 0.021, 0.235]
        result = rescale_to_unit(numbers)
        self.assertListEqual(result, expected_scaled)

    def test_rescale_large_numbers(self):
        numbers = [23456789.123456, 32109876.543210]
        expected_scaled = [0.9283781, 1.4366217]
        result = rescale_to_unit(numbers)
        self.assertListEqual(result, expected_scaled)

    def test_rescale_negative_numbers(self):
        numbers = [-5, -3, 2]
        expected_scaled = [1.0, 0.6, 0.4]
        result = rescale_to_unit(numbers)
        self.assertListEqual(result, expected_scaled)
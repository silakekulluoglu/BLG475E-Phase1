import unittest
from typing import List
from source.mistral_instruct import pluck

class TestPluck(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_pluck_empty_array(self):
        expected = []
        result = pluck([])
        self.assertEqual(result, expected)

    def test_pluck_odd_array(self):
        expected = []
        result = pluck([1, 3, 5])
        self.assertEqual(result, expected)

    def test_pluck_even_array(self):
        expected = [2, 1]
        result = pluck([0, 2, 4, 6])
        self.assertEqual(result, expected)

    def test_pluck_mixed_array(self):
        expected = [4, 1]
        result = pluck([1, 3, 4, 5, 7, 9, 2])
        self.assertEqual(result, expected)

    def test_pluck_longer_array(self):
        expected = [8, 3]
        result = pluck([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(result, expected)
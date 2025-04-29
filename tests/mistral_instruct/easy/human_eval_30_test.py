import unittest
from source.mistral_instruct import get_positive

class TestGetPositive(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_get_positive_empty_list(self):
        result = get_positive([])
        self.assertCountEqual(result, [])

    def test_get_positive_only_positives(self):
        input_list = [3, 7, 12, 0]
        result = get_positive(input_list)
        expected_output = [3, 7, 12]
        self.assertCountEqual(result, expected_output)

    def test_get_positive_only_zeros(self):
        input_list = [0, 0, 0, -5, 0]
        result = get_positive(input_list)
        self.assertCountEqual(result, [])

    def test_get_positive_negatives_and_positives(self):
        input_list = [-3, -2, -1, 0, 4, 5]
        result = get_positive(input_list)
        expected_output = [4, 5]
        self.assertCountEqual(result, expected_output)
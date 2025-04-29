import unittest
from source.mistral_instruct import truncate_number


class TestTruncateNumber(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_truncate_zero(self):
        result = truncate_number(0.0)
        self.assertEqual(result, 0.0)

    def test_truncate_positive(self):
        result = truncate_number(4.5)
        self.assertEqual(result, 4.0)

    def test_truncate_negative(self):
        result = truncate_number(-3.125)
        self.assertEqual(result, -3.0)

    def test_truncate_integer(self):
        result = truncate_number(5)
        self.assertEqual(result, 5.0)

    def test_edge_cases(self):
        result1 = truncate_number(-0.5)
        result2 = truncate_number(0.5)
        self.assertEqual(result1, -0.0)
        self.assertEqual(result2, 0.0)

if __name__ == "__main__":
    unittest.main()
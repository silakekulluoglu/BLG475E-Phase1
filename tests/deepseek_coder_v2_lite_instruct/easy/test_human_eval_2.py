import unittest

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number_3_5(self):
        self.assertEqual(truncate_number(3.5), 0.5)

    def test_truncate_number_1_33(self):
        self.assertAlmostEqual(truncate_number(1.33), 0.33)

    def test_truncate_number_123_456(self):
        self.assertAlmostEqual(truncate_number(123.456), 0.456)

    def test_truncate_number_negative(self):
        self.assertEqual(truncate_number(-3.5), -0.5)

    def test_truncate_number_zero(self):
        self.assertEqual(truncate_number(0.0), 0.0)

if __name__ == "__main__":
    unittest.main()

import unittest

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number_1(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5)

    def test_truncate_number_2(self):
        self.assertAlmostEqual(truncate_number(1.33), 0.33)

    def test_truncate_number_3(self):
        self.assertAlmostEqual(truncate_number(123.456), 0.456)

    def test_truncate_number_4(self):
        self.assertAlmostEqual(truncate_number(0.999), 0.999)

    def test_truncate_number_5(self):
        self.assertAlmostEqual(truncate_number(10.0), 0.0)

if __name__ == '__main__':
    unittest.main()
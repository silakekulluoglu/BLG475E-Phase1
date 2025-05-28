'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys, os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../../source/deepseek_coder_v2_lite_instruct/easy')
    )
)

from human_eval_2 import truncate_number

import unittest

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number_integer(self):
        self.assertEqual(truncate_number(5.0), 0.0)

    def test_truncate_number_fraction_below_one(self):
        self.assertAlmostEqual(truncate_number(0.75), 0.75)

    def test_truncate_number_high_precision(self):
        self.assertAlmostEqual(truncate_number(3.1415926535), 0.1415926535, places=10)

    def test_truncate_number_tiny_fraction(self):
        self.assertAlmostEqual(truncate_number(1.000000001), 1e-9, places=12)

    def test_truncate_number_large_value(self):
        # IEEE-754 result for (1e12 + 0.87654321) % 1.0
        expected = 0.8765869140625
        result = truncate_number(1e12 + 0.87654321)
        self.assertAlmostEqual(result, expected, places=12)

    def test_truncate_number_roundoff(self):
        val = 2.0000000002
        expected = val - int(val)
        self.assertAlmostEqual(truncate_number(val), expected, places=12)


if __name__ == "__main__":
    unittest.main()

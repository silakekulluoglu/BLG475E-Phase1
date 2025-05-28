'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../../source/deepseek_coder_v2_lite_instruct/moderate')
    )
)

from human_eval_13 import greatest_common_divisor

import unittest

class TestGreatestCommonDivisor(unittest.TestCase):
    def test_zero_and_positive(self):
        self.assertEqual(greatest_common_divisor(0, 5), 5)
        self.assertEqual(greatest_common_divisor(5, 0), 5)

    def test_both_zero(self):
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_equal_inputs(self):
        self.assertEqual(greatest_common_divisor(7, 7), 7)

    def test_large_numbers(self):
        self.assertEqual(greatest_common_divisor(100000, 25000), 25000)
        self.assertEqual(greatest_common_divisor(123456, 789012), 12)

if __name__ == '__main__':
    unittest.main()

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


from human_eval_103 import rounded_avg


import unittest

class TestRoundedAvg(unittest.TestCase):
    def test_adjacent_numbers(self):
        self.assertEqual(rounded_avg(100, 101), "0b1100100")

    def test_half_round_down(self):
        self.assertEqual(rounded_avg(8, 9), "0b1000")

    def test_half_round_up(self):
        self.assertEqual(rounded_avg(1, 2), "0b10")

    def test_large_range(self):
        expected = bin(round((1 + 100) / 2))
        self.assertEqual(rounded_avg(1, 100), expected)

    def test_equal_bounds(self):
        self.assertEqual(rounded_avg(42, 42), "0b101010")

    def test_invalid_range(self):
        self.assertEqual(rounded_avg(10, 5), -1)

if __name__ == "__main__":
    unittest.main()


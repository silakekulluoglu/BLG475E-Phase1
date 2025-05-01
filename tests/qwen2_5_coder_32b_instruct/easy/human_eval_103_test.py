'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.qwen2_5_coder_32b_instruct.easy.human_eval_103 import rounded_avg

class TestRoundedAvg(unittest.TestCase):
    def test_rounded_avg_1(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")

    def test_rounded_avg_2(self):
        self.assertEqual(rounded_avg(7, 13), "0b1010")

    def test_rounded_avg_3(self):
        self.assertEqual(rounded_avg(5, 5), "0b101")

    def test_rounded_avg_4(self):
        self.assertEqual(rounded_avg(7, 5), -1)

    def test_rounded_avg_5(self):
        self.assertEqual(rounded_avg(10, 20), "0b1111")

if __name__ == '__main__':
    unittest.main()
'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.qwen2_5_coder_32b_instruct.hard.human_eval_94 import skjkasdkd

class TestSkjkasdkd(unittest.TestCase):
    def test_skjkasdkd_1(self):
        self.assertEqual(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]), 10)

    def test_skjkasdkd_2(self):
        self.assertEqual(skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]), 25)

    def test_skjkasdkd_3(self):
        self.assertEqual(skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]), 13)

    def test_skjkasdkd_4(self):
        self.assertEqual(skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6]), 11)

    def test_skjkasdkd_5(self):
        self.assertEqual(skjkasdkd([0,81,12,3,1,21]), 3)

if __name__ == '__main__':
    unittest.main()
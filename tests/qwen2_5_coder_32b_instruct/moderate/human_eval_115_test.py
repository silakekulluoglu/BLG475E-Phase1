'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
import math
from source.qwen2_5_coder_32b_instruct.moderate.human_eval_115 import max_fill

class TestMaxFill(unittest.TestCase):
    def test_max_fill_1(self):
        self.assertEqual(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1), 6)

    def test_max_fill_2(self):
        self.assertEqual(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2), 5)

    def test_max_fill_3(self):
        self.assertEqual(max_fill([[0,0,0], [0,0,0]], 5), 0)

    def test_max_fill_4(self):
        self.assertEqual(max_fill([[1,1,1,1], [1,1,1,1]], 2), 4)

    def test_max_fill_5(self):
        self.assertEqual(max_fill([[1,1,1,1], [1,1,1,1]], 9), 2)

if __name__ == '__main__':
    unittest.main()
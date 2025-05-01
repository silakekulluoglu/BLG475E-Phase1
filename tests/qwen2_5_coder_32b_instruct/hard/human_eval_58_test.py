'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.qwen2_5_coder_32b_instruct.hard.human_eval_58 import common

class TestCommon(unittest.TestCase):
    def test_common_1(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])

    def test_common_2(self):
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])

    def test_common_3(self):
        self.assertEqual(common([4, 3, 2, 8], [3, 2, 4]), [2, 3, 4])

    def test_common_4(self):
        self.assertEqual(common([4, 3, 2, 8], []), [])

    def test_common_5(self):
        self.assertEqual(common([10, 20, 30], [5, 15, 25, 35]), [])

if __name__ == '__main__':
    unittest.main()
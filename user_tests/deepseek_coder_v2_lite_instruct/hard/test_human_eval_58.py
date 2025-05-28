'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys, os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../../source/deepseek_coder_v2_lite_instruct/hard')
    )
)

from human_eval_58 import common

import unittest

class TestCommon(unittest.TestCase):
    def test_with_negatives(self):
        self.assertEqual(common([-1, 0, 1, 2], [2, -1, 3]), [-1, 2])
    def test_duplicates(self):
        self.assertEqual(common([1, 1, 2, 2], [2, 2, 3]), [2])
    def test_no_common(self):
        self.assertEqual(common([1, 2], [3, 4]), [])
    def test_both_empty(self):
        self.assertEqual(common([], []), [])
    def test_all_common(self):
        self.assertEqual(common([3, 4, 5], [5, 4, 3]), [3, 4, 5])


if __name__ == '__main__':
    unittest.main()
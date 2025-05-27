'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys, os

sys.path.insert(0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '../../../../source/deepseek_coder_v2_lite_instruct/hard'
        )
    )
)

from human_eval_121 import solution

import unittest

class TestSolution(unittest.TestCase):
    def test_alternating(self):
        self.assertEqual(solution([1,2,3,4,5,6]), 1+3+5)
    def test_no_odds(self):
        self.assertEqual(solution([2,4,6,8]), 0)
    def test_single_pair(self):
        self.assertEqual(solution([9,10]), 9)
    def test_all_odds(self):
        self.assertEqual(solution([1,3,5,7,9]), 1+5+9)
    def test_mixed(self):
        self.assertEqual(solution([0,1,2,3,4]), 0)

if __name__ == "__main__":
    unittest.main()
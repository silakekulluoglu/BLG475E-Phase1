'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys, os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../../source/deepseek_coder_v2_lite_instruct/moderate')
    )
)


from human_eval_68 import pluck

import unittest

class TestPluck(unittest.TestCase):
    def test_no_even(self):
        self.assertEqual(pluck([1,3,5,7]), [])

    def test_even_at_start(self):
        self.assertEqual(pluck([2,3,4]), [2, 0])

    def test_multiple_minimum(self):
        self.assertEqual(pluck([4,2,2,6,2]), [2, 1])

    def test_large_list(self):
        arr = list(range(1000))
        self.assertEqual(pluck(arr), [0, 0])

if __name__ == '__main__':
    unittest.main()

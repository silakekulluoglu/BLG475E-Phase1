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

from human_eval_85 import add

import unittest

class TestAdd(unittest.TestCase):
    def test_negative_and_even(self):
        self.assertEqual(add([ -2, -4, -6, -7]), -4) 
    def test_all_odd(self):
        self.assertEqual(add([1,3,5,7]), 0)
    def test_mixed_positions(self):
        self.assertEqual(add([2,4,6,8,10]), 12)  
    def test_single_element(self):
        self.assertEqual(add([2]), 0)
    def test_empty_list(self):
        self.assertEqual(add([]), 0)

if __name__ == '__main__':
    unittest.main()
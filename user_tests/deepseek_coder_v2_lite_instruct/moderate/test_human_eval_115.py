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


from human_eval_115 import max_fill

import unittest

class TestMaxFill(unittest.TestCase):
    def test_exact_division(self):
        self.assertEqual(max_fill([[1,1,1], [2,2,2]], 3), 3)  # 3/3 + 6/3 = 1 + 2

    def test_capacity_one(self):
        self.assertEqual(max_fill([[1,0,1], [0,1]], 1), 3)

    def test_empty_grid(self):
        self.assertEqual(max_fill([], 5), 0)

    def test_mixed_empty_and_full(self):
        self.assertEqual(max_fill([[0,0], [1,1]], 2), 1)

if __name__ == '__main__':
    unittest.main()

'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys
import os

# Add the path to the source code
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../../source/deepseek_coder_v2_lite_instruct/easy')
    )
)

from human_eval_30 import get_positive


import unittest

class TestGetPositive(unittest.TestCase):
    def test_single_positive(self):
        self.assertEqual(get_positive([42]), [42])

    def test_all_zero(self):
        self.assertEqual(get_positive([0, 0, 0]), [])

    def test_floats_and_ints(self):
        self.assertEqual(get_positive([-1.5, 0.0, 2.2, -3.3, 4.0]), [2.2, 4.0])

    def test_duplicates(self):
        self.assertEqual(get_positive([1, 1, -1, 1]), [1, 1, 1])

    def test_large_range(self):
        self.assertEqual(get_positive(list(range(-5, 6))), [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()


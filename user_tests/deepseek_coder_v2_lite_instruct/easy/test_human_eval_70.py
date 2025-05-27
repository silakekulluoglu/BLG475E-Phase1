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

from human_eval_70 import strange_sort_list


import unittest

class TestStrangeSortList(unittest.TestCase):
    def test_two_elements(self):
        self.assertEqual(strange_sort_list([10, -1]), [-1, 10])

    def test_three_elements(self):
        self.assertEqual(strange_sort_list([3, 1, 2]), [1, 3, 2])

    def test_duplicates_min_max(self):
        self.assertEqual(strange_sort_list([2, 5, 2, 5]), [2, 5, 2, 5])

    def test_descending_input(self):
        self.assertEqual(strange_sort_list([5, 4, 3, 2, 1]), [1, 5, 2, 4, 3])

    def test_mixed_negative_positive(self):
        self.assertEqual(strange_sort_list([-3, 0, 3, -1, 1]), [-3, 3, -1, 1, 0])

    def test_even_length(self):
        self.assertEqual(strange_sort_list([7, 3, 5, 1]), [1, 7, 3, 5])

if __name__ == "__main__":
    unittest.main()


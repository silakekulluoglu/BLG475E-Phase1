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

from human_eval_20 import find_closest_elements

import unittest

class TestFindClosestElements(unittest.TestCase):
    def test_negative_and_positive(self):
        self.assertEqual(find_closest_elements([-1.0, 0.0, 1.0]), (-1.0, 0.0))

    def test_two_elements(self):
        self.assertEqual(find_closest_elements([0.0, 2.0]), (0.0, 2.0))

    def test_multiple_min_pairs(self):
        self.assertEqual(find_closest_elements([1.0, 1.2, 1.1]), (1.1, 1.2))

    def test_unordered_input(self):
        self.assertEqual(find_closest_elements([5.5, 3.3, 4.4]), (4.4, 5.5))

    def test_equal_values(self):
        self.assertEqual(find_closest_elements([2.0, 2.0, 3.0]), (2.0, 2.0))

if __name__ == '__main__':
    unittest.main()

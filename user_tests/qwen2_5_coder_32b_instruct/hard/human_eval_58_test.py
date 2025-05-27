"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from regenerated_codes.qwen2_5_coder_32b_instruct.hard.human_eval_58 import common

class TestCommon(unittest.TestCase):
    # Normal case with multiple overlaps and unordered input
    def test_common_1(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])

    # Second list is a proper subset of the first
    def test_common_2(self):
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])

    # All elements are shared
    def test_common_3(self):
        self.assertEqual(common([4, 3, 2, 8], [3, 2, 4]), [2, 3, 4])

    # One list is empty → result should be empty
    def test_common_4(self):
        self.assertEqual(common([4, 3, 2, 8], []), [])

    # No overlapping elements
    def test_common_5(self):
        self.assertEqual(common([10, 20, 30], [5, 15, 25, 35]), [])

    # ===============================
    # Additional test cases
    # ===============================

    # Both lists empty → result should be empty
    def test_common_empty_lists(self):
        self.assertEqual(common([], []), [])

    # Repeated elements in both lists → result still unique
    def test_common_duplicates(self):
        self.assertEqual(common([1, 1, 2, 2, 3, 3], [2, 2, 3, 3, 4, 4]), [2, 3])

    # Identical lists → return sorted unique values
    def test_common_same_list_twice(self):
        self.assertEqual(common([5, 2, 2, 1], [5, 2, 2, 1]), [1, 2, 5])

if __name__ == '__main__':
    unittest.main()

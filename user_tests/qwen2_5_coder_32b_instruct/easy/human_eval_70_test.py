"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from regenerated_codes.qwen2_5_coder_32b_instruct.easy.human_eval_70 import strange_sort_list

class TestStrangeSortList(unittest.TestCase):
    # Simple increasing sequence → alternates min and max
    def test_strange_sort_list_1(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

    # General case with more numbers
    def test_strange_sort_list_2(self):
        self.assertEqual(strange_sort_list([5, 6, 7, 8, 9]), [5, 9, 6, 8, 7])

    # All values are the same
    def test_strange_sort_list_3(self):
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

    # Empty list input
    def test_strange_sort_list_4(self):
        self.assertEqual(strange_sort_list([]), [])

    # Duplicates, negative and zero values
    def test_strange_sort_list_5(self):
        self.assertEqual(strange_sort_list([0, 2, 2, 2, 5, 5, -5, -5]), [-5, 5, -5, 5, 0, 2, 2, 2])

    # ===============================
    # Additional test cases
    # ===============================

    # Single element
    def test_strange_sort_list_6_single(self):
        self.assertEqual(strange_sort_list([42]), [42])

    # Two elements ascending
    def test_strange_sort_list_7_two_sorted(self):
        self.assertEqual(strange_sort_list([1, 2]), [1, 2])

    # Two elements descending
    def test_strange_sort_list_8_two_reversed(self):
        self.assertEqual(strange_sort_list([9, 3]), [3, 9])

    # Already descending list
    def test_strange_sort_list_9_descending(self):
        self.assertEqual(strange_sort_list([9, 8, 7, 6]), [6, 9, 7, 8])

    # All negative values
    def test_strange_sort_list_10_all_negative(self):
        self.assertEqual(strange_sort_list([-3, -1, -2]), [-3, -1, -2])

    # Alternating high-low pattern input
    def test_strange_sort_list_11_alternating(self):
        self.assertEqual(strange_sort_list([1, 100, 2, 99, 3, 98]), [1, 100, 2, 99, 3, 98])

    # Larger input to check performance and consistency
    def test_strange_sort_list_12_large_input(self):
        input_list = list(range(1, 21))  # 1 to 20
        expected = [1, 20, 2, 19, 3, 18, 4, 17, 5, 16, 6, 15, 7, 14, 8, 13, 9, 12, 10, 11]
        self.assertEqual(strange_sort_list(input_list), expected)

if __name__ == '__main__':
    unittest.main()

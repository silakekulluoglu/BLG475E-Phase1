"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from source.qwen2_5_coder_32b_instruct.hard.human_eval_149 import sorted_list_sum

class TestSortedListSum(unittest.TestCase):
    # ["aa", "a", "aaa"] → "aa" is even → result = ["aa"]
    def test_sorted_list_sum_1(self):
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])

    # Mixed lengths → keep "AI" (2), "asdf" (4), "school" (6) → sorted by length
    def test_sorted_list_sum_2(self):
        self.assertEqual(sorted_list_sum(["school", "AI", "asdf", "b"]), ["AI", "asdf", "school"])

    # All strings have odd length → return []
    def test_sorted_list_sum_3(self):
        self.assertEqual(sorted_list_sum(["d", "b", "c", "a"]), [])

    # Keep only even-length strings → sorted by length then alphabetically
    def test_sorted_list_sum_4(self):
        self.assertEqual(sorted_list_sum(["d", "dcba", "abcd", "a"]), ["abcd", "dcba"])

    # All strings of same even length → sort alphabetically
    def test_sorted_list_sum_5(self):
        self.assertEqual(sorted_list_sum(["AI", "ai", "au"]), ["AI", "ai", "au"])

    # ===============================
    # Additional test cases
    # ===============================

    # All even-length strings, mixed order → sort by length then alphabetically
    def test_sorted_list_sum_same_length(self):
        self.assertEqual(sorted_list_sum(["bbbb", "aaaa", "cccc", "dddd"]), ["aaaa", "bbbb", "cccc", "dddd"])

    # Duplicates retained, sort alphabetically within length
    def test_sorted_list_sum_with_duplicates(self):
        self.assertEqual(sorted_list_sum(["aa", "bb", "aa", "cc", "a"]), ["aa", "aa", "bb", "cc"])

    # Empty input → should return empty list
    def test_sorted_list_sum_empty(self):
        self.assertEqual(sorted_list_sum([]), [])

    # All even strings with identical lengths and different cases
    def test_sorted_list_sum_case_order(self):
        self.assertEqual(sorted_list_sum(["ba", "Ba", "aA", "AA"]), ["AA", "Ba", "aA", "ba"])

if __name__ == '__main__':
    unittest.main()

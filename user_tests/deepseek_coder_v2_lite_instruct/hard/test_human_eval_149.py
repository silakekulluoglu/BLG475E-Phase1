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

from human_eval_149 import sorted_list_sum

import unittest

class TestSortedListSum(unittest.TestCase):
    def test_all_even_lengths(self):
        self.assertEqual(sorted_list_sum(["aa","bb","cc"]), ["aa","bb","cc"])
    def test_mixed_lengths(self):
        self.assertEqual(sorted_list_sum(["a","bb","ccc","dddd"]), ["bb","dddd"])
    def test_duplicates(self):
        self.assertEqual(sorted_list_sum(["aa","aa","b","b"]), ["aa","aa"])
    def test_empty(self):
        self.assertEqual(sorted_list_sum([]), [])
    def test_same_length_alphabetical(self):
        self.assertEqual(sorted_list_sum(["dc","ab","bb"]), ["ab","bb","dc"])

if __name__ == "__main__":
    unittest.main()
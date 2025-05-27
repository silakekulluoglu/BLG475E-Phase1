'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import List, Union
from source.mistral_instruct.hard.human_eval_149 import sorted_list_sum

class TestSortedListSum(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])

    def test_multiple_even_length(self):
        self.assertEqual(sorted_list_sum(["ab", "a", "aaa", "cd"]), ["ab", "cd"])

    def test_duplicates(self):
        self.assertEqual(sorted_list_sum(["aa", "aa", "a", "aaa"]), ["aa", "aa"])

    def test_already_sorted(self):
        self.assertEqual(sorted_list_sum(["aa", "ab", "ac"]), ["aa", "ab", "ac"])

    def test_alphabetical_tiebreak(self):
        self.assertEqual(sorted_list_sum(["cd", "ab", "bb", "ac"]), ["ab", "ac", "bb", "cd"])

    def test_empty_list(self):
        self.assertEqual(sorted_list_sum([]), [])

    def test_all_odd_lengths(self):
        self.assertEqual(sorted_list_sum(["a", "aaa", "abc"]), [])

    def test_all_even_lengths(self):
        self.assertEqual(sorted_list_sum(["to", "be", "or", "not"]), ["be", "or", "to"])

    def test_case_sensitivity(self):
        self.assertEqual(sorted_list_sum(["Aa", "aa", "AB", "ab"]), ["AB", "Aa", "aa", "ab"])

    def test_empty_strings(self):
        self.assertEqual(sorted_list_sum(["", "a", "bb", "ccc", "dddd"]), ["", "bb", "dddd"])

    def test_large_input(self):
        input_list = ["even"] * 1000 + ["odd"] * 1000
        expected = ["even"] * 1000
        self.assertEqual(sorted_list_sum(input_list), expected)

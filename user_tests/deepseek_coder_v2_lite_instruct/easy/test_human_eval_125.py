'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys, os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../../source/deepseek_coder_v2_lite_instruct/easy')
    )
)

from human_eval_125 import split_words


import unittest

class TestSplitWords(unittest.TestCase):
    def test_both_whitespace_and_comma(self):
        self.assertEqual(split_words("a b,c"), ["a", "b,c"])

    def test_only_commas(self):
        self.assertEqual(split_words("a,b,c,d"), ["a", "b", "c", "d"])

    def test_no_delimiters(self):
        self.assertEqual(split_words("xyz"), 2)

    def test_empty_string(self):
        self.assertEqual(split_words(""), 0)

    def test_mixed_delimiters(self):
        self.assertEqual(split_words("hello world,test"), ["hello", "world,test"])

    def test_numeric_and_letters(self):
        self.assertEqual(split_words("abc123"), 1)

if __name__ == "__main__":
    unittest.main()


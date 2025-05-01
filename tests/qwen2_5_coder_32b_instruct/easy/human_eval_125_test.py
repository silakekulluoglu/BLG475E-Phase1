'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.qwen2_5_coder_32b_instruct.easy.human_eval_125 import split_words

class TestSplitWords(unittest.TestCase):
    def test_split_words_1(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_split_words_2(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_split_words_3(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_split_words_4(self):
        self.assertEqual(split_words("aaabb"), 2)

    def test_split_words_5(self):
        self.assertEqual(split_words(""), 0)

if __name__ == '__main__':
    unittest.main()
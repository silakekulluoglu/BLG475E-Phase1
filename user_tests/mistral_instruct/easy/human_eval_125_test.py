'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from regenerated_codes.mistral_instruct.easy.human_eval_125 import split_words

class TestSplitWords(unittest.TestCase):

    def test_split_words_whitespace_split(self): # Test for splitting by whitespace
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])
        self.assertEqual(split_words("a b c"), ["a", "b", "c"])
        self.assertEqual(split_words("   spaced   words  "), ["spaced", "words"])

    def test_split_words_comma_split(self): # Test for splitting by commas
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])
        self.assertEqual(split_words("apple,banana,cherry"), ["apple", "banana", "cherry"])

    def test_split_words_no_split_count_odds(self):
        self.assertEqual(split_words("abcdef"), 3)     # b,d,f → 1,3,5
        self.assertEqual(split_words("ace"), 0)        # a,c,e → 0,2,4
        self.assertEqual(split_words("xyz"), 2)        # x=23, z=25
        self.assertEqual(split_words("ABCDEF"), 0)     # uppercase letters, no odds
        self.assertEqual(split_words("abcDEF"), 1)     # only 'b' is odd
        self.assertEqual(split_words("123456"), 0)     # no lowercase letters, no odds
        self.assertEqual(split_words("ab1cd2"), 2)     # 'b' and 'd' are odd, '1' and '2' are ignored

    def test_split_words_only_spaces_or_commas(self): # Test for strings with only spaces or commas
        self.assertEqual(split_words(" "), [])
        self.assertEqual(split_words("   "), [])
        self.assertEqual(split_words(","), ["", ""])
        self.assertEqual(split_words(",,,"), ["", "", "", ""])

    def test_split_words_empty_string(self): # Test for empty string
        self.assertEqual(split_words(""), 0)

    def test_split_words_space_and_comma_mixed(self): # Test for mixed spaces and commas
        self.assertEqual(split_words("a,b c"), ["a,b", "c"]) 
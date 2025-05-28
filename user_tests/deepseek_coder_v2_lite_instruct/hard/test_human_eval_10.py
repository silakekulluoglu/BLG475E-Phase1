'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys, os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../../source/deepseek_coder_v2_lite_instruct/hard')
    )
)


from human_eval_10 import make_palindrome


import unittest

class TestMakePalindrome(unittest.TestCase):
    def test_two_chars(self):
        self.assertEqual(make_palindrome("ab"), "aba")
    def test_complex_suffix(self):
        self.assertEqual(make_palindrome("abac"), "abacaba")
    def test_repeated_chars(self):
        self.assertEqual(make_palindrome("aaa"), "aaa")
    def test_palindrome_already(self):
        self.assertEqual(make_palindrome("racecar"), "racecar")
    def test_special_char(self):
        self.assertEqual(make_palindrome("!"), "!")


if __name__ == '__main__':
    unittest.main()

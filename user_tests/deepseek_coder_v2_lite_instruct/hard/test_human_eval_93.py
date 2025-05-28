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

from human_eval_93 import encode

import unittest

class TestEncode(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(encode(""), "")
    def test_punctuation(self):
        self.assertEqual(encode("!?"), "!?")
    def test_swap_and_shift(self):
        self.assertEqual(encode("AbE"), "cBg")
    def test_long_string(self):
        self.assertEqual(encode("helloWORLD"), "HGLLQwqrld")
    def test_repeated_vowels(self):
        self.assertEqual(encode("AEIOUaeiou"), "cgkqwCGKQW")

if __name__ == '__main__':
    unittest.main()
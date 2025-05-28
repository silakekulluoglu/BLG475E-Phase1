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

from human_eval_78 import hex_key

import unittest

class TestHexKey(unittest.TestCase):
    def test_repeated_primes(self):
        self.assertEqual(hex_key("B2B2"), 4)
    def test_no_primes(self):
        self.assertEqual(hex_key("ACEF"), 0)
    def test_mixed(self):
        self.assertEqual(hex_key("123456"), 3)
    def test_empty(self):
        self.assertEqual(hex_key(""), 0)
    def test_full_range(self):
        self.assertEqual(hex_key("0123456789ABCDEF"), 6)


if __name__ == '__main__':
    unittest.main()

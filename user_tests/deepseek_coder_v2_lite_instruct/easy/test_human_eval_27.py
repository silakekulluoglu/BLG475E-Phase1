'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../../source/deepseek_coder_v2_lite_instruct/easy')
    )
)

from human_eval_27 import flip_case

import unittest

class TestFlipCase(unittest.TestCase):
    def test_all_lowercase(self):
        self.assertEqual(flip_case('lowercase'), 'LOWERCASE')

    def test_all_uppercase(self):
        self.assertEqual(flip_case('UPPERCASE'), 'uppercase')

    def test_alphanumeric(self):
        self.assertEqual(flip_case('a1B2c3'), 'A1b2C3')

    def test_whitespace_only(self):
        self.assertEqual(flip_case('   '), '   ')

    def test_multiline_string(self):
        self.assertEqual(flip_case('Line1\nLine2'), 'lINE1\nlINE2')

    def test_unicode_characters(self):
        self.assertEqual(flip_case('üÖ'), 'Üö')

if __name__ == "__main__":
    unittest.main()


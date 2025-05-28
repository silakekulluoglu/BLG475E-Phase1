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

from human_eval_86 import anti_shuffle


import unittest

class TestAntiShuffle(unittest.TestCase):
    def test_leading_trailing_spaces(self):
        self.assertEqual(anti_shuffle('  bca abc  '), '  abc abc  ')

    def test_multiple_spaces_between_words(self):
        self.assertEqual(anti_shuffle('aa  bb'), 'aa  bb')

    def test_punctuation_words(self):
        self.assertEqual(anti_shuffle('!! ??'), '!! ??')

    def test_empty_string(self):
        self.assertEqual(anti_shuffle(''), '')

    def test_single_word(self):
        self.assertEqual(anti_shuffle('zxy'), 'xyz')

    def test_mixed_case(self):
        self.assertEqual(anti_shuffle('AbC DeF'), 'ACb DFe')

if __name__ == "__main__":
    unittest.main()


'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys
import os

# Add the path to the source code
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../../source/deepseek_coder_v2_lite_instruct/easy')
    )
)

from human_eval_98 import count_upper


import unittest

class TestCountUpper(unittest.TestCase):
    def test_no_vowels(self):
        self.assertEqual(count_upper('BCDFG'), 0)

    def test_lowercase_vowels(self):
        self.assertEqual(count_upper('aeiouAEIOU'), 2)

    def test_uppercase_vowels_even_positions(self):
        self.assertEqual(count_upper('A_X_E'), 2)

    def test_uppercase_vowels_odd_positions(self):
        self.assertEqual(count_upper('XEAXX'), 1)

    def test_mixed_characters(self):
        self.assertEqual(count_upper('1A2E3I4O5U'), 0)

    def test_empty_string(self):
        self.assertEqual(count_upper(''), 0)


if __name__ == "__main__":
    unittest.main()

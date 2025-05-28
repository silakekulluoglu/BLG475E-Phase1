'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys, os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../../source/deepseek_coder_v2_lite_instruct/moderate')
    )
)


from human_eval_51 import remove_vowels

import unittest

class TestRemoveVowels(unittest.TestCase):
    def test_uppercase_vowels(self):
        self.assertEqual(remove_vowels('AEIOU'), '')

    def test_mixed_content(self):
        self.assertEqual(remove_vowels('H3ll0 W0rld!'), 'H3ll0 W0rld!')

    def test_newlines_and_tabs(self):
        self.assertEqual(remove_vowels("a\te\ni\n"), "\t\n\n")

    def test_unicode_vowels(self):
        self.assertEqual(remove_vowels('ĀāÉé'), 'ĀāÉé')
            
if __name__ == '__main__':
    unittest.main()

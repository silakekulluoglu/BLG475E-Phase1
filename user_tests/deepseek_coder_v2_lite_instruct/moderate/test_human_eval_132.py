'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys, os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '/regenerated_codes/deepseek_coder_v2_lite_instruct/moderate')
    )
)


from human_eval_132 import is_nested

import unittest

class TestIsNested(unittest.TestCase):
    def test_single_pair(self):
        self.assertFalse(is_nested('[]'))

    def test_deep_nesting(self):
        self.assertTrue(is_nested('[[[]]]'))

    def test_alternating(self):
        self.assertFalse(is_nested('[][][][]'))

        

if __name__ == '__main__':
    unittest.main()

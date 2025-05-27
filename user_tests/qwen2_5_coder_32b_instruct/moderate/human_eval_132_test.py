"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from source.qwen2_5_coder_32b_instruct.moderate.human_eval_132 import is_nested

class TestIsNested(unittest.TestCase):
    # ===============================
    # Prompt-specified core test cases
    # ===============================

    def test_is_nested_1(self):
        self.assertEqual(is_nested('[[]]'), True)

    def test_is_nested_2(self):
        self.assertEqual(is_nested('[]]]]]]][[[[[]'), False)

    def test_is_nested_3(self):
        self.assertEqual(is_nested('[][]'), False)

    def test_is_nested_4(self):
        self.assertEqual(is_nested('[]'), False)

    def test_is_nested_5(self):
        self.assertEqual(is_nested('[[[[]]]]'), True)

    def test_is_nested_6(self):
        self.assertEqual(is_nested('[]]]]]]]]]]'), False)

    def test_is_nested_7(self):
        self.assertEqual(is_nested('[][][[]]'), True)

    def test_is_nested_8(self):
        self.assertEqual(is_nested('[[]'), False)

    def test_is_nested_9(self):
        self.assertEqual(is_nested('[]]'), False)

    def test_is_nested_10(self):
        self.assertEqual(is_nested('[[]][['), True)

    def test_is_nested_11(self):
        self.assertEqual(is_nested('[[][]]'), True)

    def test_is_nested_12_empty(self):
        self.assertEqual(is_nested(''), False)

    def test_is_nested_13_all_open(self):
        self.assertEqual(is_nested('[[[[[[[['), False)

    def test_is_nested_14_all_close(self):
        self.assertEqual(is_nested(']]]]]]]]'), False)

    # ===============================
    # Additional edge cases
    # ===============================

    # Extra-deep nesting
    def test_is_nested_15_extra_deep(self):
        self.assertEqual(is_nested('[[[[[[[[]]]]]]]]'), True)

    # Multiple independent nested blocks
    def test_is_nested_16_multiple_nested_blocks(self):
        self.assertEqual(is_nested('[[]][[[]]]'), True)

    # Valid nesting amidst unmatched junk
    def test_is_nested_17_valid_amidst_invalid(self):
        self.assertEqual(is_nested(']]][[[]]]]]['), True)

    # Long flat sequence of brackets — no nesting
    def test_is_nested_18_long_flat(self):
        self.assertEqual(is_nested('[]' * 500), False)

    # Very long, fully nested sequence
    def test_is_nested_19_long_nested(self):
        self.assertEqual(is_nested('[' * 100 + ']' * 100), True)

if __name__ == '__main__':
    unittest.main()

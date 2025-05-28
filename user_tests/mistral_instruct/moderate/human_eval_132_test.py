'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import List, Optional
from regenerated_codes.mistral_instruct.moderate.human_eval_132 import is_nested


class TestIsNested(unittest.TestCase):
    def test_simple_nested(self):
        self.assertTrue(is_nested('[[]]'))  # Nested brackets inside

    def test_no_nested_but_unbalanced(self):
        self.assertFalse(is_nested('[]]]]]]][[[[[]'))  # Unbalanced, no nested subsequence

    def test_adjacent_pairs_no_nesting(self):
        self.assertFalse(is_nested('[][]'))  # Multiple pairs but no nesting

    def test_single_pair(self):
        self.assertFalse(is_nested('[]'))  # Single pair, no nesting

    def test_nested_complex(self):
        self.assertTrue(is_nested('[[][]]'))  # Nested inside a bigger bracket

    def test_partial_nested(self):
        self.assertTrue(is_nested('[[]][['))  # Nested subsequence exists

    def test_empty_string(self):
        self.assertFalse(is_nested(''))  # No brackets at all

    def test_only_open_brackets(self):
        self.assertFalse(is_nested('[[[['))  # No closing brackets, no nesting

    def test_only_close_brackets(self):
        self.assertFalse(is_nested(']]]]'))  # No opening brackets, no nesting

    def test_long_nested(self):
        self.assertTrue(is_nested('[[][][[]]]'))  # Nested multiple levels

    def test_long_no_nesting(self):
        self.assertFalse(is_nested('[][][][][][]'))  # Many pairs but no nesting
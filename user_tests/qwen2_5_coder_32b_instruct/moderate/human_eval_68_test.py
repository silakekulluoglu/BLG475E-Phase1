"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from regenerated_codes.qwen2_5_coder_32b_instruct.moderate.human_eval_68 import pluck

class TestPluck(unittest.TestCase):
    # Two evens: 4 and 2 → choose smallest (2) and its index (1)
    def test_pluck_1(self):
        self.assertEqual(pluck([4, 2, 3]), [2, 1])

    # Only one even → return it
    def test_pluck_2(self):
        self.assertEqual(pluck([1, 2, 3]), [2, 1])

    # Empty input → should return empty list
    def test_pluck_3(self):
        self.assertEqual(pluck([]), [])

    # Two zeros and other evens → choose first 0
    def test_pluck_4(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

    # Smallest even appears after other larger even
    def test_pluck_5(self):
        self.assertEqual(pluck([1, 2, 3, 0, 5, 3]), [0, 3])

    # ===============================
    # Additional test cases
    # ===============================

    # All elements are odd → should return empty list
    def test_pluck_6_all_odds(self):
        self.assertEqual(pluck([1, 3, 5, 7]), [])

    # All elements are even — return smallest one with first index
    def test_pluck_7_all_evens(self):
        self.assertEqual(pluck([8, 6, 4, 2, 0]), [0, 4])

    # Single even element
    def test_pluck_8_one_even(self):
        self.assertEqual(pluck([8]), [8, 0])

    # Single odd element
    def test_pluck_9_one_odd(self):
        self.assertEqual(pluck([3]), [])

    # Very large values included
    def test_pluck_10_large_numbers(self):
        self.assertEqual(pluck([999999, 12345678, 2, 5]), [2, 2])

    # First and last element are equal evens — return the first
    def test_pluck_11_same_even_ends(self):
        self.assertEqual(pluck([4, 9, 7, 4]), [4, 0])

    # Negative number in input — violates prompt
    def test_pluck_12_negative_input(self):
        with self.assertRaises(ValueError):
            pluck([1, -2, 3])

    # Non-integer input (float) — violates prompt
    def test_pluck_13_non_integer(self):
        with self.assertRaises(ValueError):
            pluck([2.5, 4, 6])

    # String element — invalid type
    def test_pluck_14_string_input(self):
        with self.assertRaises(ValueError):
            pluck(["2", 4, 6])

if __name__ == '__main__':
    unittest.main()

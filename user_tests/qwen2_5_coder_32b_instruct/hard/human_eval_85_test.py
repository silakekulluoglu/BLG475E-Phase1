"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from source.qwen2_5_coder_32b_instruct.hard.human_eval_85 import add

class TestAdd(unittest.TestCase):
    # Even number at odd index → 88
    def test_add_1(self):
        self.assertEqual(add([4, 88]), 88)

    # Only 122 at index 5 is even and odd-indexed
    def test_add_2(self):
        self.assertEqual(add([4, 5, 6, 7, 2, 122]), 122)

    # Even zero at index 1 → sum = 0
    def test_add_3(self):
        self.assertEqual(add([4, 0, 6, 7]), 0)

    # Even numbers at indices 1 and 3 → 4 + 8 = 12
    def test_add_4(self):
        self.assertEqual(add([4, 4, 6, 8]), 12)

    # Even values at indices 1, 3, 5 → 2 + 4 + 6 = 12
    def test_add_5(self):
        self.assertEqual(add([1, 2, 3, 4, 5, 6]), 12)

    # ===============================
    # Additional test cases
    # ===============================

    # Only one element → no odd indices
    def test_add_single_element(self):
        self.assertEqual(add([5]), 0)

    # All odd-indexed elements are odd → total = 0
    def test_add_all_odds_at_odd_indices(self):
        self.assertEqual(add([0, 1, 2, 3, 4, 5]), 0)

if __name__ == '__main__':
    unittest.main()

"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from regenerated_codes.qwen2_5_coder_32b_instruct.hard.human_eval_20 import find_closest_elements

class TestFindClosestElements(unittest.TestCase):
    # Only two values — minimal valid input
    def test_minimal_input(self):
        self.assertEqual(find_closest_elements([3.5, 3.6]), (3.5, 3.6))

    # Duplicate numbers — distance is zero
    def test_duplicates(self):
        self.assertEqual(find_closest_elements([5.0, 5.0, 6.0]), (5.0, 5.0))

    # Closest pair at start
    def test_closest_pair_at_start(self):
        self.assertEqual(find_closest_elements([1.0, 1.1, 3.0, 5.0]), (1.0, 1.1))

    # Closest pair at end
    def test_closest_pair_at_end(self):
        self.assertEqual(find_closest_elements([3.0, 5.0, 6.0, 6.1]), (6.0, 6.1))

    # Closest pair is among negatives
    def test_negative_closest_pair(self):
        self.assertEqual(find_closest_elements([-5.0, -4.9, 0.0]), (-5.0, -4.9))

    # ===============================
    # Additional test cases
    # ===============================

    # Mixed signs — should not cross zero
    def test_mixed_signs(self):
        self.assertEqual(find_closest_elements([-2.0, -1.0, 1.0, 2.1]), (-2.0, -1.0))

    # High precision float pair
    def test_float_precision(self):
        self.assertEqual(find_closest_elements([1.0000001, 1.0000002, 2.0]), (1.0000001, 1.0000002))

    # Reversed sorted input
    def test_reverse_sorted(self):
        self.assertEqual(find_closest_elements([9.0, 8.0, 6.8]), (8.0, 9.0))

    # Large magnitude float values
    def test_large_values(self):
        self.assertEqual(find_closest_elements([1e9, 1e9 + 1, 2e9]), (1e9, 1e9 + 1))

    # Zero should be handled correctly
    def test_with_zeros(self):
        self.assertEqual(find_closest_elements([0.0, 0.1, 1.0]), (0.0, 0.1))

    # Pair of equal values among other distant numbers
    def test_with_two_equal_among_many(self):
        self.assertEqual(find_closest_elements([10.0, 20.0, 30.0, 20.0]), (20.0, 20.0))

    # Invalid input: multiple pairs have the same minimum distance
    def test_ambiguous_pair_should_fail(self):
        with self.assertRaises(ValueError):
            find_closest_elements([1.0, 2.0, 3.0, 4.0])


if __name__ == '__main__':
    unittest.main()

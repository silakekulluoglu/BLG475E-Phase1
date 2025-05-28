'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import List
from regenerated_codes.mistral_instruct.moderate.human_eval_21 import rescale_to_unit

class TestRescale(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(
            rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]),
            [0.0, 0.25, 0.5, 0.75, 1.0]
        )

    def test_two_elements(self):
        self.assertEqual(
            rescale_to_unit([10.0, 20.0]),
            [0.0, 1.0]
        )

    def test_negative_values(self):
        self.assertEqual(
            rescale_to_unit([-5.0, 0.0, 5.0]),
            [0.0, 0.5, 1.0]
        )

    def test_all_same_values(self):
        self.assertEqual(
            rescale_to_unit([3.3, 3.3, 3.3]),
            [0.0, 0.0, 0.0]
        )

    def test_large_numbers(self):
        self.assertEqual(
            rescale_to_unit([1000000.0, 5000000.0]),
            [0.0, 1.0]
        )

    def test_floating_point_precision(self):
        result = rescale_to_unit([0.1, 0.2, 0.3])
        expected = [0.0, 0.5, 1.0]
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e)

    def test_duplicate_values(self):
        self.assertEqual(
            rescale_to_unit([1.0, 2.0, 2.0, 3.0]),
            [0.0, 0.5, 0.5, 1.0]
        )

    def test_min_max_reverse_order(self):
        self.assertEqual(
            rescale_to_unit([10.0, 0.0]),
            [1.0, 0.0]
        )
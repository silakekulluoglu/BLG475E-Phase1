"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from regenerated_codes.qwen2_5_coder_32b_instruct.moderate.human_eval_148 import bf

class TestBf(unittest.TestCase):
    # ===============================
    # Prompt test cases
    # ===============================

    def test_bf_1(self):
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))

    def test_bf_2(self):
        self.assertEqual(bf("Earth", "Mercury"), ("Venus",))

    def test_bf_3(self):
        self.assertEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))

    def test_bf_4(self):
        self.assertEqual(bf("Neptune", "Venus"), ("Earth", "Mars", "Jupiter", "Saturn", "Uranus"))

    def test_bf_5(self):
        self.assertEqual(bf("Earth", "Earth"), ())

    # ===============================
    # Additional test cases
    # ===============================

    # Canonical test: adjacent planets — should return empty
    def test_bf_6_adjacent_planets(self):
        self.assertEqual(bf("Mars", "Earth"), ())

    # Canonical test: invalid second planet
    def test_bf_7_invalid_planet_name(self):
        self.assertEqual(bf("Jupiter", "Makemake"), ())

    # Both inputs invalid
    def test_bf_8_both_invalid(self):
        self.assertEqual(bf("Ceres", "Pluto"), ())

    # One valid, one invalid
    def test_bf_9_one_invalid(self):
        self.assertEqual(bf("Earth", "Eris"), ())

    # Full solar span
    def test_bf_10_all_between(self):
        self.assertEqual(bf("Mercury", "Neptune"),
                         ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"))

    # Edge adjacent case — no planets between
    def test_bf_11_just_adjacent(self):
        self.assertEqual(bf("Venus", "Earth"), ())

if __name__ == '__main__':
    unittest.main()

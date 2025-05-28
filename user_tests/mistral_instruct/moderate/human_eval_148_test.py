'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from typing import Tuple, List
from regenerated_codes.mistral_instruct.moderate.human_eval_148 import bf

class TestBF(unittest.TestCase):
    def test_planets_in_order(self):
        self.assertEqual(
            bf("Jupiter", "Neptune"),
            ("Saturn", "Uranus")
        )
    
    def test_planets_reverse_order(self):
        self.assertEqual(
            bf("Earth", "Mercury"),
            ("Venus",)
        )
    
    def test_multiple_planets_between(self):
        self.assertEqual(
            bf("Mercury", "Uranus"),
            ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
        )
    
    def test_same_planet(self):
        self.assertEqual(
            bf("Earth", "Earth"),
            ()
        )
    
    def test_invalid_planet1(self):
        self.assertEqual(
            bf("Pluto", "Earth"),
            ()
        )
    
    def test_invalid_planet2(self):
        self.assertEqual(
            bf("Earth", "Pluto"),
            ()
        )
    
    def test_invalid_both_planets(self):
        self.assertEqual(
            bf("X", "Y"),
            ()
        )
    
    def test_adjacent_planets(self):
        self.assertEqual(
            bf("Venus", "Earth"),
            ()
        )
    
    def test_full_range(self):
        self.assertEqual(
            bf("Mercury", "Neptune"),
            ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
        )
    
    def test_lowercase_input(self):
        self.assertEqual(
            bf("mercury", "uranus"),
            ()  # Assuming case-sensitive, returns empty tuple
        )
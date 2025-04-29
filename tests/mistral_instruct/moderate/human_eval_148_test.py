import unittest
from typing import Tuple, List
from source.mistral_instruct.moderate.human_eval_148 import bf

class TestBF(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_bf_invalid_planet1(self):
        expected = tuple()
        planet1 = "Invalid Planet"
        result = bf(planet1, "Earth")
        self.assertEqual(result, expected)

    def test_bf_invalid_planet2(self):
        expected = tuple()
        planet2 = "Invalid Planet"
        result = bf("Mercury", planet2)
        self.assertEqual(result, expected)

    def test_bf_valid_adjacent_planets(self):
        expected = ["Venus"]
        planet1 = "Mercury"
        planet2 = "Venus"
        result = bf(planet1, planet2)
        self.assertEqual(result, expected)

    def test_bf_valid_nonadjacent_planets(self):
        expected = ["Mars", "Astronaut"]
        planet1 = "Mercury"
        planet2 = "Mars"
        result = bf(planet1, planet2)
        self.assertEqual(result, expected)

    def test_bf_multiple_planets(self):
        expected = ["Venus", "Earth"]
        planet1 = "Mercury"
        planet2 = "Mars"
        result = bf(planet1, planet2)
        self.assertEqual(result, expected)
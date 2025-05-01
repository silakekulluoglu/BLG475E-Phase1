'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest

class TestBf(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))
        self.assertEqual(bf("Earth", "Mercury"), ("Venus",))

    def test_edge_cases(self):
        self.assertEqual(bf("Earth", "Earth"), ())
        self.assertEqual(bf("Mars", "Earth"), ())
        self.assertEqual(bf("Jupiter", "Makemake"), ())

if __name__ == '__main__':
    unittest.main()

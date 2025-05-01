'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest

class TestRoundedAvg(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")
        self.assertEqual(rounded_avg(7, 13), "0b1010")

    def test_edge_cases(self):
        self.assertEqual(rounded_avg(7, 5), -1)
        self.assertEqual(rounded_avg(5, 1), -1)
        self.assertEqual(rounded_avg(5, 5), "0b101")

if __name__ == "__main__":
    unittest.main()

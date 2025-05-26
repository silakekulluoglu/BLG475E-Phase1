'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from regenerated_codes.mistral_instruct.easy.human_eval_103 import rounded_avg

class TestRoundedAvg(unittest.TestCase):
    def test_rounded_avg_negative_n(self):
        result = rounded_avg(-1, 5)
        self.assertEqual(result, -1)

    def test_rounded_avg_negative_m(self):
        result = rounded_avg(-9, -5)
        self.assertEqual(result, -1)

    def test_rounded_avg_n_greater_m(self):
        result = rounded_avg(92, 55)
        self.assertEqual(result, -1)

    def test_rounded_avg_zero(self):
        result = rounded_avg(0, 0)
        self.assertEqual(result, -1)

    def test_rounded_avg_simple(self):
        result = rounded_avg(3, 5)
        self.assertEqual(result, '0b100')

    def test_rounded_avg_mid(self):
        result = rounded_avg(10, 20)
        self.assertEqual(result, "0b1111")

    def test_rounded_avg_large(self):
        self.assertEqual(rounded_avg(1, 100), "0b110010")

    def test_rounded_avg_exact_middle_value(self):
        result = rounded_avg(20, 33)
        self.assertEqual(result, "0b11010")

    def test_rounded_avg_even_number(self):
        result = rounded_avg(4, 5)
        self.assertEqual(result, '0b100')

    def test_even_average_rounding(self):
        self.assertEqual(rounded_avg(1, 2), "0b10") 

    def test_rounding_down(self):
        self.assertEqual(rounded_avg(1, 4), "0b10") 
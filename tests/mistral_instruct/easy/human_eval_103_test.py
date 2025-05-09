'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.mistral_instruct.easy.human_eval_103 import rounded_avg

class TestRoundedAvg(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_rounded_avg_negative_n(self):
        result = rounded_avg(-1, 5)
        self.assertEqual(result, -1)

    def test_rounded_avg_zero(self):
        result = rounded_avg(0, 0)
        self.assertEqual(result, -1)

    def test_rounded_avg_simple(self):
        result = rounded_avg(3, 5)
        self.assertEqual(result, '1011')

    def test_rounded_avg_large(self):
        result = rounded_avg(2678, 2690)
        self.assertEqual(result, '1011011000')

    def test_rounded_avg_even_number(self):
        result = rounded_avg(4, 5)
        self.assertEqual(result, '1100')
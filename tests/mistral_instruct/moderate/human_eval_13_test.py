'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.mistral_instruct.moderate.human_eval_13 import greatest_common_divisor

class TestGCD(unittest.TestCase):
    def setUp(self):
        pass  # Setup any test fixtures here if needed

    def tearDown(self):
        pass  # Clean up after the tests run here if needed

    def test_gcd_same_number(self):
        result = greatest_common_divisor(10, 10)
        self.assertEqual(result, 10)

    def test_gcd_simple_case(self):
        result = greatest_common_divisor(24, 18)
        self.assertEqual(result, 6)

    def test_gcd_large_number(self):
        result = greatest_common_divisor(7654321, 4321765)
        self.assertEqual(result, 1369)

    def test_gcd_negative_numbers(self):
        result = greatest_common_divisor(-24, -18)
        self.assertEqual(result, 18)

    def test_gcd_zero(self):
        with self.assertRaises(TypeError):
            greatest_common_divisor(0, 5)  # Replace 'any_integer' with an appropriate value to raise the TypeError

'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from regenerated_codes.mistral_instruct.easy.human_eval_2 import truncate_number

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_zero1(self): # Test for zero as an integer
        with self.assertRaises(ValueError):
            truncate_number(0)

    def test_truncate_zero2(self): # Test for zero as a float
        with self.assertRaises(ValueError):
            truncate_number(0.0)

    def test_truncate_positive(self): # Test for positive float values
        test_cases = [
            (0.1, 0.1),
            (1.5, 0.5),
            (2.75, 0.75),
            (3.0, 0.0),
            (100.99, 0.99),
        ]
        for input_val, expected in test_cases:
            with self.subTest(input=input_val):
                self.assertAlmostEqual(truncate_number(input_val), expected) # Use assertAlmostEqual for float comparison

    def test_truncate_multiple_negatives(self): # Test for multiple negative float values
        negative_values = [-0.1, -1.0, -123.456, -9999]
        for value in negative_values:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    truncate_number(value)

    def test_truncate_integer(self): # Test for integer values
        result = truncate_number(5)
        self.assertEqual(result, 0.0)

if __name__ == "__main__":
    unittest.main()
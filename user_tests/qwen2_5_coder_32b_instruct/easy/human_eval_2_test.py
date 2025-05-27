"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from regenerated_codes.qwen2_5_coder_32b_instruct.easy.human_eval_2 import truncate_number

class TestTruncateNumber(unittest.TestCase):
    # Standard float with decimal part
    def test_truncate_number_1(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5)

    # Float with two decimal digits
    def test_truncate_number_2(self):
        self.assertAlmostEqual(truncate_number(1.33), 0.33)

    # Large number with decimal part
    def test_truncate_number_3(self):
        self.assertAlmostEqual(truncate_number(123.456), 0.456)

    # Edge case: number very close to 1
    def test_truncate_number_4(self):
        self.assertAlmostEqual(truncate_number(0.999), 0.999)

    # Edge case: integer-like float, no decimal part
    def test_truncate_number_5(self):
        self.assertAlmostEqual(truncate_number(10.0), 0.0)

    # ===============================
    # Additional test cases
    # ===============================

    # Invalid input: 0.0 would raise ValueError if enforced
    def test_truncate_number_9_negative(self):
        with self.assertRaises(ValueError):
            truncate_number(0.0)

    # Very small float value — should return itself
    def test_truncate_number_7_very_small(self):
        self.assertAlmostEqual(truncate_number(1e-10), 1e-10)

    # Very large float value with small decimal part — tests float precision
    def test_truncate_number_8_very_large(self):
        self.assertAlmostEqual(truncate_number(1e15 + 0.1), 0.1, places=6)

    # Very large float value with small decimal part — tests float precision
    def test_truncate_number_8_very_large(self):
        with self.assertRaises(ValueError):
            truncate_number(1e16 + 0.1)

    # Invalid input: negative float — would raise ValueError if enforced
    def test_truncate_number_9_negative(self):
        with self.assertRaises(ValueError):
            truncate_number(-3.5)

    # Invalid input: string instead of float — would raise TypeError if enforced
    def test_truncate_number_10_invalid_type(self):
        with self.assertRaises(TypeError):
            truncate_number("3.5")

if __name__ == '__main__':
    unittest.main()

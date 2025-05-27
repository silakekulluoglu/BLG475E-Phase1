"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from source.qwen2_5_coder_32b_instruct.moderate.human_eval_36 import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    # Simple base case — no numbers match, no 7s
    def test_fizz_buzz_1(self):
        self.assertEqual(fizz_buzz(50), 0)

    # Small range, 7s appear in one or more matches
    def test_fizz_buzz_2(self):
        self.assertEqual(fizz_buzz(78), 2)

    # Near 77 → includes 77 which has two 7s
    def test_fizz_buzz_3(self):
        self.assertEqual(fizz_buzz(79), 3)

    # Standard range check
    def test_fizz_buzz_4(self):
        self.assertEqual(fizz_buzz(100), 3)

    # Larger span check
    def test_fizz_buzz_5(self):
        self.assertEqual(fizz_buzz(200), 6)

    # ===============================
    # Additional test cases
    # ===============================

    # Zero boundary — no numbers processed
    def test_fizz_buzz_6_zero(self):
        self.assertEqual(fizz_buzz(0), 0)

    # Minimal non-zero — should still return 0
    def test_fizz_buzz_7_one(self):
        self.assertEqual(fizz_buzz(1), 0)

    # Edge case: divisible by both 11 and 13 (LCM = 143)
    def test_fizz_buzz_8_lcm_11_13(self):
        result = fizz_buzz(144)  # includes 143 which may contain 7
        self.assertTrue(isinstance(result, int))

    # Number with repeated 7s like 77, 707
    def test_fizz_buzz_9_multiple_7s_same_number(self):
        self.assertGreaterEqual(fizz_buzz(800), 4)

    # Prime number input with no divisible hits
    def test_fizz_buzz_10_prime_high(self):
        self.assertEqual(fizz_buzz(17), 0)

    # Large number for runtime stress
    def test_fizz_buzz_11_large_input(self):
        result = fizz_buzz(5000)
        self.assertTrue(isinstance(result, int))  # check stability

    # Negative input — not defined by prompt, currently returns 0
    def test_fizz_buzz_12_negative(self):
        self.assertEqual(fizz_buzz(-100), 0)  # implicit behavior

if __name__ == '__main__':
    unittest.main()

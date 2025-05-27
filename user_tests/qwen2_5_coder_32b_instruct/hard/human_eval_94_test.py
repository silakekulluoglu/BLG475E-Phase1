"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from regenerated_codes.qwen2_5_coder_32b_instruct.hard.human_eval_94 import skjkasdkd

class TestSkjkasdkd(unittest.TestCase):
    # Largest prime is 181 → 1+8+1 = 10
    def test_skjkasdkd_1(self):
        self.assertEqual(skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]), 10)

    # Largest prime is 4597 → 4+5+9+7 = 25
    def test_skjkasdkd_2(self):
        self.assertEqual(skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]), 25)

    # Largest prime is 5107 → 5+1+0+7 = 13
    def test_skjkasdkd_3(self):
        self.assertEqual(skjkasdkd([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]), 13)

    # Largest prime is 83 → 8+3 = 11
    def test_skjkasdkd_4(self):
        self.assertEqual(skjkasdkd([0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6]), 11)

    # Largest prime is 3 → sum = 3
    def test_skjkasdkd_5(self):
        self.assertEqual(skjkasdkd([0, 81, 12, 3, 1, 21]), 3)

    # Largest prime is 7 → sum = 7
    def test_skjkasdkd_6(self):
        self.assertEqual(skjkasdkd([0, 8, 1, 2, 1, 7]), 7)

    # Single prime number (8191) → 8+1+9+1 = 19
    def test_skjkasdkd_single_large_prime(self):
        self.assertEqual(skjkasdkd([8191]), 19)

    # 8191 is largest prime, ignore others → 19
    def test_skjkasdkd_largest_in_mixed(self):
        self.assertEqual(skjkasdkd([8191, 123456, 127, 7]), 19)

    # 127 is largest prime → 1+2+7 = 10
    def test_skjkasdkd_tie_or_smaller_primes(self):
        self.assertEqual(skjkasdkd([127, 97, 8192]), 10)

    # ===============================
    # Additional test cases
    # ===============================

    # Only one element and it's not a prime → 0 is expected (based on implementation behavior)
    def test_single_non_prime(self):
        self.assertEqual(skjkasdkd([1]), 0)

    # Empty list → no prime → sum should be 0
    def test_empty_list(self):
        self.assertEqual(skjkasdkd([]), 0)

    # Negative numbers → should be ignored
    def test_with_negatives(self):
        self.assertEqual(skjkasdkd([-5, -7, 2, 3]), 3)  # largest prime = 3 → sum = 3

    # All non-primes → should return 0
    def test_all_non_primes(self):
        self.assertEqual(skjkasdkd([0, 1, 4, 6, 8, 9, 10]), 0)

if __name__ == '__main__':
    unittest.main()

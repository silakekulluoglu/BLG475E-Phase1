"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from source.qwen2_5_coder_32b_instruct.hard.human_eval_78 import hex_key

class TestHexKey(unittest.TestCase):
    # Input: "AB" → only 'B' is a hex-prime (decimal 11)
    def test_hex_key_1(self):
        self.assertEqual(hex_key("AB"), 1)

    # Input: "1077E" → primes = 7, 7 → total = 2
    def test_hex_key_2(self):
        self.assertEqual(hex_key("1077E"), 2)

    # Input: "ABED1A33" → primes = 3, 3, B, D → total = 4
    def test_hex_key_3(self):
        self.assertEqual(hex_key("ABED1A33"), 4)

    # Input: "2020" → primes = 2, 2 → total = 2
    def test_hex_key_4(self):
        self.assertEqual(hex_key("2020"), 2)

    # Full hex range → primes: 2, 3, 5, 7, B, D → total = 6
    def test_hex_key_5(self):
        self.assertEqual(hex_key("123456789ABCDEF0"), 6)

    # ===============================
    # Additional test cases
    # ===============================

    # Very long hex string with multiple repeats
    def test_hex_key_long_repeated(self):
        self.assertEqual(hex_key("112233445566778899AABBCCDDEEFF00"), 12)

    # All hex prime digits only
    def test_hex_key_all_primes(self):
        self.assertEqual(hex_key("2357BD"), 6)

    # All non-prime hex digits → total should be 0
    def test_hex_key_all_non_primes(self):
        self.assertEqual(hex_key("014689ACEF"), 0)

    # Empty string input → total = 0
    def test_hex_key_empty(self):
        self.assertEqual(hex_key(""), 0)

if __name__ == '__main__':
    unittest.main()

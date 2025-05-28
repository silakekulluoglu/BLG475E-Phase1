"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from regenerated_codes.qwen2_5_coder_32b_instruct.hard.human_eval_93 import encode

class TestEncode(unittest.TestCase):
    # 'TEST' → swapcase = 'test' → replace 'e' → 'g' → 'tgst'
    def test_encode_1(self):
        self.assertEqual(encode('TEST'), 'tgst')

    # 'Mudasir' → swapcase → 'mUDASIR' → vowels: 'U', 'A', 'I' → 'W', 'C', 'K' → 'mWDCSKR'
    def test_encode_2(self):
        self.assertEqual(encode('Mudasir'), 'mWDCSKR')

    # 'YES' → swapcase = 'yes' → 'e' becomes 'g' → 'ygs'
    def test_encode_3(self):
        self.assertEqual(encode('YES'), 'ygs')

    # Full sentence with spacing
    def test_encode_4(self):
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

    # Sentence with mixed cases and spacing — validate precise letter changes
    def test_encode_5(self):
        self.assertEqual(encode("I DoNt KnOw WhAt tO WrItE"), 'k dQnT kNqW wHcT Tq wRkTg')

    # ===============================
    # Additional test cases
    # ===============================

    # Empty string should return empty string
    def test_encode_empty(self):
        self.assertEqual(encode(""), "")

    # No vowels at all
    def test_encode_no_vowels(self):
        self.assertEqual(encode("BCDFG"), "bcdfg")

    # Only vowels — test replacements and case swap
    def test_encode_only_vowels(self):
        self.assertEqual(encode("aeiouAEIOU"), "CGKQWcgkqw")

if __name__ == '__main__':
    unittest.main()

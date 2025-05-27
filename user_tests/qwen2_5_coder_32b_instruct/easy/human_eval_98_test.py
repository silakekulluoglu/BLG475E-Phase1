"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from regenerated_codes.qwen2_5_coder_32b_instruct.easy.human_eval_98 import count_upper

class TestCountUpper(unittest.TestCase):
    # Only one uppercase vowel at index 4 → count is 1
    def test_count_upper_1(self):
        self.assertEqual(count_upper('aBCdEf'), 1)

    # No uppercase vowels at even indices → count is 0
    def test_count_upper_2(self):
        self.assertEqual(count_upper('abcdefg'), 0)

    # Uppercase vowels exist but only at odd indices → count is 0
    def test_count_upper_3(self):
        self.assertEqual(count_upper('dBBE'), 0)

    # Single uppercase consonant → not a vowel → count is 0
    def test_count_upper_4(self):
        self.assertEqual(count_upper('B'), 0)

    # Single uppercase vowel at index 0 → count is 1
    def test_count_upper_5(self):
        self.assertEqual(count_upper('U'), 1)

    # ===============================
    # Additional test cases
    # ===============================

    # Empty string should return 0
    def test_count_upper_6_empty(self):
        self.assertEqual(count_upper(''), 0)

    # Multiple uppercase vowels at even indices
    def test_count_upper_7_multiple_valid(self):
        self.assertEqual(count_upper('AEIOUB'), 3)  # A (0), I (2), U (4)

    # Uppercase vowels at odd indices → should not count
    def test_count_upper_8_odd_index_vowels(self):
        self.assertEqual(count_upper('aAeEiIoOuU'), 0)

    # Lowercase vowels at even indices → should not count
    def test_count_upper_9_lowercase_even_index(self):
        self.assertEqual(count_upper('aeiouAEIOU'), 2)  # Only A (5), U (9)

    # Non-letter characters — should be ignored
    def test_count_upper_10_symbols_and_digits(self):
        self.assertEqual(count_upper('U2E@O!'), 3)

    # Unicode / accented characters — should not match any uppercase vowel
    def test_count_upper_11_unicode(self):
        self.assertEqual(count_upper('ÁÉÍÓÚ'), 0)

if __name__ == '__main__':
    unittest.main()

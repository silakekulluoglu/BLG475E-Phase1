"""
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
"""

import unittest
from regenerated_codes.qwen2_5_coder_32b_instruct.easy.human_eval_27 import flip_case

class TestFlipCase(unittest.TestCase):
    # Empty string — should return empty string
    def test_flip_case_1(self):
        self.assertEqual(flip_case(''), '')

    # Mixed case with punctuation
    def test_flip_case_2(self):
        self.assertEqual(flip_case('Hello!'), 'hELLO!')

    # Long sentence with spaces and mixed case
    def test_flip_case_3(self):
        self.assertEqual(flip_case('These violent delights have violent ends'), 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS')

    # Alphanumeric mix
    def test_flip_case_4(self):
        self.assertEqual(flip_case('Python3.8'), 'pYTHON3.8')

    # Mixed case with numbers at beginning
    def test_flip_case_5(self):
        self.assertEqual(flip_case('123abcXYZ'), '123ABCxyz')

    # ===============================
    # Additional test cases
    # ===============================

    # All lowercase — should become all uppercase
    def test_flip_case_6_all_lower(self):
        self.assertEqual(flip_case('abcdef'), 'ABCDEF')

    # All uppercase — should become all lowercase
    def test_flip_case_7_all_upper(self):
        self.assertEqual(flip_case('ABCDEF'), 'abcdef')

    # Digits only — should remain unchanged
    def test_flip_case_8_digits_only(self):
        self.assertEqual(flip_case('1234567890'), '1234567890')

    # Symbols only — should remain unchanged
    def test_flip_case_9_symbols_only(self):
        self.assertEqual(flip_case('!?@#$%^&*()_+=-'), '!?@#$%^&*()_+=-')

    # Single-character variations
    def test_flip_case_10_single_chars(self):
        self.assertEqual(flip_case('a'), 'A')
        self.assertEqual(flip_case('A'), 'a')
        self.assertEqual(flip_case('1'), '1')
        self.assertEqual(flip_case('@'), '@')

if __name__ == '__main__':
    unittest.main()

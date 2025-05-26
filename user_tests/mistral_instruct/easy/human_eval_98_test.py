'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from regenerated_codes.mistral_instruct.easy.human_eval_98 import count_upper

class TestCountUpper(unittest.TestCase):
    def test_count_upper_empty(self):
        result = count_upper('')
        self.assertEqual(result, 0)

    def test_count_upper_single_uppercase_vowel_even_index(self):
        result = count_upper('A') 
        self.assertEqual(result, 1)

    def test_count_upper_single_uppercase_vowel_odd_index(self):
        result = count_upper('bA')
        self.assertEqual(result, 0)

    def test_count_upper_odd_number_of_letters(self):
        result = count_upper('OUI')
        self.assertEqual(result, 2)

    def test_count_upper_mixed_case(self):
        result = count_upper('ioUaEo')
        self.assertEqual(result, 2)

    def test_count_upper_no_vowels(self):
        result = count_upper('BCDFGH')
        self.assertEqual(result, 0)

    def test_count_upper_vowels_but_lowercase(self):
        result = count_upper('aeiouAEIOU')
        self.assertEqual(result, 2)

    def test_count_upper_with_non_alpha_chars(self):
        result = count_upper('A1E!I?O#U') 
        self.assertEqual(result, 5)

    def test_count_upper_long_string(self):
        result = count_upper('ABCDEFGHIJKLMNOPQRSTUVWXYZAEIOU')
        self.assertEqual(result, 8)  
'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from regenerated_codes.mistral_instruct.easy.human_eval_86 import anti_shuffle

class TestAntiShuffle(unittest.TestCase):
    def test_anti_shuffle_empty(self): # Test case for an empty string
        result = anti_shuffle('')
        self.assertEqual(result, '')

    def test_anti_shuffle_single_word(self): # Test case for a single word
        result = anti_shuffle('hello')
        expected_output = 'ehllo'
        self.assertEqual(result, expected_output)

    def test_anti_shuffle_multiple_words(self):  # Test case for multiple words
        result = anti_shuffle("I am a programmer")
        expected_output = "I am a aegmmoprrr"
        self.assertEqual(result, expected_output)

    def test_anti_shuffle_mixed_case(self): # Test case for mixed case letters
        result = anti_shuffle("HELLO WORLD")
        expected_output = "EHLLO DLORW"
        self.assertEqual(result, expected_output)

    def test_anti_shuffle_special_characters(self): # Test case for special characters
        result = anti_shuffle("Hello1World!@#$%")
        expected_output = "!#$%1@HWdellloor"
        self.assertEqual(result, expected_output)

    def test_anti_shuffle_multiple_spaces(self): # Test case for multiple spaces
        result = anti_shuffle("  double   space ")
        expected_output = "  bdelou   aceps "  
        self.assertEqual(result, expected_output)

    def test_anti_shuffle_single_char_words(self):  # Test case for single character words
        result = anti_shuffle("A B C")
        expected_output = "A B C"
        self.assertEqual(result, expected_output)
    
    def test_anti_shuffle_only_spaces(self):  # Test case for a string with only spaces
        result = anti_shuffle("     ")
        expected_output = "     "
        self.assertEqual(result, expected_output)
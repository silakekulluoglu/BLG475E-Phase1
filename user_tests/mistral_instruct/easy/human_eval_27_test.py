'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
import string
from regenerated_codes.mistral_instruct.easy.human_eval_27 import flip_case

class TestFlipCase(unittest.TestCase):
    def test_flip_lowercase(self):  # Test with all lowercase letters
        input_string = "hello world"
        result = flip_case(input_string)
        expected_output = "HELLO WORLD"
        self.assertEqual(result, expected_output)

    def test_flip_uppercase(self):  # Test with all uppercase letters
        input_string = "HELLO WORLD"
        result = flip_case(input_string)
        expected_output = "hello world"
        self.assertEqual(result, expected_output)

    def test_flip_mixed_case(self): # Test with a mix of uppercase and lowercase letters
        input_string = "HeLLo wOrLd"
        result = flip_case(input_string)
        expected_output = "hEllO WoRlD"
        self.assertEqual(result, expected_output)

    def test_flip_empty_string(self): # Test with an empty string
        input_string = ""
        result = flip_case(input_string)
        expected_output = ""
        self.assertEqual(result, expected_output)

    def test_flip_special_characters(self): # Test with special/escape characters
        input_string = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@[\\]^_`{|}~\x7f'
        result = flip_case(input_string)
        expected_output = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@[\\]^_`{|}~\x7f'
        self.assertEqual(result, expected_output)
'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.qwen2_5_coder_32b_instruct.hard.human_eval_93 import encode

class TestEncode(unittest.TestCase):
    def test_encode_1(self):
        self.assertEqual(encode('TEST'), 'tgst')

    def test_encode_2(self):
        self.assertEqual(encode('Mudasir'), 'mWDCSKR')

    def test_encode_3(self):
        self.assertEqual(encode('YES'), 'ygs')

    def test_encode_4(self):
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

    def test_encode_5(self):
        self.assertEqual(encode("I DoNt KnOw WhAt tO WrItE"), 'k dQnT kNqW wHcT tQ wRkTg')

if __name__ == '__main__':
    unittest.main()
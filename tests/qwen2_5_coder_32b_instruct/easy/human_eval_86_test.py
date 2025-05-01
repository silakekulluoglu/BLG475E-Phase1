'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.qwen2_5_coder_32b_instruct.easy.human_eval_86 import anti_shuffle

class TestAntiShuffle(unittest.TestCase):
    def test_anti_shuffle_1(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')

    def test_anti_shuffle_2(self):
        self.assertEqual(anti_shuffle('hello'), 'ehllo')

    def test_anti_shuffle_3(self):
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')

    def test_anti_shuffle_4(self):
        self.assertEqual(anti_shuffle(''), '')

    def test_anti_shuffle_5(self):
        self.assertEqual(anti_shuffle('Hi. My name is Mister Robot. How are you?'), '.Hi My aemn is Meirst .Rboot How aer ?ouy')

if __name__ == '__main__':
    unittest.main()
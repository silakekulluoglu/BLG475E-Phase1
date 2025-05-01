'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest
from source.qwen2_5_coder_32b_instruct.easy.human_eval_27 import flip_case

class TestFlipCase(unittest.TestCase):
    def test_flip_case_1(self):
        self.assertEqual(flip_case(''), '')

    def test_flip_case_2(self):
        self.assertEqual(flip_case('Hello!'), 'hELLO!')

    def test_flip_case_3(self):
        self.assertEqual(flip_case('These violent delights have violent ends'), 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS')

    def test_flip_case_4(self):
        self.assertEqual(flip_case('Python3.8'), 'pYTHON3.8')

    def test_flip_case_5(self):
        self.assertEqual(flip_case('123abcXYZ'), '123ABCxyz')

if __name__ == '__main__':
    unittest.main()
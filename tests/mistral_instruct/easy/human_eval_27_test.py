import unittest
import string
from source.mistral_instruct.easy.human_eval_27 import flip_case

class TestFlipCase(unittest.TestCase):
    def test_flip_case(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')
        self.assertEqual(flip_case('HeLLo'), 'hEllo')
        self.assertEqual(flip_case('123'), '123')
        self.assertEqual(flip_case('HELLO WORLD'), 'hELLO wORLD')

if __name__ == '__main__':
    unittest.main()
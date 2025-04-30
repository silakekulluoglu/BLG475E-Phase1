import unittest
from source.mistral_instruct.easy.human_eval_86 import anti_shuffle

class TestAntiShuffle(unittest.TestCase):
    def test_anti_shuffle(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')
        self.assertEqual(anti_shuffle('hello'), 'ehllo')
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')
        self.assertEqual(anti_shuffle('1Hello World!'), '1Hello !!!Wdlor')
        self.assertEqual(anti_shuffle('1Hello World!'), '1Hello !!!Wdlor')
        self.assertEqual(anti_shuffle('Hello1 World!'), 'Hello1 !!!Wdlor')
        self.assertEqual(anti_shuffle('1Hello World!1'), '1Hello !!!Wdlor1')

if __name__ == '__main__':
    unittest.main()
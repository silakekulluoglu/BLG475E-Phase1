import unittest
from source.qwen2_5_coder_32b_instruct.hard.human_eval_85 import add

class TestAdd(unittest.TestCase):
    def test_add_1(self):
        self.assertEqual(add([4, 88]), 88)

    def test_add_2(self):
        self.assertEqual(add([4, 5, 6, 7, 2, 122]), 122)

    def test_add_3(self):
        self.assertEqual(add([4, 0, 6, 7]), 0)

    def test_add_4(self):
        self.assertEqual(add([4, 4, 6, 8]), 12)

    def test_add_5(self):
        self.assertEqual(add([1, 2, 3, 4, 5, 6]), 6)

if __name__ == '__main__':
    unittest.main()
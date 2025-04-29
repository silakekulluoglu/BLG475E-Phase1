import unittest
from source.qwen2_5_coder_32b_instruct.moderate.human_eval_132 import is_nested

class TestIsNested(unittest.TestCase):
    def test_is_nested_1(self):
        self.assertEqual(is_nested('[[]]'), True)

    def test_is_nested_2(self):
        self.assertEqual(is_nested('[]]]]]]][[[[[]'), False)

    def test_is_nested_3(self):
        self.assertEqual(is_nested('[][]'), False)

    def test_is_nested_4(self):
        self.assertEqual(is_nested('[]'), False)

    def test_is_nested_5(self):
        self.assertEqual(is_nested('[[[[]]]]'), True)

if __name__ == '__main__':
    unittest.main()
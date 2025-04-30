import unittest
from source.mistral_instruct.easy.human_eval_30 import get_positive

class TestGetPositive(unittest.TestCase):
    def test_get_positive(self):
        self.assertEqual(get_positive([1, -2, 3, -4, 5, -6, 7]), [1, 3, 5, 7])
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])
        self.assertEqual(get_positive([0, -1, 0, 0, 0]), [])
        self.assertEqual(get_positive([-1, 0, 1]), [1])

if __name__ == '__main__':
    unittest.main()
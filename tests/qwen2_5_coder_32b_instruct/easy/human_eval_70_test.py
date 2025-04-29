import unittest
from source.qwen2_5_coder_32b_instruct.easy.human_eval_70 import strange_sort_list

class TestStrangeSortList(unittest.TestCase):
    def test_strange_sort_list_1(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

    def test_strange_sort_list_2(self):
        self.assertEqual(strange_sort_list([5, 6, 7, 8, 9]), [5, 9, 6, 8, 7])

    def test_strange_sort_list_3(self):
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_strange_sort_list_4(self):
        self.assertEqual(strange_sort_list([]), [])

    def test_strange_sort_list_5(self):
        self.assertEqual(strange_sort_list([0, 2, 2, 2, 5, 5, -5, -5]), [-5, 5, -5, 5, 0, 2, 2, 2])

if __name__ == '__main__':
    unittest.main()
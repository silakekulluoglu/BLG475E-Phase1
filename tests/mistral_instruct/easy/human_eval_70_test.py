import unittest
from source.mistral_instruct.easy.human_eval_70 import strange_sort_list

class TestStrangeSortList(unittest.TestCase):
    def test_strange_sort_list(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])
        self.assertEqual(strange_sort_list([]), [])
        self.assertEqual(strange_sort_list([1, 1, 2, 3, 4, 4, 3, 2, 1]), [1, 4, 1, 2, 3, 4, 1, 3, 2])
        self.assertEqual(strange_sort_list([1, '2', 3, '4', 4, '3', 2, '1']), [1, 4, 1, 2, 3, 4, 1, 3, 2])

if __name__ == '__main__':
    unittest.main()
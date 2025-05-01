'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest

class TestStrangeSortList(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])
        self.assertEqual(strange_sort_list([5, 6, 7, 8, 9]), [5, 9, 6, 8, 7])
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])
        self.assertEqual(strange_sort_list([]), [])
        self.assertEqual(strange_sort_list([111111]), [111111])

if __name__ == "__main__":
    unittest.main()

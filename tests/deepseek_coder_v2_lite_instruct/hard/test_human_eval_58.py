'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest

class TestCommon(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
    
    def test_case_2(self):
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])
    
    def test_case_3(self):
        self.assertEqual(common([4, 3, 2, 8], [3, 2, 4]), [2, 3, 4])
    
    def test_case_4(self):
        self.assertEqual(common([4, 3, 2, 8], []), [])

if __name__ == '__main__':
    unittest.main()
'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest

class TestGreatestCommonDivisor(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(greatest_common_divisor(3, 7), 1)
    
    def test_case_2(self):
        self.assertEqual(greatest_common_divisor(10, 15), 5)
    
    def test_case_3(self):
        self.assertEqual(greatest_common_divisor(49, 14), 7)
    
    def test_case_4(self):
        self.assertEqual(greatest_common_divisor(144, 60), 12)

if __name__ == '__main__':
    unittest.main()

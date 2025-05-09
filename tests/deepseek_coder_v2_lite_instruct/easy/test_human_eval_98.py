'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest

class TestCountUpper(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(count_upper('aBCdEf'), 1)
        self.assertEqual(count_upper('abcdefg'), 0)
    
    def test_edge_cases(self):
        self.assertEqual(count_upper('B'), 0)
        self.assertEqual(count_upper('U'), 1)
        self.assertEqual(count_upper(''), 0)

if __name__ == '__main__':
    unittest.main()
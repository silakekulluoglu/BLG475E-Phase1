'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest

class TestMaxFill(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1), 6)
        self.assertEqual(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2), 5)
        self.assertEqual(max_fill([[0,0,0], [0,0,0]], 5), 0)
    
    def test_edge_cases(self):
        self.assertEqual(max_fill([[1,1,1,1], [1,1,1,1]], 2), 4)
        self.assertEqual(max_fill([[1,1,1,1], [1,1,1,1]], 9), 2)

if __name__ == '__main__':
    unittest.main()

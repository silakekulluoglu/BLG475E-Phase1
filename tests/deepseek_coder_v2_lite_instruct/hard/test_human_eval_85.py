'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest

class TestAdd(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(add([4, 88]), 88)
        self.assertEqual(add([4, 5, 6, 7, 2, 122]), 122)
        self.assertEqual(add([4, 0, 6, 7]), 0)
        self.assertEqual(add([4, 4, 6, 8]), 12)

if __name__ == '__main__':
    unittest.main()
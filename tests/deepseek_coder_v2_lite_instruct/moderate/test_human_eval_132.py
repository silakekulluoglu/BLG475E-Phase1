'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest

class TestIsNested(unittest.TestCase):
    def test_simple_cases(self):
        self.assertTrue(is_nested('[[]]'))
        self.assertFalse(is_nested('[]]]]]]][[[[[]'))
        self.assertFalse(is_nested('[][]'))

    def test_edge_cases(self):
        self.assertFalse(is_nested(''))
        self.assertFalse(is_nested('[[[[[[[[') == False)

if __name__ == '__main__':
    unittest.main()

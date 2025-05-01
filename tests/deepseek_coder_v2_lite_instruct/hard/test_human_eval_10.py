'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest

class TestMakePalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(make_palindrome(''), '')
    
    def test_single_character(self):
        self.assertEqual(make_palindrome('x'), 'x')
    
    def test_short_string(self):
        self.assertEqual(make_palindrome('xyz'), 'xyzyx')
    
    def test_already_palindrome(self):
        self.assertEqual(make_palindrome('xyx'), 'xyx')

    def test_longer_string(self):
        self.assertEqual(make_palindrome('jerry'), 'jerryrrej')


if __name__ == '__main__':
    unittest.main()

'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import unittest

class TestFlipCase(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(flip_case(''), '')
    
    def test_no_change(self):
        self.assertEqual(flip_case('Hello!'), 'hELLO!')
    
    def test_full_case_flip(self):
        self.assertEqual(flip_case('These violent delights have violent ends'), 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS')
    
    def test_mixed_case(self):
        self.assertEqual(flip_case('SwApPeDcAsE'), 'sWaPpEdCaSe')
    
    def test_numbers_and_symbols(self):
        self.assertEqual(flip_case('12345!@#$%'), '12345!@#$%')

if __name__ == "__main__":
    unittest.main()

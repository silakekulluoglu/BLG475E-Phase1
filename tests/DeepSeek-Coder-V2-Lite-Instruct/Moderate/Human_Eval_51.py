import unittest

class TestRemoveVowels(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')
    
    def test_string_with_newlines(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), 'bcdf\nghjklm')
    
    def test_string_without_vowels(self):
        self.assertEqual(remove_vowels('abcdef'), 'bcdf')
    
    def test_string_with_only_vowels(self):
        self.assertEqual(remove_vowels('aaaaa'), '')
    
    def test_string_with_mixed_case_vowels(self):
        self.assertEqual(remove_vowels('aaBAA'), 'B')
    
if __name__ == '__main__':
    unittest.main()

import unittest

class TestRemoveVowels(unittest.TestCase):
    def test_remove_vowels_1(self):
        self.assertEqual(remove_vowels(''), '')

    def test_remove_vowels_2(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), 'bcdf\ng hjklm')

    def test_remove_vowels_3(self):
        self.assertEqual(remove_vowels('fedcba'), 'fdcb')

    def test_remove_vowels_4(self):
        self.assertEqual(remove_vowels('eeeee'), '')

    def test_remove_vowels_5(self):
        self.assertEqual(remove_vowels('acBAA'), 'cB')

if __name__ == '__main__':
    unittest.main()
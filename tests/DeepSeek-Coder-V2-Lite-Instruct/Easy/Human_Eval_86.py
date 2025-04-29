import unittest

class TestAntiShuffle(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')
        self.assertEqual(anti_shuffle('hello'), 'ehllo')
        self.assertEqual(anti_shuffle('number'), 'bemnru')
        self.assertEqual(anti_shuffle('abcd'), 'abcd')
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')

if __name__ == '__main__':
    unittest.main()

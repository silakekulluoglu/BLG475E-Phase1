import unittest
from source.mistral_instruct.easy.human_eval_98 import count_upper

import unittest

class TestCountUpper(unittest.TestCase):
    def test_count_upper(self):
        self.assertEqual(count_upper('aBCdEf'), 1)
        self.assertEqual(count_upper('abcdefg'), 0)
        self.assertEqual(count_upper('dBBE'), 0)
        self.assertEqual(count_upper('dBBe'), 0)
        self.assertEqual(count_upper('1aBCdEf'), 1)
        self.assertEqual(count_upper('abcdefg1'), 0)
        self.assertEqual(count_upper('dBBe1'), 0)

if __name__ == '__main__':
    unittest.main()
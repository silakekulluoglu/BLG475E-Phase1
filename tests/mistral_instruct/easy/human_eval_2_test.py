import unittest
from source.mistral_instruct.easy.human_eval_2 import truncate_number

import unittest

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number(self):
        self.assertEqual(truncate_number(3.5), 0.5)
        self.assertEqual(truncate_number(7.123), 0.123)
        self.assertEqual(truncate_number(0.0), 0.0)
        self.assertEqual(truncate_number(-3.5), -0.5)

if __name__ == '__main__':
    unittest.main()
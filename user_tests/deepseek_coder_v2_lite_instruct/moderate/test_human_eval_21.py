'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys, os

sys.path.insert(0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '../../../../source/deepseek_coder_v2_lite_instruct/moderate'
        )
    )
)


from human_eval_21 import rescale_to_unit

import unittest

class TestRescaleToUnit(unittest.TestCase):
    def test_reversed(self):
        self.assertEqual(rescale_to_unit([5.0, 3.0, 1.0]), [1.0, 0.5, 0.0])

    def test_negative_values(self):
        self.assertEqual(rescale_to_unit([-1.0, 0.0, 1.0]), [0.0, 0.5, 1.0])

    def test_single_decimal(self):
        self.assertEqual(rescale_to_unit([0.1, 0.9]), [0.0, 1.0])
        
if __name__ == '__main__':
    unittest.main()

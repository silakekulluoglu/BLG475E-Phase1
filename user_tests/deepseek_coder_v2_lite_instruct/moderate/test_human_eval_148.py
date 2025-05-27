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


from human_eval_148 import bf

import unittest

class TestBf(unittest.TestCase):
    def test_swapped_order(self):
        self.assertEqual(bf("Neptune", "Mercury"), ("Venus","Earth","Mars","Jupiter","Saturn","Uranus"))

    def test_invalid_planet(self):
        self.assertEqual(bf("Pluto", "Earth"), ())

    def test_same_planet(self):
        self.assertEqual(bf("Mars", "Mars"), ())

    def test_adjacent_planets(self):
        self.assertEqual(bf("Venus", "Earth"), ())

if __name__ == '__main__':
    unittest.main()

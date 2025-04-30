import unittest
from source.mistral_instruct.easy.human_eval_45 import triangle_area

class TestTriangleArea(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(triangle_area(5, 3), 7.5)
        self.assertEqual(triangle_area(3, 4), 6.0)
        with self.assertRaises(ValueError):
            triangle_area(0, 3)
        with self.assertRaises(ValueError):
            triangle_area(-5, 3)
        with self.assertRaises(ValueError):
            triangle_area(3, 0)
        with self.assertRaises(TypeError):
            triangle_area('a', 3)
        with self.assertRaises(TypeError):
            triangle_area(3, 'b')

if __name__ == '__main__':
    unittest.main()
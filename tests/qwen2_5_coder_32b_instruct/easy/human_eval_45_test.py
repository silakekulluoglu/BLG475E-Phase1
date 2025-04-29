import unittest
from source.qwen2_5_coder_32b_instruct.easy.human_eval_45 import triangle_area

class TestTriangleArea(unittest.TestCase):
    def test_triangle_area_1(self):
        self.assertEqual(triangle_area(5, 3), 7.5)

    def test_triangle_area_2(self):
        self.assertEqual(triangle_area(2, 2), 2.0)

    def test_triangle_area_3(self):
        self.assertEqual(triangle_area(10, 8), 40.0)

    def test_triangle_area_4(self):
        self.assertEqual(triangle_area(0, 5), 0.0)

    def test_triangle_area_5(self):
        self.assertEqual(triangle_area(7, 0), 0.0)

if __name__ == '__main__':
    unittest.main()
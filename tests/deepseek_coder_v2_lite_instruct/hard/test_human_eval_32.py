import unittest
import random

class TestFindZero(unittest.TestCase):
    def test_simple_polynomial(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=2)
    
    def test_cubic_polynomial(self):
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=2)
    
    def test_random_polynomials(self):
        rng = random.Random(42)
        for _ in range(5):
            ncoeff = 2 * rng.randint(1, 4)
            coeffs = []
            for _ in range(ncoeff):
                coeff = rng.randint(-10, 10)
                if coeff == 0:
                    coeff = 1
                coeffs.append(coeff)
            solution = find_zero(coeffs)
            self.assertAlmostEqual(poly(coeffs, solution), 0, places=4)

if __name__ == '__main__':
    unittest.main()

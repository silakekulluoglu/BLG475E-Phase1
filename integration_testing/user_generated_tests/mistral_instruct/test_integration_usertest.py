import unittest
from typing import List
from integration_testing.integration_classes.mistral_instruct.integration_class import DataAnalysis  # replace 'your_module' with the actual module name if saved in a file

class TestDataAnalysisIntegration(unittest.TestCase):

    def setUp(self):
        self.analysis = DataAnalysis()

    def test_gcd_and_rescale_integration(self):
        # Use gcd results in a list and rescale them
        a, b = 48, 18
        gcd_result = self.analysis.greatest_common_divisor(a, b)  # Expected: 6
        numbers = [gcd_result, gcd_result * 2, gcd_result * 3]  # [6, 12, 18]
        rescaled = self.analysis.rescale_to_unit(numbers)  # Expected: [0.0, 0.5, 1.0]
        self.assertEqual(rescaled, [0.0, 0.5, 1.0])

    def test_rescale_and_pluck_integration(self):
        # Rescale first, then pluck from rescaled (rescaled are floats, so pluck should return empty)
        numbers = [10, 20, 30]
        rescaled = self.analysis.rescale_to_unit(numbers)
        result = self.analysis.pluck(rescaled)
        self.assertEqual(result, [])  # No even integers in rescaled output

    def test_pluck_with_gcd_inputs(self):
        # Generate a list of gcd values from pairs and pluck from it
        pairs = [(100, 10), (18, 6), (7, 3)]
        gcds = [self.analysis.greatest_common_divisor(a, b) for a, b in pairs]  # [10, 6, 1]
        result = self.analysis.pluck(gcds)  # Even numbers: [10, 6], min: 6, index: 1
        self.assertEqual(result, [6, 1])

    def test_combined_sequence(self):
        # Complex chain: GCD → list of values → rescale → pluck
        a, b = 30, 12
        gcd = self.analysis.greatest_common_divisor(a, b)  # 6
        values = [gcd * i for i in range(1, 4)]  # [6, 12, 18]
        rescaled = self.analysis.rescale_to_unit(values)  # [0.0, 0.5, 1.0]
        result = self.analysis.pluck([int(x * 10) for x in rescaled])  # [0, 5, 10], even: [0, 10], min: 0
        self.assertEqual(result, [0, 0])

if __name__ == '__main__':
    unittest.main()
import unittest
from typing import List
from integration_testing.integration_classes.mistral_instruct.integration_class import DataAnalysis

def check_data_analysis(candidate):
    data = DataAnalysis()

    # Test GCD function
    assert candidate.greatest_common_divisor(3, 7) == data.greatest_common_divisor(3, 7), "Error"
    assert candidate.greatest_common_divisor(10, 15) == data.greatest_common_divisor(10, 15), "Error"
    assert candidate.greatest_common_divisor(49, 14) == data.greatest_common_divisor(49, 14), "Error"
    assert candidate.greatest_common_divisor(144, 60) == data.greatest_common_divisor(144, 60), "Error"

    # Test rescale_to_unit function
    assert candidate.rescale_to_unit([2.0, 49.9]) == data.rescale_to_unit([2.0, 49.9]), "Error"
    assert candidate.rescale_to_unit([100.0, 49.9]) == data.rescale_to_unit([100.0, 49.9]), "Error"
    assert candidate.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == data.rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), "Error"
    assert candidate.rescale_to_unit([2.0, 1.0, 5.0, 3.0, 4.0]) == data.rescale_to_unit([2.0, 1.0, 5.0, 3.0, 4.0]), "Error"
    assert candidate.rescale_to_unit([12.0, 11.0, 15.0, 13.0, 14.0]) == data.rescale_to_unit([12.0, 11.0, 15.0, 13.0, 14.0]), "Error"

    # Test pluck function
    assert candidate.pluck([4,2,3]) == data.pluck([4,2,3]), "Error"
    assert candidate.pluck([1,2,3]) == data.pluck([1,2,3]), "Error"
    assert candidate.pluck([]) == data.pluck([]), "Error"
    assert candidate.pluck([5, 0, 3, 0, 4, 2]) == data.pluck([5, 0, 3, 0, 4, 2]), "Error"
    assert candidate.pluck([1, 2, 3, 0, 5, 3]) == data.pluck([1, 2, 3, 0, 5, 3]), "Error"
    assert candidate.pluck([5, 4, 8, 4 ,8]) == data.pluck([5, 4, 8, 4 ,8]), "Error"
    assert candidate.pluck([7, 6, 7, 1]) == data.pluck([7, 6, 7, 1]), "Error"
    assert candidate.pluck([7, 9, 7, 1]) == data.pluck([7, 9, 7, 1]), "Error"

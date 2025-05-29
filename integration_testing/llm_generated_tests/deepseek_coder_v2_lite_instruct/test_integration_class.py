'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import sys, os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../../integration_testing/integration_classes/deepseek_coder_v2_lite_instruct')
    )
)

from integration_class import TreeProcessor

import unittest

def test_tree_processor_integration():
    processor = TreeProcessor()

    # Test 1: Normal branch with nested functionality
    branch = [6, 2, 8, 4, 10]
    result = processor.process_tree_branch(branch)
    assert result["plucked_node"] == [2, 1], "Pluck method failed in integration test"
    assert result["gcd"] == 2, "GCD method failed in integration test"
    assert result["rescaled_branch"] == [0.5, 0.0, 0.75, 0.25, 1.0], "Rescale method failed in integration test"

    # Test 2: Branch with all odd numbers
    odd_branch = [1, 3, 5, 7]
    result = processor.process_tree_branch(odd_branch)
    assert result["plucked_node"] == [], "Pluck method failed with all odd numbers"
    assert result["gcd"] is None, "GCD method failed with all odd numbers"
    assert result["rescaled_branch"] == [0.0, 0.3333333333333333, 0.6666666666666666, 1.0], "Rescale method failed with all odd numbers"

    # Test 3: Branch with a single even number
    single_even_branch = [1, 3, 2, 5]
    result = processor.process_tree_branch(single_even_branch)
    assert result["plucked_node"] == [2, 2], "Pluck method failed with a single even number"
    assert result["gcd"] == 2, "GCD method failed with a single even number"
    assert result["rescaled_branch"] == [0.0, 0.5, 1.0, 1.0], "Rescale method failed with a single even number"

    # Test 4: Branch with all identical even numbers
    identical_even_branch = [4, 4, 4, 4]
    result = processor.process_tree_branch(identical_even_branch)
    assert result["plucked_node"] == [4, 0], "Pluck method failed with identical even numbers"
    assert result["gcd"] == 4, "GCD method failed with identical even numbers"
    assert result["rescaled_branch"] == [0.0, 0.0, 0.0, 0.0], "Rescale method failed with identical even numbers"

    # Test 5: Branch with multiple smallest even values
    multiple_even_branch = [5, 2, 3, 2, 4, 2]
    result = processor.process_tree_branch(multiple_even_branch)
    assert result["plucked_node"] == [2, 1], "Pluck method failed with multiple smallest even values"
    assert result["gcd"] == 2, "GCD method failed with multiple smallest even values"
    assert result["rescaled_branch"] == [0.75, 0.0, 0.25, 0.0, 0.5, 0.0], "Rescale method failed with multiple smallest even values"

    # Test 6: Branch with negative numbers (invalid case, but testing robustness)
    negative_branch = [-5, 0, -3, 0, -4, 2]
    result = processor.process_tree_branch(negative_branch)
    assert result["plucked_node"] == [0, 1], "Pluck method failed with negative numbers"
    assert result["gcd"] == 0, "GCD method failed with negative numbers"
    assert result["rescaled_branch"] == [0.0, 1.0, 0.3333333333333333, 1.0, 0.16666666666666666, 1.0], "Rescale method failed with negative numbers"

    # Test 7: Branch with only one element
    single_element_branch = [10]
    result = processor.process_tree_branch(single_element_branch)
    assert result["plucked_node"] == [10, 0], "Pluck method failed with a single element"
    assert result["gcd"] == 10, "GCD method failed with a single element"
    assert result["rescaled_branch"] == [0.0], "Rescale method failed with a single element"

    print("All integration tests passed!")

# Run the integration tests
test_tree_processor_integration()


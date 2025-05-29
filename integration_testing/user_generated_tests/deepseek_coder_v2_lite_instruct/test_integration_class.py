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


import unittest

from integration_class import TreeProcessor

def test_tree_processor_integration():
    processor = TreeProcessor()

    branch = [7, 14]
    result = processor.process_tree_branch(branch)
    assert result["plucked_node"] == [14, 1], "Failed to pluck the only even in a two‐element list"
    assert result["gcd"] == 1, "GCD of (14, 1) should be 1"
    assert result["rescaled_branch"] == [0.0, 1.0], "Rescaling [7,14] should map to [0.0, 1.0]"

    branch = [9, 7, 5, 4]
    result = processor.process_tree_branch(branch)
    assert result["plucked_node"] == [4, 3], "Should pluck the even 4 at index 3"
    assert result["gcd"] == 1, "GCD of (4, 3) should be 1"
    assert result["rescaled_branch"] == [
        1.0,
        0.6,
        0.2,
        0.0
    ], "Incorrect rescaling of [9,7,5,4]"

    branch = [-6, -2, -8]
    result = processor.process_tree_branch(branch)
    assert result["plucked_node"] == [-8, 2], "Should pluck the smallest even (-8) at index 2"
    assert result["gcd"] == 2, "GCD of (-8, 2) should be 2"
    assert result["rescaled_branch"] == [
        0.3333333333333333,
        1.0,
        0.0
    ], "Incorrect rescaling of [-6, -2, -8]"

    branch = [0, 1_000_000]
    result = processor.process_tree_branch(branch)
    assert result["plucked_node"] == [0, 0], "Should pluck 0 at index 0"
    assert result["gcd"] == 0, "GCD of (0, 0) should be 0"
    assert result["rescaled_branch"] == [0.0, 1.0], "Rescaling [0,1e6] should map to [0.0,1.0]"

    branch = [3]
    result = processor.process_tree_branch(branch)
    assert result["plucked_node"] == [], "Pluck should be empty for single odd value"
    assert result["gcd"] is None, "GCD should be None when no node was plucked"
    assert result["rescaled_branch"] == [], "Rescale should be empty when no node was plucked"

    try:
        processor.process_tree_branch([8])
        assert False, "Expected ZeroDivisionError for single‐element even branch"
    except ZeroDivisionError:
        pass

    print("All additional integration tests passed!")

if __name__ == "__main__":
    test_tree_processor_integration()

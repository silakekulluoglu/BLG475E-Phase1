def check(candidate):
    assert candidate([4,2,3]) == [2, 1]
    assert candidate([1,2,3]) == [2, 1]
    assert candidate([]) == []
    assert candidate([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert candidate([1, 2, 3, 0, 5, 3]) == [0, 3]
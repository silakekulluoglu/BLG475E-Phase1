def check(candidate):
    assert candidate([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6
    assert candidate([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5
    assert candidate([[0,0,0], [0,0,0]], 5) == 0
    assert candidate([[1,1,1,1], [1,1,1,1]], 2) == 4
    assert candidate([[1,1,1,1], [1,1,1,1]], 9) == 2

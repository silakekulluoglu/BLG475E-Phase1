def check(candidate):
    assert candidate(50) == 0
    assert candidate(78) == 2
    assert candidate(200) == 6
    assert candidate(4000) == 192
    assert candidate(100000) == 8026

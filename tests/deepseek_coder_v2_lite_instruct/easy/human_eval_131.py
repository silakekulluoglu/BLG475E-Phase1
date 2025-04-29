def check(candidate):
    assert candidate(5) == 5
    assert candidate(54) == 5
    assert candidate(120) == 1
    assert candidate(5014) == 5
    assert candidate(98765) == 315
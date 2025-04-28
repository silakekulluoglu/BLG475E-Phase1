def check(candidate):
    assert candidate(1, 5) == "0b11"
    assert candidate(7, 13) == "0b1010"
    assert candidate(964, 977) == "0b1111001010"
    assert candidate(996, 997) == "0b1111100100"
    assert candidate(560, 851) == "0b1011000010"
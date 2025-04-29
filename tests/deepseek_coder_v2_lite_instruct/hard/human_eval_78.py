def check(candidate):
    assert candidate("AB") == 1
    assert candidate("1077E") == 2
    assert candidate("ABED1A33") == 4
    assert candidate("123456789ABCDEF0") == 6
    assert candidate("112233445566778899AABBCCDDEEFF00") == 12

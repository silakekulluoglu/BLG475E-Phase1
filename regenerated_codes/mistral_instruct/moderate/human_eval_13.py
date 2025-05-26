'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def greatest_common_divisor(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    if a == 0 and b == 0:
        raise ValueError("GCD is undefined for both arguments being zero")
    if a == 0:
        return b
    if b == 0:
        return a
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
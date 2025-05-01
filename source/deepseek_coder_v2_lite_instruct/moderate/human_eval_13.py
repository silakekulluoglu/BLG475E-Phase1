'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

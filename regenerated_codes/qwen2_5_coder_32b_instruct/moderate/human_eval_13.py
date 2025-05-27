'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def greatest_common_divisor(a, b):
    if a == 0 and b == 0:
        raise ValueError("Both inputs cannot be zero.")
    
    # Ensure a and b are non-negative
    a, b = abs(a), abs(b)
    
    # Euclidean algorithm to find GCD
    while b != 0:
        a, b = b, a % b
    
    return a
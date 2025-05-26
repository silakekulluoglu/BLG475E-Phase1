'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def digits(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer.")

    product = 1
    only_even = True
    while n > 0:
        digit = n % 10
        if (digit & 1) == 1:
            only_even = False
            product *= digit
        n //= 10

    return not only_even and product or 0

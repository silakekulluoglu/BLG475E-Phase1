'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import math

def poly(xs: list, x: float):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    if len(xs) % 2 != 0:
        raise ValueError("The list should have an even number of coefficients.")

    def f(x):
        return poly([coeff * (-1) ** i for coeff, i in enumerate(xs)], x)

    max_pow = len(xs) // 2
    min_val = float('inf')
    root = None

    # Find the interval where root lies.
    for i in range(max_pow):
        val1 = f(math.pow(2, i))
        if val1 < 0:
            break
        min_val = min(min_val, val1)

    for i in range(max_pow - 1, 0, -1):
        val2 = f(math.pow(2, i))
        if val2 > 0:
            break
        min_val = min(min_val, val2)

    if min_val == 0:
        raise ValueError("The polynomial does not have a root in the given interval.")

    # Binary search on the obtained interval.
    start = math.pow(2, max_pow - 1)
    end = math.pow(2, max_pow)
    while abs(start - end) > 1e-6:
        mid = (start + end) / 2
        if f(mid) * f(end) < 0:
            start = mid
        else:
            end = mid

    root = (start + end) / 2
    return round(root, 2)
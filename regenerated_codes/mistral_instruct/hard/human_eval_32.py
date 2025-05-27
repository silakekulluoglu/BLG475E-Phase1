'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import math

def poly(xs: list, x: float):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    if len(xs) <= 0:
        raise ValueError("All coefficients must not be zero.")
    elif len(xs) % 2 == 1:
        raise ValueError("The given coefficients list must have an even number of elements.")
    elif xs[-1] == 0:
        raise ValueError("The largest non-zero coefficient can not be zero.")

    n = len(xs) // 2 - 1
    a = xs[n]
    b = sum([xs[i] for i in range(n)])

    if b != 0:
        discr = (b**2) - (4 * a * poly([-b, 0], n))
    else:
        discr = None

    if discr is not None and discr >= 0:
        sqrt_discr = math.sqrt(discr)
        x1 = (-b + sqrt_discr) / (2 * a)
        x2 = (-b - sqrt_discr) / (2 * a)
    else:
        x1, x2 = None, None

    if x1 is not None:
        def f(x):
            return poly([1,], x - x1)

        def df(x):
            return 1 - f(x)

        def ddf(x):
            return -f(x)

        x_new = x1 - poly([0, 1 / df(x1)], n)
        while abs(poly([x_new, 1 / ddf(x_new)], n)) > 0.00001:
            x_old = x_new
            x_new -= poly([0, 1 / df(x_old)], n)
    elif x2 is not None:
        def f(x):
            return poly([1,], x - x2)

        def df(x):
            return 1 - f(x)

        def ddf(x):
            return -f(x)

        x_new = x2 - poly([0, 1 / df(x2)], n)
        while abs(poly([x_new, 1 / ddf(x_new)], n)) > 0.00001:
            x_old = x_new
            x_new -= poly([0, 1 / df(x_old)], n)
    else:
        raise ValueError("No real root found.")

    return round(x_new, 2)
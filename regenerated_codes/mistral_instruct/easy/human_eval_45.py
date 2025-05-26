'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def triangle_area(a: float, h: float) -> float:
    if a < 0:
        raise ValueError("Either side or height must be non-negative.")
    elif h < 0:
        raise ValueError("Either side or height must be non-negative.")

    return (a * h) / 2
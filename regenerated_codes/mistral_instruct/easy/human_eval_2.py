'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''
import math

def truncate_number(number: float) -> float:
    if number <= 0:
        raise ValueError("Input must be positive.")

    integer_part = math.floor(number)
    decimal_part = number - integer_part

    return decimal_part
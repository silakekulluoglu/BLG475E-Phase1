'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

from math import sqrt

def is_multiply_prime(a):
    if a < 2 or (a % 2 == 0 and a != 2):
        return False

    prime_multipliers = [2, 3]
    multiple = 2

    while len(prime_multipliers) < 3:
        multiple += 1
        if a % multiple != 0:
            continue

        is_prime = True
        for potential_divisor in range(2, int(multiple**0.5)+1):
            if multiple % potential_divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_multipliers.append(multiple)

    return all([x <= a for x in prime_multipliers]) and len(prime_multipliers) == 3
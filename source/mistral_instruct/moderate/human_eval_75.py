'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def is_multiply_prime(a):
    if a <= 1 or a > 96:
        return False

    primes = [2, 3, 5]
    factors = set()
    for p in primes:
        while a % p == 0:
            factors.add(p)
            a //= p
    if len(factors) != 3 or a > 1:
        return False

    return all([f in primes for f in factors])
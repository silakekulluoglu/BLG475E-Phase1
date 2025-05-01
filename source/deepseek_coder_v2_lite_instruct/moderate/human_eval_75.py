'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def is_multiply_prime(a):
    def is_prime(n):
        if n <= 1:
            return False
        for j in range(2, int(n**0.5) + 1):
            if n % j == 0:
                return False
        return True

    for i in range(2, 101):
        if not is_prime(i):
            continue
        for j in range(i, 101):
            if not is_prime(j):
                continue
            for k in range(j, 101):
                if not is_prime(k):
                    continue
                if i * j * k == a:
                    return True
    return False

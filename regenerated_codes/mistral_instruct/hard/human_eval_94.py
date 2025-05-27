'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def skjkasdkd(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    max_prime = 0
    max_prime_sum = 0

    if not lst:
        return 0

    for num in lst:
        if is_prime(num) and num > max_prime:
            max_prime = num

    digit_sum = sum(map(int, list(str(max_prime))))
    return digit_sum or 0
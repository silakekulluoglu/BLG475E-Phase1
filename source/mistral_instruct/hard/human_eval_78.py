'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def hex_key(num):
    prime_digits = [2, 3, 5, 7]  # Prime hexadecimal digits
    if not num:
        return 0

    hex_map = {
        "A": 11,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }
    prime_count = 0
    for digit in num:
        if digit.isdigit():
            if int(digit) in prime_digits:
                prime_count += 1
        elif digit in hex_map:
            prime_count += prime_digits.count(hex_map[digit])
    return prime_count
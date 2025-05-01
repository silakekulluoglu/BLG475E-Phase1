'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def count_upper(s):
    count = 0
    uppercase_vowels = "AEIOU"
    for i in range(0, len(s), 2):
        if s[i] in uppercase_vowels:
            count += 1
    return count

'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def count_upper(s):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    index = 0
    count = 0
    for char in s:
        if (index % 2 == 0) and (char.isupper() and char in VOWELS):
            count += 1
        index += 1
    return count
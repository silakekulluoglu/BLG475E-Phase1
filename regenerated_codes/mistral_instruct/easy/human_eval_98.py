'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

UPPERCASE_VOWELS = 'AEIOU'

def count_upper(s):
    if not s:  # If the input is empty, return 0
        return 0

    count = 0
    for i, char in enumerate(s):  # Iterate through the characters and their indices
        if char in UPPERCASE_VOWELS and i % 2 == 0:  # Check if the current character is an uppercase vowel and its index is even
            count += 1
    return count
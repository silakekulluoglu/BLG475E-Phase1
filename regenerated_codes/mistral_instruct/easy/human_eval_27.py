'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import string

def flip_case(string: str) -> str:
    result = ""
    for char in string:
        if char in string.ascii_lowercase:
            result += char.upper()
        elif char in string.ascii_uppercase:
            result += char.lower()
        else:
            result += char
    return result
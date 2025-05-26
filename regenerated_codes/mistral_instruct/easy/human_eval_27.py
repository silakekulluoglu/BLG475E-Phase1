'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def flip_case(string: str) -> str:
    translated = [c.upper() if c.islower() else c.lower() for c in string]
    return ''.join(translated)

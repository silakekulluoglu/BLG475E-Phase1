'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def remove_vowels(text):
    vowels = set("aeiouAEIOU")
    return ''.join(c for c in text if c.lower() not in vowels)
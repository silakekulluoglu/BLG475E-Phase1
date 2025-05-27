'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

VOWEL_MAP = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'}
VCONSONANT_MAP = {c: c for c in 'bcdfghjklmnpqrstvwxyz' if c not in VOWEL_MAP}

def encode(message):
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char in VOWEL_MAP:
                vowel_pos = list(VOWEL_MAP).index(char) + 2
                encoded_char = VOWEL_MAP[VOWEL_MAP[(list(VOWEL_MAP)[vowel_pos % len(VOWEL_MAP)] 
if vowel_pos > len(VOWEL_MAP) else VOWEL_MAP[0])]]
                encoded_char = encoded_char.lower() if char.isupper() else encoded_char.upper()
            else:
                encoded_char = char.swapcase()
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message
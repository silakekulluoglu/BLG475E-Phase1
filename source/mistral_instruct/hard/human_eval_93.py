'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def encode(message):
    vowels = "aeiou"  # Vowels to be replaced
    result = ""
    for char in message.lower():  # Ensure all letters are lowercase
        if char.isalpha():
            if char in vowels:
                idx = vowels.index(char) + 2
                result += chr((ord(vowels[idx % len(vowels)]) - ord("a")) + ord("A"))
            else:
                result += char.swapcase()
        else:
            result += char
    return result
'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def split_words(txt):
    if " " in txt:
        words = []
        current_word = ""
        for char in txt:
            if char == " ":
                if current_word:
                    words.append(current_word)
                    current_word = ""
            else:
                current_word += char
        if current_word:
            words.append(current_word)
        return words
    elif "," in txt:
        return txt.split(",")
    else:
        count = 0
        for char in txt:
            if char in LOWERCASE_LETTERS and (ord(char) + 1) % 2 == 1:
                count += 1
        return count
'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def split_words(txt):
    words = []
    for char in txt:
        if char.isspace():
            if words:
                break
        elif char == ',':
            words.append(txt[words[-1]:txt.index(char)].strip())
            continue
        else:
            if ord('a') <= ord(char.lower()) <= ord('z'):
                if ord(char.lower()) % 2 != 0:
                    words.append(char)
    if not words:
        return len([i for i in txt.lower() if i.isalpha() and (ord(i) < ord('a') or 
ord(i) > ord('z'))])
    else:
        return words
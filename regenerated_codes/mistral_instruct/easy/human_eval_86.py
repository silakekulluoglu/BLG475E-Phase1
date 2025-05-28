'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import operator
def anti_shuffle(s):
    words = s.split()
    result = []
    for word in words:
        sorted_word = ''.join(sorted(list(word)))
        result.append(sorted_word)
    return ' '.join(result)

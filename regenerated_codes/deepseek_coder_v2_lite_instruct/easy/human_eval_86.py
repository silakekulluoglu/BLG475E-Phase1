'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def anti_shuffle(s):
    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])

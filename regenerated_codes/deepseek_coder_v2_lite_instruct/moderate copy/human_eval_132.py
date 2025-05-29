'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def is_nested(string):
    depth = 0
    for ch in string:
        if ch == '[':
            depth += 1
        else: 
            if depth >= 2:
                return True
            depth = max(depth - 1, 0)
    return False

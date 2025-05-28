'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def is_nested(brackets):
    for i in range(len(brackets) - 2):
        if brackets[i] == '[' and brackets[i + 1] == '[' and brackets[i + 2] == ']':
            # Check if there is a closing bracket after the second opening bracket
            for j in range(i + 3, len(brackets)):
                if brackets[j] == ']':
                    return True
    return False
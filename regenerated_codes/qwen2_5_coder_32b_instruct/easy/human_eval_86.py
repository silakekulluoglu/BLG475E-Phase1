'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

import re

def anti_shuffle(s):
    # Regular expression to match sequences of alphabetic characters (words)
    word_pattern = re.compile(r'[^\s\U0001F600-\U0001F64F]+')
    
    def sort_word(match):
        # Sort the characters in the matched word by their ASCII values
        return ''.join(sorted(match.group(0)))
    
    # Use re.sub to replace each word with its sorted version
    sorted_string = word_pattern.sub(sort_word, s)
    return sorted_string
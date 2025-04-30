def count_upper(s):
    vowels = 'AEIOUY'
    count = 0
    for i, char in enumerate(s.upper()):
        if char.isalpha() and char in vowels and i % 2 == 0:
            count += 1
    return count
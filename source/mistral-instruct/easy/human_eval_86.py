def anti_shuffle(s):
    words = s.split()
    result = []
    for word in words:
        sorted_word = ''.join(sorted(list(word)))
        result.append(sorted_word)
    return ' '.join(result)
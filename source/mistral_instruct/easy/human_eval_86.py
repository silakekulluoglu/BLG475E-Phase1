def anti_shuffle(s):
    words = s.split()
    result = []
    for word in words:
        chars = list(word)
        chars = [char for char in chars if char.isalpha()]
        chars.sort(key=ord)
        result.append(''.join(chars))
        result.append(' ')
    return ''.join(result)[:-1]

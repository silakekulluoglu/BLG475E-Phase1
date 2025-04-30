def split_words(txt):
    if txt.count(' ') == 0:
        if txt.count(',') == 0:
            result = 0
            for char in txt.lower():
                if char.isalpha() and ord(char) % 2 == 1:
                    result += 1
            return result
        else:
            words = txt.split(',')
            result = 0
            for word in words:
                for char in word.lower():
                    if char.isalpha() and ord(char) % 2 == 1:
                        result += 1
            return result
    else:
        return txt.split()
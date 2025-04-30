import string

def flip_case(string: str) -> str:
    result = ""
    for char in string:
        if char in string.ascii_lowercase:
            result += char.upper()
        elif char in string.ascii_uppercase:
            result += char.lower()
        else:
            result += char
    return result
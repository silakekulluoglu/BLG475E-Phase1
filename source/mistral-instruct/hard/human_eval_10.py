def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:

    if not string:
        return ''

    length = len(string)
    for i in range(length):
        if is_palindrome(string[i:]):
            palindrome_suffix = string[i:]
            prefix = string[:i]
            reversed_prefix = prefix[::-1]
            return f"{palindrome_suffix}{reversed_prefix}"
    else:
        return f"{string}{string[::-1]}"
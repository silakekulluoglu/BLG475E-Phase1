'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string."""
    if not isinstance(string, str):
        raise TypeError("Input must be a string.")

    def is_longest_palindrome(substring):
        return is_palindrome(substring) and (len(substring) > 
len(longest))

    longest = ""
    palindromes = []
    for i in range(1, len(string)):
        substring = string[:i] + string[i:][::-1]
        if is_longest_palindrome(substring):
            longest = substring
            palindromes.append(substring)

    if not longest:
        # If the given input string is not a palindrome, find the shortest possible palindrome that can be made from it.
        for i in range(len(string)):
            for j in range(i + 1, len(string)):
                substring = string[i:j]
                if is_longest_palindrome(substring):
                    longest = substring
                    break

        # Find the letter(s) that will be in the middle and then add the last/symmetric part of the palindrome to the word.
        first_half = longest[:len(longest) // 2]
        second_half = longest[len(longest) // 2:]
        # Check if do you need to complete that pattern
        for i in range(1, len(first_half)):
            if first_half[i - 1] == first_half[i]:
                return (first_half + string + second_half)[::-1]

        # If no pattern is found, choose the last letter and add the letters before to make it palindrome.
        return (string[-2:][::-1] + string[:-2])[::-1]

def even_odd_palindrome(n):
    evens = sum([1 for x in range(1, n) if str(x) == str(x)[::-1] and x % 2 == 0])
    odds = sum([1 for x in range(1, n) if str(x) == str(x)[::-1] and x % 2 != 0])

    return (evens, odds)
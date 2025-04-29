def solution(lst):
    result = 0
    for i, num in enumerate(lst):
        if num % 2 != 0 and i % 2 == 0:
            result += num
    return result
def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if not stack or stack[-1] != '[':
                return False
            else:
                stack.pop()
    return len(stack) == 0
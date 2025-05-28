'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def is_nested(string):
    stack = []

    for char in string:
        # If we find an opening bracket, push it onto the stack.
        if char == '[':
            stack.append(char)
        # If we find a closing bracket, check if the stack is empty or if the top element on the stack is not an opening bracket.
        elif char == ']':
            # If the stack is empty, it means there are closed brackets without any corresponding opening brackets, so return False.
            if not stack:
                return False
            # Pop the top element from the stack and compare it with the closing bracket.
            last_opening = stack.pop()
            # If the top element is an opening bracket, push it back onto the stack (as a sentinel value) because there's no corresponding closing bracket yet.
            if last_opening == '[':
                stack.append(last_opening)
            else:
                # If the top element is a closing bracket, check if it has a matching opening bracket in the stack.
                if last_opening != ']':
                    # If there's no more nested closed brackets (i.e., the current closing bracket doesn't have a corresponding opening bracket), return False.
                    while stack[-1] != '[':
                        stack.pop()
                else:
                    # If there are still some nested closed brackets, continue processing the string.
                    if stack:
                        continue
    # If we've processed the entire string and the stack is empty or contains only opening brackets (as sentinel values), it means there are no nested closed brackets, so return False.
    if stack or stack[-1] != '[':
        return False

    # If the stack contains only closing brackets without any corresponding opening brackets, it means there are some nested closed brackets, so return True.
    return len(stack) > 0
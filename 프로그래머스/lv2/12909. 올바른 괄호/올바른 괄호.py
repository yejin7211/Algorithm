def solution(s):
    stack = []
    for c in s:
        stack.append(c)
        if len(stack) >= 2 and stack[len(stack) - 1] == ')' and stack[len(stack) - 2] == '(':
            del stack[len(stack) - 1]
            del stack[len(stack) - 1]
    
    while len(stack) >= 2 and stack[0] == '(' and stack[len(stack) - 1] == ')':
        del stack[len(stack) - 1]
        del stack[0]
    if len(stack) == 0:
        return True
    return False
def solution(number, k):
    answer = ''

    stack = [number[0]]
    for n in number[1:]:
        while k and stack and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)

    while k:
        stack.pop()
        k -= 1
        
    return ''.join(stack)
import sys
input = sys.stdin.readline


def good_word(s):
    if len(s) % 2 == 1:
        return False
    stack = []
    for c in s:
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
        stack.append(c)
    while len(stack) >= 2 and stack[-1] == stack[-2]:
        stack.pop()
        stack.pop()
    if stack:
        return False
    return True


answer = 0
n = int(input())
for _ in range(n):
    word = input().rstrip()
    if good_word(word):
        answer += 1
print(answer)

import sys
input = sys.stdin.readline

s = input().strip()
word = input().strip()

stack = []
for c in s:
    stack.append(c)
    while len(stack) >= len(word) and ''.join(stack[-len(word):]) == word:
        for _ in range(len(word)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')

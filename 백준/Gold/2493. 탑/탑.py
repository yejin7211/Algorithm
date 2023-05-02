import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

stack = []
for idx, val in enumerate(arr):
    while stack and stack[-1][1] < val:
        stack.pop()
    if len(stack) == 0:
        print(end='0 ')
    else:
        print(stack[-1][0], end=' ')
    stack.append([idx + 1, val])

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
F = defaultdict(int)
for v in A:
    F[v] += 1

A.reverse()
stack = []
answer = []
for v in A:
    while stack and stack[-1][0] <= F[v]:
        stack.pop()
    if stack:
        answer.append(stack[-1][1])
    else:
        answer.append(-1)
    stack.append([F[v], v])

print(*list(reversed(answer)))

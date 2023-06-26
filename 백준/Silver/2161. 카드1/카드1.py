import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
for v in range(n, 0, -1):
    q.append(v)

while q:
    print(q.pop(), end=' ')
    if(q):
        v = q.pop()
        q.appendleft(v)

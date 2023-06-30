import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
q = deque()
for i in range(n):
    q.append([i+1, arr[i]])

while q:
    idx, v = q.popleft()
    print(idx, end=' ')
    if v > 0 and q:
        for _ in range(v-1):
            v1 = q.popleft()
            q.append(v1)
    elif v < 0 and q:
        for _ in range(-v):
            v2 = q.pop()
            q.appendleft(v2)

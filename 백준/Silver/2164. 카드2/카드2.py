import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque([i for i in range(1, n+1)])
while len(q) >= 2:
    tmp = q.popleft()
    num = q.popleft()
    q.append(num)

print(q.pop())

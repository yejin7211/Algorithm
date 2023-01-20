import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

visited = [float('inf') for _ in range(n+1)]
q = deque([[n, 0]])
visited[n] = n


def path(a):
    arr = [a]
    while a != n:
        arr.append(visited[a])
        a = visited[a]
    return arr[::-1]


while q:
    x, cnt = q.popleft()
    if x == 1:
        print(cnt)
        print(*path(x))
        break
    if x % 3 == 0 and x//3 >= 1 and visited[x//3] == float('inf'):
        visited[x//3] = x
        q.append([x//3, cnt+1])
    if x % 2 == 0 and x//2 >= 1 and visited[x//2] == float('inf'):
        visited[x//2] = x
        q.append([x//2, cnt+1])
    if x-1 >= 1 and visited[x-1] == float('inf'):
        visited[x-1] = x
        q.append([x-1, cnt+1])
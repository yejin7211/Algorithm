import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque([[n, 0]])
visited = [float('inf') for _ in range(100001)]
visited[n] = -1


def search_root(x):
    root = [x]
    while x != n:
        root.append(visited[x])
        x = visited[x]
    return root[::-1]


while q:
    cur, time = q.popleft()
    if cur == k:
        print(time)
        print(*search_root(cur))
        break

    for i in [-1, 1]:
        if 0 <= cur+i <= 100000 and visited[cur+i] == float('inf'):
            visited[cur+i] = cur
            q.append([cur+i, time+1])
    if cur*2 <= 100000 and visited[cur*2] == float('inf'):
        visited[cur*2] = cur
        q.append([cur*2, time+1])

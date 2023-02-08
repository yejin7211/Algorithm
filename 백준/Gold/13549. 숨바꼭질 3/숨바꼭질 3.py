import sys
from collections import deque
input = sys.stdin.readline

MAX = 100001
n, k = map(int, input().split())
visited = [False for _ in range(MAX)]
dist = [int(2e9) for _ in range(MAX)]

q = deque([n])
visited[n] = True
dist[n] = 0
while q:
    cur = q.popleft()
    if cur*2 < MAX and not visited[cur*2]:
        visited[cur*2] = True
        q.appendleft(cur*2)
        dist[cur*2] = dist[cur]
    if cur+1 < MAX and not visited[cur+1]:
        visited[cur+1] = True
        q.append(cur+1)
        dist[cur+1] = dist[cur] + 1
    if cur-1 >= 0 and not visited[cur-1]:
        visited[cur-1] = True
        q.append(cur-1)
        dist[cur-1] = dist[cur] + 1

print(dist[k])


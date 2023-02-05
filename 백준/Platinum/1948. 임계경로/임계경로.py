import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
inDegree = [0 for _ in range(n+1)]
edges = [[] for _ in range(n+1)]
edges_rev = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    edges[s].append([e, t])
    edges_rev[e].append([s, t])
    inDegree[e] += 1

s, d = map(int, input().split())

q = deque()
for i in range(1, n+1):
    if inDegree[i] == 0:
        q.append(i)

dist = [0 for _ in range(n+1)]
while q:
    cur = q.popleft()
    for v, w in edges[cur]:
        if dist[cur] + w > dist[v]:
            dist[v] = dist[cur] + w
        inDegree[v] -= 1
        if inDegree[v] == 0:
            q.append(v)

cnt = 0
visited = [0 for _ in range(n+1)]
q = deque([d])
while q:
    cur = q.popleft()
    for v, w in edges_rev[cur]:
        if dist[v] + w == dist[cur]:
            cnt += 1
            if not visited[v]:
                visited[v] = 1
                q.append(v)

print(dist[d])
print(cnt)

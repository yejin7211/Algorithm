import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


q = deque([r])
visited = [0 for _ in range(n+1)]
visited[r] = 1
cnt = 1
while q:
    cur = q.popleft()
    for v in sorted(graph[cur], reverse=True):
        if visited[v] == 0:
            cnt += 1
            visited[v] = cnt
            q.append(v)

for i in range(1, n+1):
    print(visited[i])

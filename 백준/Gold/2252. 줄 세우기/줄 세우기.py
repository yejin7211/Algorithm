import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
degree = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

q = deque()
for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)

answer = []
while q:
    cur = q.popleft()
    answer.append(cur)
    for v in graph[cur]:
        degree[v] -= 1
        if degree[v] == 0:
            q.append(v)

print(*answer)
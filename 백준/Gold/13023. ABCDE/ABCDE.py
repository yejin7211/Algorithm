import sys
from collections import defaultdict
input = sys.stdin.readline

answer = 0
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(cur, cnt):
    global answer
    if cnt == 5:
        answer = 1
        return

    for v in graph[cur]:
        if not visited[v]:
            visited[cur] = True
            dfs(v, cnt+1)
            visited[v] = False


for i in range(n):
    visited = [False for _ in range(n)]
    visited[i] = True
    dfs(i, 1)
print(answer)

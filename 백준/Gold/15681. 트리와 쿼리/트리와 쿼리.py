import sys
sys.setrecursionlimit(10**5)
from collections import defaultdict
input = sys.stdin.readline

n, r, Q = map(int, input().split())
graph = defaultdict(list)
visited = [0 for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(parent):
    visited[parent] += 1
    for child in graph[parent]:
        if visited[child] == 0:
            visited[parent] += dfs(child)
    return visited[parent]


dfs(r)

for _ in range(Q):
    print(visited[int(input())])

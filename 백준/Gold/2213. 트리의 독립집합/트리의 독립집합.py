import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, 0]] + [[0, w[i]] for i in range(n)]
path = [[[], [i]] for i in range(n+1)]
visited = [False for _ in range(n+1)]


def dfs(cur):
    visited[cur] = True
    for v in graph[cur]:
        if not visited[v]:
            dfs(v)
            dp[cur][1] += dp[v][0]
            dp[cur][0] += max(dp[v])
            path[cur][1] += path[v][0]
            if dp[v][1] > dp[v][0]:
                path[cur][0] += path[v][1]
            else:
                path[cur][0] += path[v][0]


dfs(1)
print(max(dp[1]))
print(*(sorted(path[1][0] if dp[1][0] > dp[1][1] else path[1][1])))

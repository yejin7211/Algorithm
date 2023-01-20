import sys
sys.setrecursionlimit(10**5)
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
tree = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for _ in range(n+1)]
for i in range(1, n + 1):
    dp[i][1] = p[i-1]
visited = set()


def dfs(cur):
    visited.add(cur)
    for v in tree[cur]:
        if v not in visited:
            visited.add(v)
            dfs(v)
            dp[cur][0] += max(dp[v][1], dp[v][0])
            dp[cur][1] += dp[v][0]


dfs(1)
print(max(dp[1]))

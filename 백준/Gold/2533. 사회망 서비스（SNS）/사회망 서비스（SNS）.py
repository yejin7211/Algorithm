import sys
sys.setrecursionlimit(10**7)
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
tree = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 1] for _ in range(n+1)]
visited = set()


def dfs(cur):
    visited.add(cur)
    for v in tree[cur]:
        if v not in visited:
            visited.add(v)
            dfs(v)
            dp[cur][0] += dp[v][1]
            dp[cur][1] += min(dp[v][0], dp[v][1])


dfs(1)

print(min(dp[1][0], dp[1][1]))
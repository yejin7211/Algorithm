import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

cnt = 1
def dfs(cur):
    global cnt
    answer[cur] = cnt
    for pos in sorted(graph[cur], reverse=True):
        if answer[pos] == 0:
            cnt += 1
            dfs(pos)


n, m, r = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = [0 for _ in range(n+1)]
dfs(r)
for i in range(1, n+1):
    print(answer[i])

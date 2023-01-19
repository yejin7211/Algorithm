import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dist = [float('inf') for _ in range(n+1)]


def bf(s):
    dist[s] = 0
    for i in range(n):
        for j in range(m):
            s, e, w = graph[j][0], graph[j][1], graph[j][2]
            if dist[s] != float('inf') and dist[s] + w < dist[e]:
                dist[e] = dist[s] + w
                if i == n-1:
                    return True
    return False


negative_cycle = bf(1)
if negative_cycle:
    print(-1)
else:
    for i in range(2, n+1):
         print(dist[i] if dist[i] != float('inf') else -1)

import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

n, e = map(int, input().split())
k = int(input())

graph = defaultdict(list)
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

dist = [float('inf') for _ in range(n+1)]
heap = [[0, k]]
dist[k] = 0
while heap:
    cost, cur = heappop(heap)
    if dist[cur] < cost:
        continue
    for v, w in graph[cur]:
        if cost + w < dist[v]:
            dist[v] = cost + w
            heappush(heap, [dist[v], v])

for i in range(1, n+1):
    if dist[i] == float('inf'):
        print('INF')
    else:
        print(dist[i])
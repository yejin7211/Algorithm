import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

k_minTime = [[int(1e9) for _ in range(k)] for _ in range(n+1)]
heap = [[0, 1]]
k_minTime[1][0] = 0
while heap:
    time, cur = heappop(heap)
    for v, w in graph[cur]:
        if time+w < k_minTime[v][k-1]:
            k_minTime[v][k-1] = time+w
            k_minTime[v].sort()
            heappush(heap, [time+w, v])

for i in range(1, n+1):
    if k_minTime[i][k-1] == int(1e9):
        print(-1)
    else:
        print(k_minTime[i][k-1])

import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
degree = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

heap = [i for i in range(1, n+1) if degree[i] == 0]

answer = []
while heap:
    cur = heappop(heap)
    answer.append(cur)
    for v in graph[cur]:
        degree[v] -= 1
        if degree[v] == 0:
            heappush(heap, v)

print(*answer)

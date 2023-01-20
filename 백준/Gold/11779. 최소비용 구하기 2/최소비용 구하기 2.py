import sys
from heapq import heappush, heappop
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
s, e = map(int, input().split())

dist = [float('inf') for _ in range(n+1)]
heap = [[0, s, [s]]]
dist[s] = 0
while heap:
    cost, cur, visited = heappop(heap)
    if cur == e:
        print(cost)
        print(len(visited))
        print(*visited)
        break
    for pos, wei in graph[cur]:
        if dist[cur] + wei < dist[pos]:
            dist[pos] = dist[cur] + wei
            heappush(heap, [dist[pos], pos, visited+[pos]])

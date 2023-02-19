import sys
from heapq import heappush, heappop
from collections import defaultdict
input = sys.stdin.readline


def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    root[max(x, y)] = min(x, y)


def dijkstra(s, e):
    dist = [int(1e9) for _ in range(n+1)]
    heap = [[0, s]]
    dist[s] = 0
    while heap:
        d, cur = heappop(heap)
        if cur == e:
            return d
        for v, w in graph[cur]:
            if d + w < dist[v]:
                dist[v] = d + w
                heappush(heap, [d+w, v])
    return int(1e9)


answer = 0
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
root = [i for i in range(n+1)]
edges = []
for i in range(n):
    for j in range(n):
        edges.append([i+1, j+1, board[i][j]])
edges.sort(key=lambda x: x[2])

graph = defaultdict(list)
for a, b, c in edges:
    if dijkstra(a, b) < c:
        answer = -1
        break
    if find(a) != find(b) or c < dijkstra(a, b):
        union(find(a), find(b))
        graph[a].append((b, c))
        graph[b].append((a, c))
        answer += c

print(answer)

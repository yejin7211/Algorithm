import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline


def dijkstra(start):
    dist = [100000000 for _ in range(n+1)]
    heap = [[0, start]]
    dist[start] = 0
    while heap:
        v, cur = heappop(heap)
        if dist[cur] < v:
            continue
        for pos, wei in graph[cur]:
            if dist[cur] + wei < dist[pos]:
                dist[pos] = dist[cur] + wei
                heappush(heap, [dist[pos], pos])
    return dist


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d])

    s_ = dijkstra(s)
    g_ = dijkstra(g)
    h_ = dijkstra(h)

    answer = []
    for _ in range(t):
        x = int(input())
        if s_[g]+g_[h]+h_[x] == s_[x] or s_[h]+h_[g]+g_[x] == s_[x]:
            answer.append(x)
    print(*sorted(answer))

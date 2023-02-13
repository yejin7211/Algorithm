import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    visited_time = [int(1e9) for _ in range(n+1)]
    heap = [[0, c]]
    visited_time[c] = 0
    while heap:
        time, cur = heappop(heap)
        for v, t in graph[cur]:
            if time + t < visited_time[v]:
                visited_time[v] = time + t
                heappush(heap, [time + t, v])

    infected_computer = 0
    infected_maxTime = 0
    for i in range(1, n+1):
        if visited_time[i] != int(1e9):
            infected_computer += 1
            infected_maxTime = max(infected_maxTime, visited_time[i])
    print(infected_computer, infected_maxTime)

import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline


def dijkstra():
    distance = [int(1e9) for _ in range(n)]
    heap = [[0, s]]
    distance[s] = 0
    while heap:
        dist, cur = heappop(heap)
        if distance[cur] < dist:
            continue
        for v, w in edge[cur]:
            if distance[cur] + w < distance[v] and not check[cur][v]:
                distance[v] = distance[cur] + w
                heappush(heap, [distance[v], v])
    return distance


def bfs():
    q = deque([d])
    while q:
        cur = q.popleft()
        if cur == s:
            continue
        for pre_v, pre_c in edge_rev[cur]:
            if distance[pre_v] + pre_c == distance[cur] and not check[pre_v][cur]:
                check[pre_v][cur] = True
                q.append(pre_v)


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    s, d = map(int, input().split())
    edge = [[] for _ in range(n)]
    edge_rev = [[] for _ in range(n)]
    check = [[False for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        edge[u].append([v, p])
        edge_rev[v].append([u, p])

    distance = dijkstra()
    bfs()
    distance = dijkstra()

    print(distance[d] if distance[d] != int(1e9) else -1)

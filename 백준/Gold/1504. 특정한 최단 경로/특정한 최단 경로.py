import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

n, e = map(int, input().split())
connect = defaultdict(list)
for _ in range(e):
    a, b, c = map(int, input().split())
    connect[a].append([b, c])
    connect[b].append([a, c])
v1, v2 = map(int, input().split())


def move(cur, target):
    heap = [[0, cur]]
    dist = [987654321 for _ in range(n+1)]
    dist[cur] = 0
    while heap:
        distance, cur = heappop(heap)
        if cur == target:
            return distance
        for pos, cost in connect[cur]:
            if dist[cur] + cost < dist[pos]:
                dist[pos] = dist[cur] + cost
                heappush(heap, [dist[pos], pos])
    return -1


cnt1, cnt2 = -1, -1
if move(1, v1) != -1 and move(v1, v2) != -1 and move(v2, n) != -1:
    cnt1 = move(1, v1) + move(v1, v2) + move(v2, n)
if move(1, v2) != -1 and move(v2, v1) != -1 and move(v1, n) != -1:
    cnt2 = move(1, v2) + move(v2, v1) + move(v1, n)

if cnt1 == -1 or cnt2 == -1:
    print(max(cnt1, cnt2))
else:
    print(min(cnt1, cnt2))

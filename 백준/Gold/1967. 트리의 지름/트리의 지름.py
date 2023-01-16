import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def search(cur):
    dist = [float('inf') for _ in range(n+1)]
    dist[cur] = 0
    q = deque([cur])
    while q:
        cur = q.popleft()
        for pos, wei in graph[cur]:
            if dist[cur] + wei <= dist[pos]:
                dist[pos] = dist[cur] + wei
                q.append(pos)
    return dist[1:]


n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append([c, w])
    graph[c].append([p, w])

distances = search(1)
start_node = distances.index(max(distances)) + 1
print(max(search(start_node)))
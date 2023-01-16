import sys
from collections import deque, defaultdict
input = sys.stdin.readline


def search(cur):
    dist = [float('inf') for _ in range(V + 1)]
    q = deque([cur])
    dist[cur] = 0
    while q:
        cur = q.popleft()
        for v, w in graph[cur]:
            if dist[cur] + w < dist[v]:
                dist[v] = dist[cur] + w
                q.append(v)
    return dist[1:]


V = int(input())
graph = defaultdict(list)
for _ in range(V):
    nums = list(map(int, input().split()))
    for i in range(1, len(nums)-1, 2):
        graph[nums[0]].append([nums[i], nums[i+1]])


distances = search(1)
start_node = distances.index(max(distances)) + 1
print(max(search(start_node)))

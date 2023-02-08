import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False for _ in range(max(n*2, k*2))]

heap = [[0, n]]
visited[n] = True
while heap:
    Time, cur = heappop(heap)
    if cur == k:
        print(Time)
        break

    if cur * 2 <= k*2 and not visited[cur*2]:
        visited[cur*2] = True
        heappush(heap, [Time, cur*2])
    if cur-1 >= 0 and not visited[cur-1]:
        visited[cur-1] = True
        heappush(heap, [Time+1, cur-1])
    if cur+1 <= k*2 and not visited[cur+1]:
        visited[cur+1] = True
        heappush(heap, [Time+1, cur+1])

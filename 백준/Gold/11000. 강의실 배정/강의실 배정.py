import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
classes = sorted(list(list(map(int, input().split())) for _ in range(n)))

heap = []
for s, t in classes:
    if heap and heap[0] <= s:
        heappop(heap)
    heappush(heap, t)

print(len(heap))

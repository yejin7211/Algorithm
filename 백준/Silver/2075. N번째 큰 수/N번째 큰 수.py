import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def search_max_in_row(r):  # O(n)
    max_c, max_v = -int(2e9), -int(2e9)
    for j in range(n):
        if arr[r][j] > max_v:
            max_v = arr[r][j]
            max_c = j
    return [-max_v, r, max_c]


n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))

heap = []
heappush(heap, search_max_in_row(n-1))
last_rowIdx, last_rowIdx_count = n-1, 0
for _ in range(n-1):
    item, rowIdx, colIdx = heappop(heap)
    arr[rowIdx][colIdx] = -int(2e9)
    if rowIdx == last_rowIdx:
        last_rowIdx_count += 1
        if last_rowIdx_count == n:
            last_rowIdx -= 1
            last_rowIdx_count = 0
        heappush(heap, search_max_in_row(last_rowIdx))
    if rowIdx != 0:
        heappush(heap, [-arr[rowIdx-1][colIdx], rowIdx-1, colIdx])

item, rowIdx, colIdx = heappop(heap)
print(item * -1)

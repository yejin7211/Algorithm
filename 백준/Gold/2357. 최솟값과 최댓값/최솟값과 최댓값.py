import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
minV = [int(1e9) for _ in range(n*4)]
maxV = [0 for _ in range(n*4)]


def init_minV(start, end, idx):
    if start == end:
        minV[idx] = min(minV[idx], arr[start])
        return minV[idx]

    mid = (start + end) // 2
    minV[idx] = min(init_minV(start, mid, idx*2), init_minV(mid+1, end, idx*2+1))
    return minV[idx]


def init_maxV(start, end, idx):
    if start == end:
        maxV[idx] = max(maxV[idx], arr[start])
        return maxV[idx]

    mid = (start + end) // 2
    maxV[idx] = max(init_maxV(start, mid, idx*2), init_maxV(mid+1, end, idx*2+1))
    return maxV[idx]


init_minV(0, n-1, 1)
init_maxV(0, n-1, 1)


def interval_minV(start, end, idx, left, right):
    if end < left or right < start:
        return int(1e9)
    if left <= start and end <= right:
        return minV[idx]

    mid = (start + end) // 2
    return min(interval_minV(start, mid, idx*2, left, right), interval_minV(mid+1, end, idx*2+1, left, right))


def interval_maxV(start, end, idx, left, right):
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return maxV[idx]

    mid = (start + end) // 2
    return max(interval_maxV(start, mid, idx*2, left, right), interval_maxV(mid+1, end, idx*2+1, left, right))


for _ in range(m):
    a, b = map(int, input().split())
    print(interval_minV(0, n-1, 1, a-1, b-1), interval_maxV(0, n-1, 1, a-1, b-1))

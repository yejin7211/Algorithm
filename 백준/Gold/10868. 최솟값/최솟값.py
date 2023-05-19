import sys
input = sys.stdin.readline


def init(start, end, idx):
    if start == end:
        tree[idx] = min(tree[idx], arr[start])
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = min(init(start, mid, idx*2), init(mid+1, end, idx*2+1))
    return tree[idx]


def interval_min(start, end, idx, left, right):
    if end < left or right < start:
        return INF
    if left <= start and end <= right:
        return tree[idx]
    mid = (start + end) // 2
    return min(interval_min(start, mid, idx*2, left, right), interval_min(mid+1, end, idx*2+1, left, right))


INF = int(2e9)
n, m = map(int, input().split())
arr = list(int(input()) for _ in range(n))
tree = [INF for _ in range(n * 4)]
init(0, n-1, 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(interval_min(0, n-1, 1, a-1, b-1))

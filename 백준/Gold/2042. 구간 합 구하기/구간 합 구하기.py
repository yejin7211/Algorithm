import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [0 for _ in range(n*4)]


def init(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]

    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx*2) + init(mid+1, end, idx*2+1)
    return tree[idx]


init(0, n-1, 1)


def update(start, end, idx, diff, value):
    if diff < start or end < diff:
        return

    tree[idx] += value
    if start == end:
        return

    mid = (start + end) // 2
    update(start, mid, idx*2, diff, value)
    update(mid+1, end, idx*2+1, diff, value)


def interval_sum(start, end, idx, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[idx]

    mid = (start + end) // 2
    return interval_sum(start, mid, idx*2, left, right) + interval_sum(mid+1, end, idx*2+1, left, right)


for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        size = c-arr[b-1]
        arr[b-1] = c
        update(0, n-1, 1, b-1, size)
    if a == 2:
        print(interval_sum(0, n-1, 1, b-1, c-1))

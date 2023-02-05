import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [0] + [int(input()) for _ in range(n)]
tree = [1 for _ in range((n+1)*4)]


def init(start, end, idx):
    if start == end:
        tree[idx] = (tree[idx] * arr[start]) % 1000000007
        return tree[idx]

    mid = (start + end) // 2
    tree[idx] = (init(start, mid, idx*2) * init(mid+1, end, idx*2+1)) % 1000000007
    return tree[idx]


init(1, n, 1)


def update(start, end, idx, diff, value):
    if start > diff or diff > end:
        return

    tree[idx] = value
    if start < diff:
        tree[idx] = (tree[idx] * interval_multi(1, n, 1, start, diff-1)) % 1000000007
    if diff < end:
        tree[idx] = (tree[idx] * interval_multi(1, n, 1, diff+1, end)) % 1000000007
    if start == end:
        return

    mid = (start + end) // 2
    update(start, mid, idx*2, diff, value)
    update(mid+1, end, idx*2+1, diff, value)


def interval_multi(start, end, idx, left, right):
    if right < start or end < left:
        return 1
    if left <= start and end <= right:
        return tree[idx]

    mid = (start + end) // 2
    return (interval_multi(start, mid, idx*2, left, right) * interval_multi(mid+1, end, idx*2+1, left, right)) % 1000000007


for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b] = c
        update(1, n, 1, b, c)
    if a == 2:
        print(interval_multi(1, n, 1, b, c))

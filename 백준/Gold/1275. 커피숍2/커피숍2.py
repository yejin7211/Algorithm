import sys
input = sys.stdin.readline


def init(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx*2) + init(mid+1, end, idx*2+1)
    return tree[idx]


def interval_sum(start, end, idx, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[idx]
    mid = (start + end) // 2
    return interval_sum(start, mid, idx*2, left, right) + interval_sum(mid+1, end, idx*2+1, left, right)


def change_tree(start, end, idx, key, wei):
    if key < start or end < key:
        return
    tree[idx] -= wei
    if start == end:
        return
    mid = (start + end) // 2
    change_tree(start, mid, idx*2, key, wei)
    change_tree(mid+1, end, idx*2+1, key, wei)


n, q = map(int, input().split())
arr = list(map(int, input().split()))
tree = [0 for _ in range(n * 4)]
init(0, n-1, 1)

for _ in range(q):
    x, y, a, b = map(int, input().split())
    print(interval_sum(0, n-1, 1, min(x, y)-1, max(x, y)-1))
    change_tree(0, n-1, 1, a-1, arr[a-1]-b)
    arr[a - 1] = b

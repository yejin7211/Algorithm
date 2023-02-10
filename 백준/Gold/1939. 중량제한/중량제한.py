import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
v1, v2 = map(int, input().split())
root = [i for i in range(n+1)]


def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    root[max(x, y)] = min(x, y)


edges.sort(key=lambda x: -x[2])
for a, b, c in edges:
    a_root = find(a)
    b_root = find(b)
    union(a_root, b_root)
    if find(v1) == find(v2):
        print(c)
        break

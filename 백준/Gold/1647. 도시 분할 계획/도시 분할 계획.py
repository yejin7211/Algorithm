import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paths = [list(map(int, input().split())) for _ in range(m)]
root = [i for i in range(n+1)]

paths.sort(key=lambda x: x[2])


def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    root[max(x, y)] = min(x, y)


costs = []
for a, b, c in paths:
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        union(root_a, root_b)
        costs.append(c)

print(sum(costs) - max(costs))

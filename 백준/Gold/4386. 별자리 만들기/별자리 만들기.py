import sys
from math import sqrt
input = sys.stdin.readline

n = int(input())
pos = [[]] + [list(map(float, input().split())) for _ in range(n)]
root = [i for i in range(n+1)]
edges = []
for i in range(1, n+1):
    for j in range(i+1, n+1):
        x1, y1 = pos[i]
        x2, y2 = pos[j]
        dist = sqrt((x1-x2)**2 + (y1-y2)**2)
        edges.append([i, j, dist])
edges.sort(key=lambda x: x[2])


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    root[max(root_y, root_x)] = min(root_y, root_x)


def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


answer = 0
for u, v, dist in edges:
    if find(u) != find(v):
        answer += dist
        union(u, v)
print('%.2lf' % answer)

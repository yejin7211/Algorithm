import sys
from math import sqrt
input = sys.stdin.readline

n, m = map(int, input().split())
pos = [[]] + [list(map(int, input().split())) for _ in range(n)]

edges = []
for n1 in range(1, n+1):
    for n2 in range(n1+1, n+1):
        x1, y1 = pos[n1]
        x2, y2 = pos[n2]
        dist = sqrt((x1-x2)**2 + (y1-y2)**2)
        edges.append((dist, n1, n2))
edges.sort(key=lambda x: x[0])


def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_y < root_x:
        root[root_x] = root_y
    if root_y > root_x:
        root[root_y] = root_x


root = [i for i in range(n+1)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    union(n1, n2)

answer = 0
for dist, n1, n2 in edges:
    if find(n1) != find(n2):
        union(n1, n2)
        answer += dist

print(format(answer, '.2f'))

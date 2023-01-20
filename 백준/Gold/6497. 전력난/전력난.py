# 크루스칼 알고리즘(Kruskal Algorithm)
# 탐욕법(greedy method)

import sys
input = sys.stdin.readline


def find(a):
    if a != root[a]:
        root[a] = find(root[a])
    return root[a]


def union(a, b):
    if a > b:
        root[a] = b
    else:
        root[b] = a


while True:
    answer = 0
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    graph.sort(key=lambda x: x[2])
    root = [i for i in range(m+1)]
    for x, y, z in graph:
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            union(root_x, root_y)
        else:
            answer += z

    print(answer)

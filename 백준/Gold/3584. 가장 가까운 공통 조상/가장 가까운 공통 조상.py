import sys
from collections import defaultdict, deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[b].append(a)
    v1, v2 = map(int, input().split())

    path = {v1}
    while graph[v1]:
        v1 = graph[v1][0]
        path.add(v1)

    if v2 in path:
        print(v2)
        continue
    cur = v2
    while graph[v2]:
        v2 = graph[v2][0]
        if v2 in path:
            print(v2)
            break

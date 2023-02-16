import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
graph = defaultdict(list)
inDegree = [0 for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

q = deque()
for i in range(1, n+1):
    if inDegree[i] == 0:
        q.append(i)

moved = [set() for _ in range(n+1)]
while q:
    cur = q.popleft()
    for v in graph[cur]:
        inDegree[v] -= 1
        moved[v].add(cur)
        moved[v] |= moved[cur]
        if inDegree[v] == 0:
            q.append(v)

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if a in moved[b] and b not in moved[a]:
        print(-1)
    elif b in moved[a] and a not in moved[b]:
        print(1)
    else:
        print(0)

'''
-1: b에는 a가 있고, a에는 b가 없다
1: a에는 b가 있고, b에는 a가 없다
0: 그 외
'''

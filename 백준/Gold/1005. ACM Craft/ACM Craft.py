import sys
from collections import defaultdict, deque
from copy import deepcopy
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    dp = deepcopy(d)
    inDegree = [0 for _ in range(n+1)]
    edges = defaultdict(list)
    for _ in range(k):
        x, y = map(int, input().split())
        edges[x].append(y)
        inDegree[y] += 1
    w = int(input())

    q = deque()
    for i in range(1, n+1):
        if inDegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        for v in edges[cur]:
            inDegree[v] -= 1
            dp[v] = max(dp[v], dp[cur]+d[v])
            if inDegree[v] == 0:
                q.append(v)

    print(dp[w])

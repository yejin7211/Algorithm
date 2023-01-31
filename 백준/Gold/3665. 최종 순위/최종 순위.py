import sys
from collections import defaultdict, deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    graph = defaultdict(list)
    indegree = [0 for _ in range(n+1)]
    score = list(map(int, input().split()))
    for i in range(n-1):
        for j in range(i+1, n):
            graph[score[i]].append(score[j])
            indegree[score[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if a in graph[b]:
            graph[b].remove(a)
            indegree[a] -= 1
            graph[a].append(b)
            indegree[b] += 1
        elif b in graph[a]:
            graph[a].remove(b)
            indegree[b] -= 1
            graph[b].append(a)
            indegree[a] += 1

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    answer = []
    while q:
        cur = q.popleft()
        answer.append(cur)
        for v in graph[cur]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    if len(answer) < n:
        print('IMPOSSIBLE')
    else:
        print(*answer)

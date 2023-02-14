import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
inDegree = [0 for _ in range(n+1)]
for _ in range(m):
    arr = list(map(int, input().split()))
    for i in range(2, len(arr)):
        graph[arr[i-1]].append(arr[i])
        inDegree[arr[i]] += 1

q = deque()
for i in range(1, n+1):
    if inDegree[i] == 0:
        q.append(i)

answer = []
while q:
    cur = q.popleft()
    answer.append(cur)
    for v in graph[cur]:
        inDegree[v] -= 1
        if inDegree[v] == 0:
            q.append(v)

if len(answer) == n:
    for v in answer:
        print(v)
else:
    print(0)

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
time = [0 for _ in range(n+1)]
total_time = [0 for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
graph = defaultdict(list)
for i in range(1, n+1):
    arr = list(map(int, input().split()))
    time[i] = total_time[i] = arr[0]
    for j in range(1, len(arr)-1):
        graph[arr[j]].append(i)
        inDegree[i] += 1

q = deque()
for i in range(1, n+1):
    if inDegree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    for v in graph[cur]:
        inDegree[v] -= 1
        total_time[v] = max(total_time[v], time[v]+total_time[cur])
        if inDegree[v] == 0:
            q.append(v)

for i in range(1, n+1):
    print(total_time[i])

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque([r])
answer = [0 for _ in range(n+1)]
answer[r] = 1
cnt = 1
while q:
    cur = q.popleft()
    for v in sorted(graph[cur]):
        if answer[v] == 0:
            cnt += 1
            q.append(v)
            answer[v] = cnt

for v in answer[1:]:
    print(v)

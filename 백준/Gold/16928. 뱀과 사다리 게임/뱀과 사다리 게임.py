import sys
from collections import deque
input = sys.stdin.readline

# input
moveMap = {}
n, m = map(int, input().split())
for _ in range(n + m):
    x, y = map(int, input().split())
    moveMap[x] = y

visited = [False] * 101
queue = deque([(1, 0)])
visited[1] = True

# bfs
while queue:
    cur, cnt = queue.popleft()
    if cur == 100:
        print(cnt)
        break

    for i in range(1, 7):
        new = cur + i
        if new > 100 or visited[new]:
            continue
        if new in moveMap:
            new = moveMap[new]

        queue.append((new, cnt + 1))
        visited[new] = True

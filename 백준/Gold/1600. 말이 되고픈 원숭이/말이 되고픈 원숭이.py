import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0, -1, -2, -2, -1, 1, 2, 2, 1]
dx = [0, 0, -1, 1, -2, -1, 1, 2, -2, -1, 1, 2]

k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
visited = [[[False for _ in range(k+1)] for _ in range(w)] for _ in range(h)]

q = deque([[0, k, 0, 0]])
visited[0][0][k] = True
while q:
    cnt, k, y, x = q.popleft()
    if y == h-1 and x == w-1:
        print(cnt)
        exit(0)
    if k > 0:
        for i in range(4, 12):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            if board[ny][nx] == 0 and not visited[ny][nx][k-1]:
                visited[ny][nx][k-1] = True
                q.append([cnt+1, k-1, ny, nx])
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny < 0 or ny >= h or nx < 0 or nx >= w:
            continue
        if board[ny][nx] == 0 and not visited[ny][nx][k]:
            visited[ny][nx][k] = True
            q.append([cnt+1, k, ny, nx])

print(-1)

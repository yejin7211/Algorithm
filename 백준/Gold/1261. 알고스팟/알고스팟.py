import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

m, n = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
broken_wallCnt = [[int(2e9) for _ in range(m)] for _ in range(n)]
for i in range(n):
    row = input()
    for j in range(m):
        board[i][j] = int(row[j])

q = deque([[0, 0, 0]])
visited[0][0] = True
broken_wallCnt[0][0] = 0
while q:
    y, x, cnt = q.popleft()
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue
        if not visited[ny][nx]:
            visited[ny][nx] = True
            if board[ny][nx] == 0:
                q.appendleft([ny, nx, cnt])
                broken_wallCnt[ny][nx] = broken_wallCnt[y][x]
            if board[ny][nx] == 1:
                q.append([ny, nx, cnt+1])
                broken_wallCnt[ny][nx] = broken_wallCnt[y][x]+1

print(broken_wallCnt[n-1][m-1])

import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs1(y, x):
    q = deque([(y, x)])
    visited[y][x] = True
    board[y][x] = count
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if board[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = 1
                board[ny][nx] = count
                q.append((ny, nx))


def bfs2(color):
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if board[i][j] == color:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if board[ny][nx] != 0 and board[ny][nx] != color:
                return dist[y][x]
            if board[ny][nx] == 0 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
count = 1
for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j]:
            bfs1(i, j)
            count += 1

answer = float('inf')
for i in range(1, count):
    answer = min(answer, bfs2(i))
print(answer)

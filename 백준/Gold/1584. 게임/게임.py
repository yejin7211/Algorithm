import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

board = [[0 for _ in range(501)] for _ in range(501)]
life = [[int(2e9) for _ in range(501)] for _ in range(501)]

n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            board[i][j] = max(board[i][j], 1)

m = int(input())
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            board[i][j] = max(board[i][j], 2)

# 0-1 BFS 알고리즘
q = deque([[0, 0, 0]])
life[0][0] = 0
while q:
    y, x, v = q.popleft()
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny < 0 or ny > 500 or nx < 0 or nx > 500:
            continue
        if board[ny][nx] == 0 and life[ny][nx] > life[y][x]:
            life[ny][nx] = life[y][x]
            q.appendleft([ny, nx, v])
        if board[ny][nx] == 1 and life[ny][nx] > life[y][x]+1:
            life[ny][nx] = life[y][x]+1
            q.append([ny, nx, v+1])

print(life[500][500] if life[500][500] != int(2e9) else -1)

import sys
from collections import deque
input = sys.stdin.readline

dy = [0, -1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, 0, -1, 1, -1, 1, -1, 1]

answer = 0
board = [list(input().rstrip()) for _ in range(8)]
q = deque([(7, 0)])
while q:
    size = len(q)
    for _ in range(size):
        y, x = q.popleft()
        if y == 0 and x == 7:
            print(1)
            exit(0)
        for i in range(9):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= 8 or nx < 0 or nx >= 8:
                continue
            if board[ny][nx] == '.':
                q.append((ny, nx))

    for i in range(7, 0, -1):
        for j in range(8):
            board[i][j] = board[i-1][j]
    for j in range(8):
        board[0][j] = '.'

    size2 = len(q)
    for _ in range(size2):
        y, x = q.popleft()
        if board[y][x] == '.':
            q.append((y, x))

print(0)

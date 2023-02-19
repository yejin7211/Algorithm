import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

h, w = map(int, input().split())
board = [list(input().rstrip()) for _ in range(h)]
sand_q = deque()
for i in range(h):
    for j in range(w):
        if board[i][j] == '.':
            board[i][j] = 0
            sand_q.append((i, j))
        else:
            board[i][j] = int(board[i][j])

count = 0
while True:
    size = len(sand_q)
    for _ in range(size):
        y, x = sand_q.popleft()
        for i in range(8):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            if board[ny][nx] > 0:
                board[ny][nx] -= 1
                if board[ny][nx] == 0:
                    sand_q.append((ny, nx))
    if len(sand_q) == 0:
        break
    count += 1

print(count)

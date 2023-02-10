import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
L_pos = []
for i in range(r):
    for j in range(c):
        if board[i][j] == 'L':
            L_pos.append((i, j, str(len(L_pos)+1)))


def expanding_L(y, x, k):
    global L_pos
    q = deque([(y, x)])
    board[y][x] = k
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if board[ny][nx] == '.':
                board[ny][nx] = k
                L_pos.append((ny, nx, k))
                q.append((ny, nx))
            if board[ny][nx] == 'L':
                print(0)
                exit(0)


expanding_L(L_pos[0][0], L_pos[0][1], '1')
expanding_L(L_pos[1][0], L_pos[1][1], '2')

water_pos = []
for i in range(r):
    for j in range(c):
        if board[i][j] != 'X':
            water_pos.append((i, j))


def melting():
    global water_pos
    q = deque(water_pos)
    water_pos = []

    size = len(q)
    for _ in range(size):
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if board[ny][nx] == 'X':
                board[ny][nx] = '.'
                water_pos.append((ny, nx))


def move_L():
    global L_pos
    q = deque(L_pos)

    L_pos = []
    while q:
        y, x, k = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if board[ny][nx] == '.':
                board[ny][nx] = k
                L_pos.append((ny, nx, k))
                q.append((ny, nx, k))
            if board[ny][nx] != 'X' and board[ny][nx] != k:
                return 1
    return 0


day = 0
while True:
    day += 1
    melting()
    res = move_L()
    if res == 1:
        break

print(day)

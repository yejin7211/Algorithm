import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = -1
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def separated():
    mountain = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                mountain[i][j] = 1
                cnt += 1
                if len(q) == 0:
                    q.append((i, j))
    if cnt == 0:
        return -1

    while q:
        y, x = q.popleft()
        mountain[y][x] = 0
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if mountain[ny][nx]:
                mountain[ny][nx] = 0
                q.append((ny, nx))

    for i in range(n):
        for j in range(m):
            if mountain[i][j]:
                return 1
    return 0


while True:
    answer += 1
    state = separated()
    if state in [-1, 1]:
        print(answer if state == 1 else 0)
        break

    contacted = [[0 for _ in range(m)] for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if board[y][x]:
                for i in range(4):
                    ny, nx = y+dy[i], x+dx[i]
                    if ny < 0 or ny >= n or nx < 0 or nx >= m:
                        continue
                    if board[ny][nx] == 0:
                        contacted[y][x] += 1

    for i in range(n):
        for j in range(m):
            board[i][j] = max(0, board[i][j]-contacted[i][j])

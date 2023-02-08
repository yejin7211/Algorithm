import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x):
    visited = [[-1 for _ in range(w+2)] for _ in range(h+2)]
    q = deque([[y, x]])
    visited[y][x] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= h+2 or nx < 0 or nx >= w+2:
                continue
            if visited[ny][nx] == -1:
                if board[ny][nx] == '#':
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])
                elif board[ny][nx] in ['.', '$']:
                    visited[ny][nx] = visited[y][x]
                    q.appendleft([ny, nx])

    return visited


t = int(input())
for _ in range(t):
    answer = int(2e9)
    h, w = map(int, input().split())
    board = [['.' for _ in range(w+2)] for _ in range(h+2)]
    persons_pos = []
    for i in range(h):
        row = input().rstrip()
        for j in range(w):
            board[i+1][j+1] = row[j]
            if board[i+1][j+1] == '$':
                persons_pos.append((i+1, j+1))

    dp1 = bfs(0, 0)
    y, x = persons_pos.pop()
    dp2 = bfs(y, x)
    y, x = persons_pos.pop()
    dp3 = bfs(y, x)

    for i in range(h+2):
        for j in range(w+2):
            if dp1[i][j] != -1 and dp2[i][j] != -1 and dp3[i][j] != -1:
                res = dp1[i][j] + dp2[i][j] + dp3[i][j]
                if board[i][j] == '#':
                    res -= 2
                answer = min(answer, res)

    print(answer)

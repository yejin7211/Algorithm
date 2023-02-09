import sys
from collections import deque
input = sys.stdin.readline

answer = int(2e9)
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

virus = []
blank = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus.append((i, j))
        if board[i][j] == 0:
            blank += 1

selected = []


def bfs():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque(selected)
    for y, x in selected:
        visited[y][x] = 0

    cnt = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if visited[ny][nx] == -1 and board[ny][nx] != 1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))
                if board[ny][nx] == 0:
                    cnt += 1
                    if cnt == blank:
                        return visited[ny][nx]

    if cnt == blank:
        return 0
    return int(2e9)


def dfs(idx, cnt):
    global answer
    if cnt == m:
        answer = min(answer, bfs())
        return

    for i in range(idx, len(virus)):
        selected.append(virus[i])
        dfs(i+1, cnt+1)
        selected.pop()


dfs(0, 0)
print(answer if answer != int(2e9) else -1)

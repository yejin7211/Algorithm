import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(i, j):
    group = [0, 0, 0, j, (i, j)]  # 그룹 크기, 무지개 블록, 기준 블록 행, 최대 열
    color = board[i][j]
    normal_blocks = [(i, j)]
    rainbow_blocks = []
    q = deque([(i, j)])
    visited[i][j] = True
    while q:
        y, x = q.popleft()
        group[0] += 1
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if not visited[ny][nx]:
                if board[ny][nx] == color:
                    normal_blocks.append((ny, nx))
                    visited[ny][nx] = True
                    group[3] = max(group[3], nx)
                    q.append((ny, nx))
                if board[ny][nx] == 0:
                    rainbow_blocks.append((ny, nx))
                    group[1] += 1
                    visited[ny][nx] = True
                    group[3] = max(group[3], nx)
                    q.append((ny, nx))
    for y, x in rainbow_blocks:
        visited[y][x] = False
    normal_blocks.sort(key=lambda x: (x[0], x[1]))
    group[2] = normal_blocks[0][0]
    return group


def bfs2(y, x):
    color = board[y][x]
    visited2 = [[False for _ in range(n)] for _ in range(n)]
    q = deque([(y, x)])
    visited2[y][x] = True
    while q:
        y, x = q.popleft()
        board[y][x] = -2
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if not visited2[ny][nx]:
                if board[ny][nx] == color or board[ny][nx] == 0:
                    visited2[ny][nx] = True
                    q.append((ny, nx))


def gravity():
    for i in range(n-1, -1, -1):
        for j in range(n):
            if 0 <= board[i][j] <= m:
                y = i
                while y+dy[1] < n and board[y+dy[1]][j] == -2:
                    y += dy[1]
                board[y][j], board[i][j] = board[i][j], board[y][j]


def rotation():
    global board
    arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] = board[j][n-i-1]
    board = arr


answer = 0
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    block_groups = []
    for i in range(n):
        for j in range(n):
            if 1 <= board[i][j] <= m and not visited[i][j]:
                group = bfs(i, j)
                if group[0] >= 2:
                    block_groups.append(group)
    block_groups.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
    if len(block_groups) == 0:
        break

    y, x = block_groups[0][4]
    answer += block_groups[0][0]**2
    bfs2(y, x)

    gravity()
    rotation()
    gravity()


print(answer)

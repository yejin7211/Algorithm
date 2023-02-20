import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def search(y, x, d):
    while True:
        if board[y][x] == 'x':
            board[y][x] = '.'
            break
        x = x+dx[d]
        if x < 0 or x >= c:
            break


def bfs(y, x, k):
    poses = []
    visited[y][x] = k
    q = deque([(y, x)])
    while q:
        y, x = q.popleft()
        poses.append((y, x))
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if board[ny][nx] == 'x' and not visited[ny][nx]:
                visited[ny][nx] = k
                q.append((ny, nx))
    return poses


def gravity(poses):
    poses.sort(key=lambda x: (-x[0], x[1]))
    q = deque(poses)
    min_move_cnt = int(1e9)
    while q:
        y, x = q.popleft()
        ny = y
        while ny+dy[1] < r and (board[ny+dy[1]][x] == '.' or visited[ny+dy[1]][x] == visited[y][x]):
            ny += dy[1]
        min_move_cnt = min(min_move_cnt, ny-y)

    q = deque(poses)
    while q:
        y, x = q.popleft()
        ny = y+dy[1]*min_move_cnt
        board[ny][x], board[y][x] = board[y][x], board[ny][x]


r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

n = int(input())
seq = list(map(int, input().split()))
for k in range(n):
    if k % 2 == 0:
        search(r-seq[k], 0, 3)
    else:
        search(r-seq[k], c-1, 2)

    visited = [[0 for _ in range(c)] for _ in range(r)]
    count = 0
    poses_list = []
    for i in range(r-1, -1, -1):
        for j in range(c):
            if board[i][j] == 'x' and visited[i][j] == 0:
                count += 1
                poses = bfs(i, j, count)
                if i != r-1:
                    poses_list.append(poses)

    for poses in poses_list:
        gravity(poses)

for row in board:
    print(''.join(row))

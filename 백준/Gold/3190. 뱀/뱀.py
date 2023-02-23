import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
turn_L = {0: 2, 1: 3, 2: 1, 3: 0}
turn_D = {0: 3, 1: 2, 2: 0, 3: 1}

time = 0
n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
k = int(input())
for _ in range(k):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1

L = int(input())
info = {}
for _ in range(L):
    x, c = input().split()
    info[int(x)] = c

visited = [[False for _ in range(n)] for _ in range(n)]
snape = deque([(0, 0)])
visited[0][0] = True
direction = 3
while True:
    if time in info:
        if info[time] == 'L':
            direction = turn_L[direction]
        elif info[time] == 'D':
            direction = turn_D[direction]

    time += 1
    apple = False
    prev = (-1, -1)
    for _ in range(len(snape)):
        y, x = snape.popleft()
        visited[y][x] = False
        if prev == (-1, -1):
            ny, nx = y+dy[direction], x+dx[direction]
            if ny < 0 or ny >= n or nx < 0 or nx >= n or visited[ny][nx]:
                print(time)
                exit(0)
            if board[ny][nx]:
                apple = True
                board[ny][nx] = 0
            snape.append((ny, nx))
            visited[ny][nx] = True
        else:
            snape.append(prev)
            visited[prev[0]][prev[1]] = True
        prev = (y, x)

    if apple:
        visited[prev[0]][prev[1]] = True
        snape.append(prev)

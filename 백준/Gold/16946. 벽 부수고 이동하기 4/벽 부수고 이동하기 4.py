import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(n)]
colors = [[-1 for _ in range(m)] for _ in range(n)]
cnt = defaultdict(int)


def painting_board(y, x):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    q = deque([[y, x]])
    colors[y][x] = color
    cnt[color] += 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if board[ny][nx] == 0 and colors[ny][nx] == -1:
                q.append([ny, nx])
                colors[ny][nx] = color
                cnt[color] += 1


color = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and colors[i][j] == -1:
            painting_board(i, j)
            color += 1

for i in range(n):
    line = ''
    for j in range(m):
        if board[i][j] == 0:
            line += '0'
        else:
            area = 1
            checked_colors = set()
            if i-1 >= 0 and board[i-1][j] == 0:
                if colors[i-1][j] not in checked_colors:
                    checked_colors.add(colors[i-1][j])
                    area += cnt[colors[i-1][j]]
            if i+1 < n and board[i+1][j] == 0:
                if colors[i+1][j] not in checked_colors:
                    checked_colors.add(colors[i+1][j])
                    area += cnt[colors[i+1][j]]
            if j-1 >= 0 and board[i][j-1] == 0:
                if colors[i][j-1] not in checked_colors:
                    checked_colors.add(colors[i][j-1])
                    area += cnt[colors[i][j-1]]
            if j+1 < m and board[i][j+1] == 0:
                if colors[i][j+1] not in checked_colors:
                    checked_colors.add(colors[i][j+1])
                    area += cnt[colors[i][j+1]]
            line += str(area % 10)
    print(line)

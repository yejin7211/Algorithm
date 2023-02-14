import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[int(2e9) for _ in range(n+1)] for _ in range(n+1)]
paths = [[[] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    board[a][b] = board[b][a] = c
    paths[a][b] = [a, b]
    paths[b][a] = [b, a]
for i in range(1, n+1):
    board[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]
                paths[i][j] = paths[i][k][:-1] + paths[k][j]

answer = [['-' for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if len(paths[i][j]) >= 2:
            answer[i][j] = paths[i][j][1]

for row in answer[1:]:
    print(*row[1:])

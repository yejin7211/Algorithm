import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
board = [[int(2e9) for _ in range(n+1)] for _ in range(n+1)]
path = [[[] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    board[a][b] = min(board[a][b], c)
    path[a][b] = [a, b]

for i in range(1, n+1):
    board[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]
                path[i][j] = path[i][k][:-1] + path[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        print(board[i][j] if board[i][j] != int(2e9) else 0, end=' ')
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        print(len(path[i][j]), end=' ')
        print(*path[i][j])

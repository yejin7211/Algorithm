import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
paths = [[[] for _ in range(n+1)] for _ in range(n+1)]
board = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    paths[a][b] = [a, b]
    board[a][b] = min(board[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]
                paths[i][j] = paths[i][k][:-1] + paths[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        print(board[i][j] if board[i][j] != float('inf') else 0, end=' ')
    print()
for i in range(1, n+1):
    for j in range(1, n+1):
        print(len(paths[i][j]), end=' ')
        print(*paths[i][j])
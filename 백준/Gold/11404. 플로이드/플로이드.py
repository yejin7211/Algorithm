import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
m = int(input())
board = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    board[a][b] = min(board[a][b], c)
for i in range(1, n+1):
    board[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            board[i][j] = min(board[i][j], board[i][k]+board[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(board[i][j] if board[i][j] != float('inf') else 0, end=' ')
    print()
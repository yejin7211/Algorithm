import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
t = [0] + list(map(int, input().split()))
board = [[int(1e9) for _ in range(n+1)] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    board[a][b] = board[b][a] = l
for i in range(n):
    board[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            board[i][j] = min(board[i][j], board[i][k]+board[k][j])

answer = 0
for i in range(1, n+1):
    items = sum(t[j] for j in range(1, n+1) if board[i][j] <= m)
    answer = max(answer, items)
print(answer)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(y, x):
    if dp[y][x]:
        return dp[y][x]

    dp[y][x] = 1
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue
        if board[ny][nx] > board[y][x]:
            dp[y][x] = max(dp[y][x], dfs(ny, nx)+1)
    return dp[y][x]


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = -1
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))
print(answer)
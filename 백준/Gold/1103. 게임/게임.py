import sys
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def dfs(y, x, cnt):
    global answer
    answer = max(answer, cnt)
    visited[y][x] = True
    dp[y][x] = cnt

    X = int(board[y][x])
    for i in range(4):
        ny, nx = y+dy[i]*X, x+dx[i]*X
        if 0 <= ny < n and 0 <= nx < m:
            if visited[ny][nx]:
                print(-1)
                exit(0)
            if board[ny][nx] != 'H' and dp[ny][nx] < cnt+1:
                dfs(ny, nx, cnt+1)
    visited[y][x] = False


answer = 0
n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]

dfs(0, 0, 1)

print(answer)

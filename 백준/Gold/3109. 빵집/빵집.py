import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
dy = [-1, 0, 1]
dx = [1, 1, 1]


def dfs(y, x, cnt):
    board[y][x] = cnt
    if x == c-1:
        return True
    for i in range(3):
        ny, nx = y+dy[i], x+dx[i]
        if ny < 0 or ny >= r or nx < 0 or nx >= c:
            continue
        if board[ny][nx] == '.':
            if dfs(ny, nx, cnt):
                return True
    return False


cnt = 0
for i in range(r):
    if dfs(i, 0, cnt):
        cnt += 1
print(cnt)

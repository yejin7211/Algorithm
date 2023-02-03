import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = 0
r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
alpha = [False for _ in range(26)]
alpha[ord(board[0][0])-65] = True
cnt = 1


def dfs(y, x):
    global cnt, answer
    answer = max(answer, cnt)
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny < 0 or ny >= r or nx < 0 or nx >= c:
            continue
        if not alpha[ord(board[ny][nx])-65]:
            alpha[ord(board[ny][nx])-65] = True
            cnt += 1
            dfs(ny, nx)
            alpha[ord(board[ny][nx])-65] = False
            cnt -= 1


dfs(0, 0)

print(answer)

import sys
from collections import deque
input = sys.stdin.readline

n, m, p = map(int, input().split())
s = [0] + list(map(int, input().split()))
board = [list(input().rstrip()) for _ in range(n)]
pos = [[] for _ in range(p+1)]
for i in range(n):
    for j in range(m):
        if board[i][j].isdigit():
            pos[int(board[i][j])].append((i, j))
            board[i][j] = int(board[i][j])


def bfs(num):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    q = deque(pos[num])
    pos[num] = list()
    for _ in range(s[num]):
        size = len(q)
        if size == 0:
            break
        for _ in range(size):
            y, x = q.popleft()
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue
                if board[ny][nx] == '.':
                    board[ny][nx] = num
                    pos[num].append([ny, nx])
                    q.append((ny, nx))


turn = 1
while True:
    bfs(turn)
    turn += 1
    if turn > p:
        turn = 1
        check = False
        for i in range(1, p+1):
            if pos[i] != list():
                check = True
        if not check:
            break

cnt = [0 for _ in range(p+1)]
for i in range(n):
    for j in range(m):
        if type(board[i][j]) == int:
            cnt[board[i][j]] += 1
print(*cnt[1:])

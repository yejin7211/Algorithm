import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = int(1e9)
n, m, k = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    row = input().rstrip()
    for j in range(m):
        board[i][j] = int(row[j])

visited = [[[False for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
q = deque([[1, k, 0, 0]])
visited[0][0][k] = True
while q:
    dist, k, y, x = q.popleft()
    if y == n-1 and x == m-1:
        answer = min(answer, dist)
        continue
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue
        if board[ny][nx] == 1 and k > 0 and not visited[ny][nx][k-1]:
            visited[ny][nx][k-1] = True
            q.append([dist+1, k-1, ny, nx])
        if board[ny][nx] == 0 and not visited[ny][nx][k]:
            visited[ny][nx][k] = True
            q.append([dist+1, k, ny, nx])

if answer == int(1e9):
    print(-1)
else:
    print(answer)

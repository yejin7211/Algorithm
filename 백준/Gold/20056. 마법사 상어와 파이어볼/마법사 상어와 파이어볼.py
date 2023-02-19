import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
q = deque([list(map(int, input().split())) for _ in range(m)])

for _ in range(k):
    board = [[[] for _ in range(n)] for _ in range(n)]
    while q:
        r, c, m, s, d = q.popleft()
        ny, nx = r-1, c-1
        for _ in range(s):
            ny, nx = ny+dy[d], nx+dx[d]
            if ny < 0:
                ny = n-1
            if ny == n:
                ny = 0
            if nx < 0:
                nx = n-1
            if nx == n:
                nx = 0
        board[ny][nx].append([m, s, d])

    for i in range(n):
        for j in range(n):
            if len(board[i][j]) == 1:
                m, s, d = board[i][j][0]
                q.append([i+1, j+1, m, s, d])
            elif len(board[i][j]) > 1:
                total_m, total_s = 0, 0
                odd_even = [0, 0]
                for m, s, d in board[i][j]:
                    total_m += m
                    total_s += s
                    odd_even[d % 2] += 1
                directions = [1, 3, 5, 7]
                if odd_even[0] == 0 or odd_even[1] == 0:
                    directions = [0, 2, 4, 6]
                if total_m // 5 != 0:
                    for k in range(4):
                        q.append([i+1, j+1, total_m//5, total_s//len(board[i][j]), directions[k]])

answer = 0
while q:
    y, x, m, s, d = q.popleft()
    answer += m
print(answer)

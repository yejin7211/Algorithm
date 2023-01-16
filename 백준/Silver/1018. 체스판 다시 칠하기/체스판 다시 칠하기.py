import sys
input = sys.stdin.readline

m, n = map(int, input().split())
board = [['' for _ in range(n)] for _ in range(m)]
for i in range(m):
    s = input().strip()
    for j in range(n):
        board[i][j] = s[j]

next_color = {'W': 'B', 'B': 'W'}


def make_chess(y, x, color):
    painting = 0
    for ny in range(y, y+8):
        for nx in range(x, x+8):
            if board[ny][nx] != color:
                painting += 1
            color = next_color[color]
        color = next_color[color]
    return painting


answer = float('inf')
for i in range(m):
    for j in range(n):
        if i+8 <= m and j+8 <= n:
            cnt = min(make_chess(i, j, 'B'), make_chess(i, j, 'W'))
            answer = min(answer, cnt)
print(answer)

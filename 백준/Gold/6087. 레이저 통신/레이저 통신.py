import sys
from heapq import heappush, heappop
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def search():
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'C':
                return i, j


w, h = map(int, input().split())
board = [list(input().rstrip()) for _ in range(h)]
count = [[int(2e9) for _ in range(w)] for _ in range(h)]

start_y, start_x = search()
heap = [[0, start_y, start_x, -1]]
count[start_y][start_x] = 0
while heap:
    cnt, y, x, direction = heappop(heap)
    if board[y][x] == 'C' and cnt != 0:
        print(cnt)
        break
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny < 0 or ny >= h or nx < 0 or nx >= w:
            continue
        if board[ny][nx] != '*':
            if (direction == -1 or direction == i) and count[y][x] <= count[ny][nx]:
                count[ny][nx] = count[y][x]
                heappush(heap, [cnt, ny, nx, i])
            elif count[y][x] + 1 <= count[ny][nx]:
                count[ny][nx] = count[y][x]
                heappush(heap, [cnt+1, ny, nx, i])

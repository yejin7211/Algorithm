import sys
from heapq import heappush, heappop
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

count = 0
while True:
    n = int(input())
    if n == 0:
        break

    count += 1
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    heap = [[board[0][0], 0, 0]]
    visited[0][0] = True
    while heap:
        lost_rupy, y, x = heappop(heap)
        if y == n-1 and x == n-1:
            print('Problem ' + str(count) + ': ' + str(lost_rupy))
            break
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if not visited[ny][nx]:
                heappush(heap, [lost_rupy+board[ny][nx], ny, nx])
                visited[ny][nx] = True

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]

dp[0][0] = 1
heap = [[-board[0][0], 0, 0]]
while heap:
    priority, y, x = heappop(heap)
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue
        if board[ny][nx] < board[y][x]:
            if dp[ny][nx] == 0:
                heappush(heap, [-board[ny][nx], ny, nx])
            dp[ny][nx] += dp[y][x]

print(dp[n-1][m-1])

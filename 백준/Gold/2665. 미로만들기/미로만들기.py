import sys
from heapq import heappush, heappop
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

heap = [[0, 0, 0]]
visited[0][0] = True
while heap:
    cnt, y, x = heappop(heap)
    if y == n-1 and x == n-1:
        print(cnt)
        break
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue
        if not visited[ny][nx]:
            visited[ny][nx] = True
            if board[ny][nx] == 1:
                heappush(heap, [cnt, ny, nx])
            else:
                heappush(heap, [cnt+1, ny, nx])

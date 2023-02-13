import sys
from copy import deepcopy
input = sys.stdin.readline

move = [
    [],
    [[(-1, 0)], [(1, 0)], [(0, -1)], [(0, 1)]],
    [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]],
    [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
    [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, -1), (1, 0), (0, 1)], [(-1, 0), (0, -1), (1, 0)]],
    [[(-1, 0), (1, 0), (0, -1), (0, 1)]]
]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

answer = n*m
cctv = []
for i in range(n):
    for j in range(m):
        if 1 <= board[i][j] <= 5:
            cctv.append((board[i][j], i, j))
        if board[i][j] == 6:
            answer -= 1


def dfs(depth, arr):
    global answer, cctv
    if depth == len(cctv):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    cnt += 1
        answer = min(answer, cnt)
        return

    num, y, x = cctv[depth]
    for idx in range(len(move[num])):
        tmp = [deepcopy(row) for row in arr]
        for k in range(len(move[num][idx])):
            ny, nx = y, x
            while 0 <= ny + move[num][idx][k][0] < n and 0 <= nx + move[num][idx][k][1] < m:
                ny, nx = ny + move[num][idx][k][0], nx + move[num][idx][k][1]
                if tmp[ny][nx] != '#' and tmp[ny][nx] == 6:
                    break
                tmp[ny][nx] = '#'
        dfs(depth+1, tmp)


dfs(0, board)
print(answer)

import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = 0
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

'''
4
2 4 16 8
8 4 0 0
16 8 2 0
2 8 2 0
'''


def move(k, arr):
    res = [r[:] for r in arr]
    added_blocks = set()

    if k == 0:
        for i in range(1, n):
            for j in range(n):
                if res[i][j] != 0:
                    ny, x = i, j
                    while ny + dy[k] >= 0:
                        ny += dy[k]
                        if res[ny][x] == 0:
                            res[ny][x] = res[ny-dy[k]][x]
                            res[ny-dy[k]][x] = 0
                        elif (ny, x) not in added_blocks and res[ny][x] == res[ny-dy[k]][x]:
                            added_blocks.add((ny, x))
                            res[ny][x] *= 2
                            res[ny-dy[k]][x] = 0
                            break
                        else:
                            break
    elif k == 1:
        for i in range(n-2, -1, -1):
            for j in range(n):
                if res[i][j] != 0:
                    ny, x = i, j
                    while ny + dy[k] < n:
                        ny += dy[k]
                        if res[ny][x] == 0:
                            res[ny][x] = res[ny-dy[k]][x]
                            res[ny-dy[k]][x] = 0
                        elif (ny, x) not in added_blocks and res[ny][x] == res[ny-dy[k]][x]:
                            added_blocks.add((ny, x))
                            res[ny][x] *= 2
                            res[ny-dy[k]][x] = 0
                            break
                        else:
                            break
    elif k == 2:
        for j in range(1, n):
            for i in range(n):
                if res[i][j] != 0:
                    y, nx = i, j
                    while nx + dx[k] >= 0:
                        nx += dx[k]
                        if res[y][nx] == 0:
                            res[y][nx] = res[y][nx-dx[k]]
                            res[y][nx-dx[k]] = 0
                        elif (y, nx) not in added_blocks and res[y][nx] == res[y][nx-dx[k]]:
                            added_blocks.add((y, nx))
                            res[y][nx] *= 2
                            res[y][nx-dx[k]] = 0
                            break
                        else:
                            break
    elif k == 3:
        for j in range(n-2, -1, -1):
            for i in range(n):
                if res[i][j] != 0:
                    y, nx = i, j
                    while nx + dx[k] < n:
                        nx += dx[k]
                        if res[y][nx] == 0:
                            res[y][nx] = res[y][nx-dx[k]]
                            res[y][nx-dx[k]] = 0
                        elif (y, nx) not in added_blocks and res[y][nx] == res[y][nx-dx[k]]:
                            added_blocks.add((y, nx))
                            res[y][nx] *= 2
                            res[y][nx-dx[k]] = 0
                            break
                        else:
                            break

    return res


def dfs(cnt, board, order):
    global answer
    if cnt == 5:
        block = max(max(row) for row in board)
        answer = max(answer, block)
    else:
        for i in range(4):
            new_board = move(i, board)
            dfs(cnt+1, new_board, order+[i])


dfs(0, board, [])
print(answer)

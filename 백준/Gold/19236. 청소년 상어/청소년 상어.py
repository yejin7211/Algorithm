import sys
from copy import deepcopy
input = sys.stdin.readline

dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]

answer = 0
fish_info = dict()
board = [[0 for _ in range(4)] for _ in range(4)]
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(0, 8, 2):
        board[i][j//2] = line[j]
        fish_info[line[j]] = [i, j//2, line[j+1]]

num = board[0][0]
shark_info = fish_info[num]
del fish_info[num]
board[0][0] = 0


def dfs(board, fish_info, shark_info, result):
    global answer
    shark_y, shark_x, shark_d = shark_info
    for i in range(1, 17):
        if i in fish_info:
            y, x, d = fish_info[i]
            for _ in range(8):
                ny, nx = y+dy[d], x+dx[d]
                if 0 <= ny < 4 and 0 <= nx < 4:
                    if [ny, nx] != [shark_y, shark_x]:
                        if board[ny][nx] != 0:
                            ny, nx, your_d = fish_info[board[ny][nx]]
                            fish_info[board[ny][nx]] = [y, x, your_d]
                        fish_info[i] = [ny, nx, d]
                        board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
                        break
                d += 1
                if d == 9:
                    d = 1

    for _ in range(3):
        arr = [deepcopy(row) for row in board]
        fish_info2 = deepcopy(fish_info)
        shark_y, shark_x = shark_y+dy[shark_d], shark_x+dx[shark_d]
        if shark_y < 0 or shark_y >= 4 or shark_x < 0 or shark_x >= 4:
            answer = max(answer, result)
            break
        num = board[shark_y][shark_x]
        if num != 0:
            shark_info2 = fish_info2[num]
            del fish_info2[num]
            arr[shark_y][shark_x] = 0
            dfs(arr, fish_info2, shark_info2, result+num)


dfs(board, fish_info, shark_info, num)

print(answer)

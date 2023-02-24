import sys
from copy import deepcopy
input = sys.stdin.readline

dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]
change_dice = {1: [0, 3, 2, 6, 1, 5, 4], 2: [0, 4, 2, 1, 6, 5, 3],
               3: [0, 5, 1, 3, 4, 6, 2], 4: [0, 2, 6, 3, 4, 1, 5]}

n, m, y, x, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))
dice = [0 for _ in range(7)]

for d in orders:
    y, x = y + dy[d], x + dx[d]
    if y < 0 or y >= n or x < 0 or x >= m:
        y, x = y - dy[d], x - dx[d]
        continue
    lst = change_dice[d]
    new_dice = [0 for _ in range(7)]
    for i in range(1, 7):
        new_dice[lst[i]] = dice[i]
    dice = deepcopy(new_dice)
    if board[y][x] == 0:
        board[y][x] = dice[6]
    else:
        dice[6] = board[y][x]
        board[y][x] = 0
    print(dice[1])


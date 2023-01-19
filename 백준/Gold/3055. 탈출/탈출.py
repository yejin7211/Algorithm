import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
animal, water = deque(), deque()
board = [['' for _ in range(c)] for _ in range(r)]
for i in range(r):
    s = input()
    for j in range(c):
        board[i][j] = s[j]
        if s[j] == 'S':
            animal.append((i, j))
        if s[j] == '*':
            water.append((i, j))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

check = False
Time = 0
while True:
    animal_cnt = len(animal)
    for _ in range(animal_cnt):
        y, x = animal.popleft()
        if board[y][x] == '*':
            continue
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if board[ny][nx] == 'D':
                check = True
                break
            if board[ny][nx] == '.':
                animal.append((ny, nx))
                board[ny][nx] = 'S'
    Time += 1
    if check or not animal:
        break

    water_cnt = len(water)
    for _ in range(water_cnt):
        y, x = water.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if board[ny][nx] in ['.', 'S']:
                water.append((ny, nx))
                board[ny][nx] = '*'

print(Time if check else "KAKTUS")

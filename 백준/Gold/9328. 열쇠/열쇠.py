import sys
from collections import deque, defaultdict
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    answer = 0
    h, w = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(h)]
    keys = set(input().rstrip())
    unopened_doors = defaultdict(list)
    q = deque()
    if '0' in keys:
        keys.remove('0')


    def move(y, x):
        global board, answer, q, unopened_doors
        if board[y][x] != '*':
            if 'a' <= board[y][x] <= 'z':
                keys.add(board[y][x])
            if board[y][x] == '$':
                answer += 1

            if 'A' <= board[y][x] <= 'Z':
                if chr(ord(board[y][x])+32) in keys:
                    board[y][x] = '*'
                    q.append((y, x))
                else:
                    unopened_doors[board[y][x]].append((y, x))
            else:
                board[y][x] = '*'
                q.append((y, x))


    for i in range(h):
        move(i, 0)
        move(i, w-1)
    for j in range(w):
        move(0, j)
        move(h-1, j)

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            move(ny, nx)
            for k in keys:
                door = chr(ord(k)-32)
                while door in unopened_doors and len(unopened_doors[door]) != 0:
                    for ypos, xpos in unopened_doors[door]:
                        q.append((ypos, xpos))
                        board[ypos][xpos] = '*'
                        unopened_doors[door].remove((ypos, xpos))
                        break

    print(answer)

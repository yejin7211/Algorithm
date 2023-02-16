import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

dy = [0, -1, 0]
dx = [-1, 0, 1]

answer = 0
n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
enemy_cnt = sum(row.count(1) for row in board)
if enemy_cnt == 0:
    print(0)
    exit(0)
pos = []


def dead_enemy(r, c, arr):
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([0, r, c])
    while q:
        cnt, y, x = q.popleft()
        if cnt == d:
            break
        for i in range(3):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m or ny == r:
                continue
            if arr[ny][nx] == 1:
                return ny, nx
            else:
                visited[ny][nx] = True
                q.append((cnt+1, ny, nx))
    return -1, -1


def simulation():
    arr = [deepcopy(row) for row in board]
    total_enemy_cnt = enemy_cnt
    removed_enemy_cnt = 0
    rIdx = n
    while rIdx > 0:
        died_enemy = set()
        for x in pos:
            y, x = dead_enemy(rIdx, x, arr)
            if y != -1 and x != -1:
                died_enemy.add((y, x))
        total_enemy_cnt -= len(died_enemy)
        removed_enemy_cnt += len(died_enemy)
        for y, x in died_enemy:
            arr[y][x] = 0
        rIdx -= 1
    return removed_enemy_cnt


def dfs(idx):
    global answer
    if len(pos) == 3:
        cnt = simulation()
        answer = max(answer, cnt)
        return
    for i in range(idx, m):
        pos.append(i)
        dfs(i+1)
        pos.pop()


dfs(0)
print(answer)

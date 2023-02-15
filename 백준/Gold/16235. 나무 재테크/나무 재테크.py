import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

answer = 0
n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

land = [[5 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    for i in range(n):
        for j in range(n):
            died_amount = 0
            new_trees = deque()
            for z in trees[i][j]:
                if land[i][j] >= z:
                    land[i][j] -= z
                    new_trees.append(z+1)
                else:
                    died_amount += z//2
            trees[i][j] = new_trees
            land[i][j] += died_amount

    tmp = []
    for i in range(n):
        for j in range(n):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    for d in range(8):
                        ny, nx = i+dy[d], j+dx[d]
                        if 0 <= ny < n and 0 <= nx < n:
                            tmp.append((ny, nx))
            land[i][j] += A[i][j]

    for y, x in tmp:
        trees[y][x].appendleft(1)

cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(trees[i][j])
print(cnt)

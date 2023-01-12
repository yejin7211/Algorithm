import sys
from itertools import permutations
from math import sqrt
input = sys.stdin.readline

pos = []
for _ in range(4):
    x, y = map(int, input().split())
    pos.append([x, y])

minCnt = float('inf')
for path in permutations([i for i in range(1, 4)], 3):
    cnt = 0
    curX, curY = pos[0][0], pos[0][1]
    for k in path:
        a, b = pos[k][0], curX
        c, d = pos[k][1], curY
        cnt += sqrt((a-b)**2 + (c-d)**2)
        curX, curY = pos[k][0], pos[k][1]
    minCnt = min(minCnt, cnt)

print(int(minCnt))
import sys
input = sys.stdin.readline

n = int(input())
pos = [list(map(int, input().split())) for _ in range(n)]
pos.append(pos[0])

x, y = 0, 0
for i in range(n):
    x += pos[i][0] * pos[i+1][1]
    y += pos[i][1] * pos[i+1][0]

print(round(abs((x-y)/2), 1))

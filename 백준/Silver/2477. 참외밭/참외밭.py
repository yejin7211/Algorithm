import sys
input = sys.stdin.readline

k = int(input())
info = [list(map(int, input().split())) for _ in range(6)]

info2 = sorted(info, key=lambda x: -x[1])
y, x = [], []
for direction, length in info2:
    if x == list() and (direction == 1 or direction == 2):
        x = [direction, length]
    if y == list() and (direction == 3 or direction == 4):
        y = [direction, length]

answer = x[1] * y[1]
orders = {(2, 4): (1, 3), (1, 4): (3, 2), (1, 3): (2, 4), (2, 3): (4, 1)}
order = orders[(x[0], y[0])]
info *= 2
for i in range(len(info)):
    if i+1 < len(info) and (info[i][0], info[i+1][0]) == order:
        answer -= info[i][1] * info[i+1][1]
        break
print(answer * k)

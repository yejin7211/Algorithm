import sys
input = sys.stdin.readline

answer = 0
n = int(input())
line = sorted([sorted(list(map(int, input().split()))) for _ in range(n)])

left, right = line[0][0], line[0][1]
for x, y in line[1:]:
    if right < x:
        answer += right - left
        left, right = x, y
    if right < y:
        right = y

print(answer + right - left)

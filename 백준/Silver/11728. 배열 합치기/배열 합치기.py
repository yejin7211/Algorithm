import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

answer = []
pointer_a, pointer_b = 0, 0
while pointer_a < n and pointer_b < m:
    if a[pointer_a] < b[pointer_b]:
        answer.append(a[pointer_a])
        pointer_a += 1
    else:
        answer.append(b[pointer_b])
        pointer_b += 1

while pointer_a < n:
    answer.append(a[pointer_a])
    pointer_a += 1
while pointer_b < m:
    answer.append(b[pointer_b])
    pointer_b += 1

print(*answer)

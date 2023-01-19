import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
answer = 0

remain = {i: 0 for i in range(m)}
for i in range(n):
    if i > 0:
        a[i] += a[i-1]
    if a[i] % m == 0:
        answer += 1
    remain[a[i] % m] += 1

for v in remain.values():
    if v >= 2:
        answer += v * (v-1) // 2
print(answer)

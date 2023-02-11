import sys
input = sys.stdin.readline

answer = 0
n = int(input())
if n == 1:
    print(1)
    exit(0)

left, right = 1, 2
total = 3
while left <= right and right <= n:
    if total == n:
        answer += 1
        total -= left
        left += 1
    elif total < n:
        right += 1
        total += right
    elif total > n:
        total -= left
        left += 1

print(answer)

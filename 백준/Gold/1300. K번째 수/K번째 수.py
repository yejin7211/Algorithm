import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

left, right = 1, n*n
while left <= right:
    mid = (left + right) // 2
    cnt = sum(min(mid//i, n) for i in range(1, n+1))
    if cnt >= k:
        right = mid - 1
    else:
        left = mid + 1

print(left)

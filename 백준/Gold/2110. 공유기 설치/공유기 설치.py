import sys
input = sys.stdin.readline

n, c = map(int, input().split())
x = sorted([int(input()) for _ in range(n)])

left, right = 1, max(x)
while left <= right:
    mid = (left + right) // 2
    cnt, cur = 1, x[0]
    for pos in x[1:]:
        if pos - cur >= mid:
            cnt += 1
            cur = pos

    if cnt >= c:
        left = mid + 1
    else:
        right = mid - 1

print(right)

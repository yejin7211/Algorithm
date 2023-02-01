import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heights = list(map(int, input().split()))

left, right = 1, max(heights)
while left <= right:
    mid = (left + right) // 2
    length = sum(h-mid for h in heights if h >= mid)
    if length >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)

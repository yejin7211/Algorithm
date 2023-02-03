import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = [0] + list(map(int, input().split()))
for i in range(1, n+1):
    arr[i] += arr[i-1]

answer = n+1
left, right = 0, 1
while left <= right and right <= n:
    if arr[right] - arr[left] < s:
        right += 1
    else:
        answer = min(answer, right - left)
        left += 1

print(answer if answer != n+1 else 0)

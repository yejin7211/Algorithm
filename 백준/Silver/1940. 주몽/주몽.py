import sys
input = sys.stdin.readline

answer = 0
n = int(input())
m = int(input())
nums = sorted(list(map(int, input().split())))

left, right = 0, n-1
while left < right:
    total = nums[left] + nums[right]
    if total <= m:
        if total == m:
            answer += 1
        left += 1
    else:
        right -= 1

print(answer)

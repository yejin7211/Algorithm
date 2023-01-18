import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

minGap = float('inf')
answer = [-1, -1]
left, right = 0, n-1
while left < right:
    total = nums[left] + nums[right]
    if abs(total) < minGap:
        minGap = abs(total)
        answer = [nums[left], nums[right]]
    if total < 0:
        left += 1
    else:
        right -= 1
        
print(*sorted(answer))

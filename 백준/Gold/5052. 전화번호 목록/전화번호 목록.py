import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = sorted(list(input().strip() for _ in range(n)))

    answer = 'YES'
    for i in range(n-1):
        numLen = len(nums[i])
        if nums[i] == nums[i+1][:numLen]:
            answer = 'NO'
    print(answer)

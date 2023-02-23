import sys
input = sys.stdin.readline

answer = 0
n = int(input())
a = list(map(int, input().split()))

# increasing sequence
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j]+1)

# decreasing sequence
dp2 = [1 for _ in range(n)]
for i in range(n-1, -1, -1):
    for j in range(i, n):
        if a[j] < a[i]:
            dp2[i] = max(dp2[i], dp2[j]+1)

for i in range(n):
    answer = max(answer, dp[i]+dp2[i]-1)
print(answer)

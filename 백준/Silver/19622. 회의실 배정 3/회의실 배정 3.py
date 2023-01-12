import sys
input = sys.stdin.readline

n = int(input())
dp = [[0, 0] for _ in range(n)]
for i in range(n):
    s, e, p = input().split()
    dp[i][1] = int(p)

if n != 1:
    dp[1][0] = dp[0][1]
    for i in range(2, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        dp[i][1] = max(dp[i-1][0], dp[i-2][1]) + dp[i][1]
print(max(dp[n-1][0], dp[n-1][1]))
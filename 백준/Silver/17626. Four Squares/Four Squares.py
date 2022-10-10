import math

n = int(input())
dp = [i for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, int(math.sqrt(i))+1):
        dp[i] = min(dp[i-pow(j, 2)] + 1, dp[i])

print(dp[n])

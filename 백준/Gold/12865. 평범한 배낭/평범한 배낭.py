import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for w in range(1, k+1):
        if items[i][0] <= w:
            dp[i][w] = max(items[i][1]+dp[i-1][w-items[i][0]], dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]

print(dp[n][k])

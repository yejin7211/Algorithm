import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i] = 1
    if i != 1 and arr[i-1] == arr[i]:
        dp[i-1][i] = 1

for i in range(2, n):
    j = 1
    while i + j <= n:
        if arr[j] == arr[i+j] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1
        j += 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])

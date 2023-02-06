import sys
input = sys.stdin.readline

N, M = map(int, input().split())
m = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(sum(c)+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for cur in range(sum(c)+1):
        if c[i] > cur:
            dp[i][cur] = dp[i-1][cur]
        else:
            dp[i][cur] = max(dp[i-1][cur], dp[i-1][cur-c[i]]+m[i])

for j in range(sum(c)+1):
    if dp[N][j] >= M:
        print(j)
        break

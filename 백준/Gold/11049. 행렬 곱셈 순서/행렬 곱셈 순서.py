import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[int(2e9) for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 0

for gap in range(n):
    for s in range(n):
        e = s + gap
        if e >= n:
            break
        for m in range(s, e):
            res = dp[s][m] + dp[m+1][e] + (matrix[s][0] * matrix[m][1] * matrix[e][1])
            dp[s][e] = min(dp[s][e], res)

print(dp[0][-1])

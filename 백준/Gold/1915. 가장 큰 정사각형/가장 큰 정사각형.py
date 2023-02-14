import sys
input = sys.stdin.readline

answer = 0
n, m = map(int, input().split())
board = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(n):
    row = input().rstrip()
    for j in range(m):
        board[i+1][j+1] = int(row[j])

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if board[i][j] == 1:
            dp[i][j] = 1
            if dp[i-1][j] >= 1 and dp[i][j-1] >= 1:
                if dp[i-1][j] == dp[i][j-1]:
                    dp[i][j] += dp[i-1][j] - 1
                    k = dp[i-1][j]
                    if i-k >= 0 and j-k >= 0 and board[i-k][j-k] == 1:
                        dp[i][j] += 1
                else:
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1])

for i in range(1, n+1):
    for j in range(1, m+1):
        answer = max(answer, dp[i][j]**2)
print(answer)

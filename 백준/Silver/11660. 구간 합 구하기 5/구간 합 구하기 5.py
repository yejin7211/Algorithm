import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(1, n):
        dp[i][j] += dp[i][j-1]
for j in range(n):
    for i in range(1, n):
        dp[i][j] += dp[i-1][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1 = x1-1, y1-1
    x2, y2 = x2-1, y2-1
    answer = dp[x2][y2]
    if y1-1 >= 0:
        answer -= dp[x2][y1-1]
    if x1-1 >= 0:
        answer -= dp[x1-1][y2]
    if x1-1 >= 0 and y1-1 >= 0:
        answer += dp[x1-1][y1-1]
    print(answer)
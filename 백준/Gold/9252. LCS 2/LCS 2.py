import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]

i, j = 1, 1
while i <= len(a) and j <= len(b):
    if a[i-1] == b[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
    else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    i += 1
    if i > len(a):
        j += 1
        i = 1

answer = []
i, j = len(a), len(b)
while dp[i][j]:
    if dp[i-1][j] == dp[i][j]:
        i -= 1
    elif dp[i][j-1] == dp[i][j]:
        j -= 1
    else:
        answer.append(a[i-1])
        i -= 1
        j -= 1

print(dp[len(a)][len(b)])
print(''.join(reversed(answer)))

import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
LCS = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]

i, j = 1, 1
while j <= len(a) and i <= len(b):
    if a[j-1] == b[i-1]:
        LCS[i][j] = LCS[i-1][j-1] + 1
    else:
        LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
    j += 1
    if j > len(a):
        i += 1
        j = 1

print(max(max(row) for row in LCS))

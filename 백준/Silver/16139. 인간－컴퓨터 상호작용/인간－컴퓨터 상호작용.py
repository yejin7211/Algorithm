import sys
input = sys.stdin.readline

s = input().rstrip()
alpha = [{chr(c): 0 for c in range(97, 123)} for _ in range(len(s))]
for i in range(len(s)):
    alpha[i][s[i]] += 1
for i in range(1, len(s)):
    for j in range(97, 123):
        alpha[i][chr(j)] += alpha[i-1][chr(j)]

q = int(input())
for _ in range(q):
    c, l, r = input().split()
    n = alpha[int(r)][c]
    m = 0
    if int(l)-1 >= 0:
        m = alpha[int(l)-1][c]
    print(n - m)

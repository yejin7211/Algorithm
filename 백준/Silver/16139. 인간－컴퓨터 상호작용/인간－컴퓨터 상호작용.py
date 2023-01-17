import sys
input = sys.stdin.readline

s = input().rstrip()
q = int(input())
for _ in range(q):
    c, l, r = input().split()
    print(s[int(l):int(r)+1].count(c))

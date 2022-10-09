import sys
input = sys.stdin.readline

n, m = map(int, input().split())
info = {}

for _ in range(n):
    site, pw = input().split()
    info[site] = pw

for _ in range(m):
    site = input().rstrip()
    print(info[site])
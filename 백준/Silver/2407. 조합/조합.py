import sys
input = sys.stdin.readline

n, m = map(int, input().split())

m = min(m, n - m)

a = 1
for _ in range(m):
     a *= n
     n -= 1

b = 1
while m >= 1:
     b *= m
     m -= 1

print(a // b)
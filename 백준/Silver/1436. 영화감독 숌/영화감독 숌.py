import sys
input = sys.stdin.readline

k = int(input())

n = 666
count = 1
while count < k:
    n += 1
    if '666' in str(n):
        count += 1
    n = int(n)

print(n)
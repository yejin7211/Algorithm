import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

info = Counter(A)
for k in B:
    if k in info and info[k] > 0:
        info[k] -= 1

print(sum(info.values()))
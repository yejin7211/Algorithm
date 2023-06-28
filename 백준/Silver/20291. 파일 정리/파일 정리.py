import sys
from collections import defaultdict
input = sys.stdin.readline


n = int(input())
dic = defaultdict(int)
for _ in range(n):
    file = str(input().rstrip())
    idx = file.find('.')
    dic[file[idx+1:]] += 1

items = sorted(list(dic.items()))
for a, b in items:
    print(a, b)
    
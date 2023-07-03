import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
dic = defaultdict(int)
for _ in range(n):
    word = str(input().rstrip())
    if len(word) >= m:
        dic[word] += 1

items = sorted(list(dic.items()), key=lambda x: (-x[1], -len(x[0]), x[0]))
for word, cnt in items:
    print(word)

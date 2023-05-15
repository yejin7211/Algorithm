import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
dic = defaultdict(int)
for _ in range(n):
    num = int(input())
    dic[num] += 1

result = sorted(list(dic.items()), key=lambda x: (-x[1], x[0]))
print(result[0][0])

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = list(map(int, input().split()))

dic = {}
for i in range(n):
    if arr[i] not in dic:
        dic[arr[i]] = [arr[i], i, 1]
    else:
        dic[arr[i]][2] += 1

info = sorted(list(dic.values()), key=lambda x: (-x[2], x[1]))
for num, idx, cnt in info:
    for _ in range(cnt):
        print(num, end=' ')

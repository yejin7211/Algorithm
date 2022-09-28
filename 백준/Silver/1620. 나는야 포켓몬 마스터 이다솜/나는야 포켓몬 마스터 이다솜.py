import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}

for i in range(1, n + 1):
    s = input().rstrip()
    dic[i] = s
    dic[s] = i

for i in range(m):
    s = input().rstrip()
    if s.isdigit():
        print(dic[int(s)])
    else:
        print(dic[s])


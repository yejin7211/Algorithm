import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = []


def sol():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    x = 1
    if s != []:
        x = s[-1]
    for i in range(x, n+1):
        s.append(i)
        sol()
        s.pop()


sol()
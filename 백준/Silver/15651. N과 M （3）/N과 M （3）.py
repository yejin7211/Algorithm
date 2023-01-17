import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = []


def sol(cnt):
    if cnt == 0:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        s.append(i)
        sol(cnt - 1)
        s.pop()


sol(m)
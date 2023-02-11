import sys
input = sys.stdin.readline


def dfs():
    if len(res) == m:
        print(*res)
        return

    for i in range(n):
        res.append(arr[i])
        dfs()
        res.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = []

dfs()
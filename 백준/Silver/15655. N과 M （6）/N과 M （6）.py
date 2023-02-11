import sys
input = sys.stdin.readline


def dfs(idx):
    if len(seq) == m:
        print(*seq)
        return

    for i in range(idx, n):
        seq.append(arr[i])
        dfs(i+1)
        seq.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
seq = []

dfs(0)

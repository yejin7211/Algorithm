import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False for _ in range(n)]
res = []


def dfs():
    if len(res) == m:
        print(*res)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            res.append(arr[i])
            dfs()
            res.pop()
            visited[i] = False


dfs()

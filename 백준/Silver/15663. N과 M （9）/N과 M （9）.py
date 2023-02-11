import sys
input = sys.stdin.readline


def dfs(cnt):
    global answer, res
    if cnt == m:
        res2 = res.rstrip()
        if res2 not in answer:
            answer.append(res2)
            print(res2)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            res += arr[i]
            dfs(cnt+1)
            res = res[:-len(arr[i])]
            visited[i] = False


answer = []
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
arr = [str(num)+' ' for num in arr]
visited = [False for _ in range(n)]
res = ''

dfs(0)

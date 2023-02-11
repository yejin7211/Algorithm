import sys
input = sys.stdin.readline


def dfs(cnt):
    global res
    if cnt == m:
        if res[:-1] not in answer:
            answer.add(res[:-1])
            print(res[:-1])
        return

    for i in range(n):
        tmp = res
        res += arr[i]
        dfs(cnt+1)
        res = tmp


answer = set()
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
arr = [str(num)+' ' for num in arr]
res = ''

dfs(0)

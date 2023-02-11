import sys
input = sys.stdin.readline


def dfs(idx, cnt):
    global res
    if cnt == m:
        res2 = res.strip()
        if res2 not in answer:
            print(res2)
            answer.append(res2)
        return

    for i in range(idx, n):
        res += arr[i]
        dfs(i, cnt+1)
        res = res[:-len(arr[i])]


answer = []
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
arr = [str(num)+' ' for num in arr]
res = ''

dfs(0, 0)

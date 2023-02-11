import sys
input = sys.stdin.readline


def calc():
    res = 0
    for i in range(n-1):
        res += abs(seq[i]-seq[i+1])
    return res


def dfs():
    global answer
    if len(seq) == n:
        answer = max(answer, calc())
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            seq.append(arr[i])
            dfs()
            seq.pop()
            visited[i] = False


answer = 0
n = int(input())
arr = sorted(list(map(int, input().split())))
visited = [False for _ in range(n)]
seq = []

dfs()

print(answer)

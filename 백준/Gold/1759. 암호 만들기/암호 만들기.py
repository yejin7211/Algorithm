import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alpha = sorted(list(input().split()))
answer = []


def dfs(idx):
    global answer
    if len(answer) == L:
        cnt = 0
        for c in ['a', 'e', 'i', 'o', 'u']:
            cnt += answer.count(c)
        if cnt >= 1 and L-cnt >= 2:
            print(''.join(answer))
        return
    for i in range(idx, C):
        answer.append(alpha[i])
        dfs(i + 1)
        answer.pop()


dfs(0)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

root = [i for i in range(n+1)]
arr = list(map(int, input().split()))
for i in range(1, arr[0]+1):
    root[arr[i]] = -1


def find(x):
    if root[x] != -1 and root[x] != x:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    if x == -1 and y == -1:
        return
    if x == -1:
        root[y] = -1
    elif y == -1:
        root[x] = -1
    else:
        root[max(x, y)] = min(x, y)


parties = [list(map(int, input().split())) for _ in range(m)]
for party in parties:
    for p in range(2, len(party)):
        union(find(party[1]), find(party[p]))

answer = 0
for party in parties:
    answer += 1
    for p in party[1:]:
        if find(p) == -1:
            answer -= 1
            break

print(answer)
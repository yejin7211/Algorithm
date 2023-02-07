import sys
input = sys.stdin.readline

answer = 0
n = int(input())
m = int(input())
cost = [list(map(int, input().split())) for _ in range(m)]
cost.sort(key=lambda x: x[2])
root = [i for i in range(n+1)]


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    root[max(x, y)] = min(x, y)


for a, b, c in cost:
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        union(a_root, b_root)
        answer += c

print(answer)

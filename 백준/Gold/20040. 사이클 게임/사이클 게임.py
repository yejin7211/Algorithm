import sys
input = sys.stdin.readline

answer = 0
n, m = map(int, input().split())
root = [i for i in range(n)]


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    if x < y:
        root[y] = x
    else:
        root[x] = y


for cnt in range(1, m+1):
    a, b = map(int, input().split())
    a_root = find(a)
    b_root = find(b)
    if a_root == b_root:
        answer = cnt
        break
    else:
        union(a_root, b_root)

print(answer)
import sys
input = sys.stdin.readline


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        root[y_root] = x_root
        count[x_root] += count[y_root]
        

t = int(input())
for _ in range(t):
    f = int(input())
    root, count = {}, {}
    for _ in range(f):
        id1, id2 = input().rstrip().split()
        if id1 not in root:
            root[id1] = id1
            count[id1] = 1
        if id2 not in root:
            root[id2] = id2
            count[id2] = 1

        union(id1, id2)
        print(count[find(id1)])

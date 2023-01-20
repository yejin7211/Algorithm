import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())
root = [i for i in range(n+1)]


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


for _ in range(m):
    c, a, b = map(int, input().split())
    a_root = find(a)
    b_root = find(b)
    if c == 0:
        if a_root != b_root:
            if a_root < b_root:
                root[b_root] = a_root
            else:
                root[a_root] = b_root
    else:
        print('YES' if a_root == b_root else 'NO')

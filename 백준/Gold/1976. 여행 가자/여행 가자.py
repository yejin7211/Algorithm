import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
connect = []
for s in range(n):
    info = list(map(int, input().split()))
    for e in range(n):
        if info[e] == 1:
            connect.append([s+1, e+1])
seq = list(map(int, input().split()))

root = [i for i in range(n+1)]


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


for s, e in connect:
    s_root = find(s)
    e_root = find(e)
    if s_root != e_root:
        if s_root < e_root:
            root[e_root] = s_root
        else:
            root[s_root] = e_root

possible = True
for i in range(1, m):
    if root[seq[i]] != root[seq[0]]:
        possible = False
        break
print('YES' if possible else 'NO')

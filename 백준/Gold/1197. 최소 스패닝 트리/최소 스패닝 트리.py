import sys
input = sys.stdin.readline

v, e = map(int, input().split())
connect = [list(map(int, input().split())) for _ in range(e)]
connect.sort(key=lambda x: x[2])
parent = [i for i in range(v+1)]


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


answer = 0
for a, b, c in connect:
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        if a_root > b_root:
            parent[a_root] = b_root
        else:
            parent[b_root] = a_root
        answer += c
print(answer)

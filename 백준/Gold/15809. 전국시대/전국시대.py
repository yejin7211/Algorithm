import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [0] + [int(input()) for _ in range(n)]
root = [i for i in range(n+1)]


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    root[max(x, y)] = min(x, y)
    a[min(x, y)] += a[max(x, y)]


def union2(x, y):
    root[y] = x
    a[x] -= a[y]


for _ in range(m):
    o, p, q = map(int, input().split())
    if o == 1:
        union(find(p), find(q))
    else:
        if a[find(p)] > a[find(q)]:
            union2(find(p), find(q))
        elif a[find(p)] < a[find(q)]:
            union2(find(q), find(p))
        else:
            root[find(p)] = root[find(q)] = 0

country = set()
for i in range(1, n+1):
    if find(i) != 0:
        country.add(find(i))

power = []
for i in country:
    power.append(a[i])

print(len(country))
print(*sorted(power))

import sys
input = sys.stdin.readline

answer = 0
n = int(input())
root = [i for i in range(n)]

planets = []
for i in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, i))

edges = []
for i in range(3):
    planets.sort(key=lambda x: x[i])
    for j in range(1, n):
        d = abs(planets[j-1][i] - planets[j][i])
        edges.append([d, planets[j-1][3], planets[j][3]])
edges.sort()


def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    root[max(x, y)] = min(x, y)


for w, s, e in edges:
    root_s = find(s)
    root_e = find(e)
    if root_s != root_e:
        union(root_s, root_e)
        answer += w

print(answer)

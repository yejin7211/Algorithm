import sys
input = sys.stdin.readline


def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    root[max(x, y)] = min(x, y)


n = int(input())
m = int(input())
root = [i for i in range(n+1)]
board = [[int(1e9) for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    board[a][b] = board[b][a] = 1
    union(find(a), find(b))
for i in range(1, n+1):
    board[i][i] = 0

parts = set()
for i in range(1, n+1):
    parts.add(find(i))
print(len(parts))

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            board[i][j] = min(board[i][j], board[i][k]+board[k][j])

dist = {}
for i in range(1, n+1):
    dist[i] = 0
    for j in range(1, n+1):
        if find(i) == find(j):
            dist[i] = max(dist[i], board[i][j])

leaders = []
for p in parts:
    hobo, minDist = p, dist[p]
    for i in range(1, n+1):
        if find(i) == p and dist[i] < minDist:
            hobo, minDist = i, dist[i]
    leaders.append(hobo)

for leader in sorted(leaders):
    print(leader)

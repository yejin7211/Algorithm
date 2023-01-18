import sys
input = sys.stdin.readline

v, e = map(int, input().split())
dist = [[float('inf') for _ in range(v+1)] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

answer = float('inf')
for i in range(1, v+1):
    answer = min(answer, dist[i][i])
print(answer if answer != float('inf') else -1)

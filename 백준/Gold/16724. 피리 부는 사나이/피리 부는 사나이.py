import sys
input = sys.stdin.readline

answer = 0
n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

dy = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
dx = {'U': 0, 'D': 0, 'L': -1, 'R': 1}


def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    root[max(x, y)] = min(x, y)


root = [i for i in range(n*m)]
for y in range(n):
    for x in range(m):
        k = board[y][x]
        ny, nx = y+dy[k], x+dx[k]
        if find(y*m+x) != find(ny*m+nx):
            union(find(y*m+x), find(ny*m+nx))

safe_root = set()
for i in range(n):
    for j in range(m):
        if find(i*m+j) not in safe_root:
            safe_root.add(find(i*m+j))
            answer += 1
print(answer)

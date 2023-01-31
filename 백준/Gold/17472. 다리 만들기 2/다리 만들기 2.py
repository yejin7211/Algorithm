import sys
from collections import deque
input = sys.stdin.readline

# 섬들을 색깔 별로 구분
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

color = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            color += 1
            q = deque([(i, j)])
            while q:
                y, x = q.popleft()
                board[y][x] = color
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if ny < 0 or ny >= n or nx < 0 or nx >= m:
                        continue
                    if board[ny][nx] == 1:
                        q.append((ny, nx))

# 가능한 다리 모두 찾기
bridges = []
for i in range(n):
    for j in range(m):
        if board[i][j] != 0:
            for k in range(4):
                ny, nx = i, j
                length, finish = 0, -1
                while True:
                    ny, nx = ny + dy[k], nx + dx[k]
                    if ny < 0 or ny >= n or nx < 0 or nx >= m or board[ny][nx] == board[i][j]:
                        break
                    if board[ny][nx] != 0 and board[ny][nx] != board[i][j]:
                        finish = board[ny][nx]
                        break
                    length += 1
                if finish != -1 and length != 1:
                    bridges.append([board[i][j], finish, length])


# 최소 스패닝 트리(MST) 알고리즘
# 크루스칼 알고리즘 + 유니온 파인드
def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    root[max(x, y)] = min(x, y)


if len(bridges) == 0:
    print(-1)
else:
    answer = 0
    root = [i for i in range(color+1)]
    bridges.sort(key=lambda x: x[2])
    for s, e, l in bridges:
        root_s = find(s)
        root_e = find(e)
        if root_s != root_e:
            union(root_s, root_e)
            answer += l

    finish_root = find(2)
    for i in range(3, color+1):
        root_i = find(i)
        if finish_root != root_i:
            answer = -1
            break
    print(answer)

import sys
input = sys.stdin.readline

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]

answer = 0
r, c, m = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(m)]

col = 0
while col < c:
    col += 1  # 1
    idx, idx_y = -1, r+1  # 2
    exist_check = [True for _ in range(len(sharks))]
    for i in range(len(sharks)):
        y, x = sharks[i][0], sharks[i][1]
        if x == col:
            if idx == -1 or y < idx_y:
                idx, idx_y = i, y
    if idx != -1:
        answer += sharks[idx][4]
        exist_check[idx] = False

    moved_results = [[-1 for _ in range(c+1)] for _ in range(r+1)]
    for i in range(len(sharks)):
        if not exist_check[i]:
            continue
        y, x, s, d, z = sharks[i]
        ny, nx = y, x
        while (d == 1 or d == 2) and s >= (r-1)*2:
            s -= (r-1)*2
        while (d == 3 or d == 4) and s >= (c-1)*2:
            s -= (c-1)*2
        for _ in range(s):
            if d == 1 and ny == 1:
                d = 2
            elif d == 2 and ny == r:
                d = 1
            elif d == 3 and nx == c:
                d = 4
            elif d == 4 and nx == 1:
                d = 3
            ny, nx = ny + dy[d], nx + dx[d]

        if moved_results[ny][nx] != -1:
            your_z = sharks[moved_results[ny][nx]][4]
            if z < your_z:
                exist_check[i] = False
            else:
                exist_check[moved_results[ny][nx]] = False
                moved_results[ny][nx] = i
                sharks[i] = [ny, nx, s, d, z]
        else:
            moved_results[ny][nx] = i
            sharks[i] = [ny, nx, s, d, z]

    idx = 0
    for i in range(len(sharks)):
        if exist_check[i]:
            sharks[idx] = sharks[i]
            idx += 1
    sharks = sharks[:idx]

print(answer)

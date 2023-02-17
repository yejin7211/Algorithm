import sys
input = sys.stdin.readline

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

time = 0
n, m, k = map(int, input().split())
board = [[[0, 0] for _ in range(n)] for _ in range(n)]

sharks = {}
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] != 0:
            board[i][j] = [row[j], k]
            sharks[row[j]] = [i, j]  # 번호, 냄새 남은 횟수, 현재 바라보는 방향

arr = list(map(int, input().split()))
for i in range(m):
    sharks[i+1].append(arr[i])

directions = {}
for num in range(1, m+1):
    for d in range(1, 5):
        directions[str(num)+'_'+str(d)] = list(map(int, input().split()))

while len(sharks) > 1:
    time += 1
    if time > 1000:
        print(-1)
        exit(0)

    for num in range(1, m+1):
        if num not in sharks:
            continue
        y, x, cur_d = sharks[num]
        seq = directions[str(num)+'_'+str(cur_d)]
        moved = False
        for d in seq:
            ny, nx = y+dy[d], x+dx[d]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if board[ny][nx][1] == 0:  # 아무 냄새가 없는 칸으로
                sharks[num] = [ny, nx, d]
                moved = True
                break
        if not moved:
            for d in seq:
                ny, nx = y + dy[d], x + dx[d]
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue
                if board[ny][nx][0] == num:  # 자신의 냄새가 있는 칸으로
                    sharks[num] = [ny, nx, d]
                    moved = True
                    break

    removed = set()
    for num1 in range(1, m+1):  # 겹치는 것이 있는지 확인
        for num2 in range(num1+1, m+1):
            if num1 in sharks and num2 in sharks:
                y1, x1, cur_d1 = sharks[num1]
                y2, x2, cur_d2 = sharks[num2]
                if [y1, x1] == [y2, x2] and num1 < num2:
                    removed.add(num2)

    for num in removed:
        del sharks[num]

    for num in range(1, m+1):
        if num in sharks:
            y, x, cur_d = sharks[num]
            board[y][x] = [num, k]

    for i in range(n):
        for j in range(n):
            if board[i][j][1] != 0:
                num = board[i][j][0]
                if num in sharks:
                    y, x, cur_d = sharks[num]
                    if [y, x] != [i, j]:
                        board[i][j][1] -= 1
                        if board[i][j][1] == 0:
                            board[i][j][0] = 0
                else:
                    board[i][j][1] -= 1
                    if board[i][j][1] == 0:
                        board[i][j][0] = 0

print(time)

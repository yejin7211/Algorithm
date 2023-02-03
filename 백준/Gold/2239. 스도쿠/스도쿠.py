import sys
input = sys.stdin.readline

board = [[0 for _ in range(9)] for _ in range(9)]
for i in range(9):
    row = input().rstrip()
    for j in range(9):
        board[i][j] = int(row[j])


def search_blank():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return -1, -1


def dfs(y, x):
    if y == -1 and x == -1:
        for row in board:
            print(''.join(map(str, row)))
        sys.exit()

    nums = {i for i in range(1, 10)}
    for i in range(9):
        if board[i][x] in nums:
            nums.remove(board[i][x])
    for j in range(9):
        if board[y][j] in nums:
            nums.remove(board[y][j])
    for i in range(y//3*3, y//3*3+3):
        for j in range(x//3*3, x//3*3+3):
            if board[i][j] in nums:
                nums.remove(board[i][j])

    for n in nums:
        board[y][x] = n
        new_y, new_x = search_blank()
        dfs(new_y, new_x)
        board[y][x] = 0


y, x = search_blank()
dfs(y, x)

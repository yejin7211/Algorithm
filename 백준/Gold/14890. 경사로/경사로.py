import sys
input = sys.stdin.readline

answer = 0
n, l = map(int, input().split())
board = [[0 for _ in range(n+1)]] + [[0] + list(map(int, input().split())) for _ in range(n)]

for j in range(1, n+1):  # 세로
    col_check = [False for _ in range(n+1)]
    possible = True
    for i in range(1, n):
        if abs(board[i+1][j] - board[i][j]) >= 2:
            possible = False
        if board[i+1][j] < board[i][j]:
            if i+l > n:
                possible = False
            else:
                for rIdx in range(i+1, i+1+l):
                    if board[rIdx][j] != board[i+1][j] or col_check[rIdx]:
                        possible = False
                if possible:
                    for rIdx in range(i+1, i+1+l):
                        col_check[rIdx] = True
        elif board[i+1][j] > board[i][j]:
            if i+1-l <= 0:
                possible = False
            else:
                for rIdx in range(i, i-l, -1):
                    if board[rIdx][j] != board[i][j] or col_check[rIdx]:
                        possible = False
                if possible:
                    for rIdx in range(i, i-l, -1):
                        col_check[rIdx] = True
        if not possible:
            break

    if possible:
        answer += 1

for i in range(1, n+1):  # 가로
    row_check = [False for _ in range(n+1)]
    possible = True
    for j in range(1, n):
        if abs(board[i][j+1] - board[i][j]) >= 2:
            possible = False
        if board[i][j+1] < board[i][j]:
            if j+l > n:
                possible = False
            else:
                for cIdx in range(j+1, j+1+l):
                    if board[i][cIdx] != board[i][j+1] or row_check[cIdx]:
                        possible = False
                if possible:
                    for cIdx in range(j+1, j+1+l):
                        row_check[cIdx] = True
        elif board[i][j+1] > board[i][j]:
            if j+1-l <= 0:
                possible = False
            else:
                for cIdx in range(j, j-l, -1):
                    if board[i][cIdx] != board[i][j] or row_check[cIdx]:
                        possible = False
                if possible:
                    for cIdx in range(j, j-l, -1):
                        row_check[cIdx] = True
        if not possible:
            break

    if possible:
        answer += 1

print(answer)

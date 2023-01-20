import sys
input = sys.stdin.readline

n = int(input())
board = [['*' for _ in range(n)] for _ in range(n)]


def remove_board(x):
    if x == 1:
        return
    x //= 3
    a, b = x, x
    while True:
        for i in range(a, a+x):
            for j in range(b, b+x):
                board[i][j] = ' '
        if b + x*3 < n:
            b += x*3
        elif a + x*3 < n:
            a += x*3
            b = x
        else:
            break
    remove_board(x)


remove_board(n)
for line in board:
    print(''.join(line))
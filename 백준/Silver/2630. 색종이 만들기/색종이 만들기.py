import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = [0, 0]


def same(ul_y, ul_x, dr_y, dr_x):
    for i in range(ul_y, dr_y+1):
        for j in range(ul_x, dr_x+1):
            if board[i][j] != board[ul_y][ul_x]:
                return False
    return True


def dfs(ul_y, ul_x, dr_y, dr_x, n):
    if same(ul_y, ul_x, dr_y, dr_x):
        answer[board[ul_y][ul_x]] += 1
    else:
        dfs(ul_y, ul_x, dr_y-n//2, dr_x-n//2, n//2)
        dfs(ul_y, ul_x+n//2, dr_y-n//2, dr_x, n//2)
        dfs(ul_y+n//2, ul_x, dr_y, dr_x-n//2, n//2)
        dfs(ul_y+n//2, ul_x+n//2, dr_y, dr_x, n//2)


dfs(0, 0, n-1, n-1, n)

print(answer[0])
print(answer[1])

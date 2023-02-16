import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = 0
board = [list(input().rstrip()) for _ in range(5)]
res = []


def dfs(idx, s_cnt, y_cnt):
    global answer
    if len(res) == 7:
        if s_cnt >= 4:
            q = deque([res[0]])
            checked = {res[0]}
            while q:
                y, x = q.popleft()
                for i in range(4):
                    ny, nx = y+dy[i], x+dx[i]
                    if ny < 0 or ny >= 5 or nx < 0 or nx >= 5:
                        continue
                    if (ny, nx) in res and (ny, nx) not in checked:
                        checked.add((ny, nx))
                        q.append((ny, nx))
            if len(checked) == 7:
                answer += 1
        return

    for i in range(idx, 25):
        res.append((i//5, i % 5))
        if board[i//5][i % 5] == 'S':
            dfs(i+1, s_cnt+1, y_cnt)
        else:
            dfs(i+1, s_cnt, y_cnt+1)
        res.pop()


dfs(0, 0, 0)
print(answer)

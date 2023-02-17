import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m, oil = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r-1, c-1

person_pos = []
target = {}
for _ in range(m):
    s_y, s_x, e_y, e_x = map(int, input().split())
    person_pos.append((s_y-1, s_x-1))
    target[(s_y-1, s_x-1)] = [e_y-1, e_x-1]


def bfs1():
    global oil
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque([[r, c, oil]])
    visited[r][c] = True
    while q:
        size = len(q)
        persons = []
        for _ in range(size):
            y, x, cur_oil = q.popleft()
            if cur_oil == 0:
                print(-1)
                exit(0)
            if (y, x) in person_pos:
                persons.append([y, x, cur_oil])
                continue
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue
                if board[ny][nx] == 0 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append([ny, nx, cur_oil-1])
        if persons:
            persons.sort(key=lambda x: (x[0], x[1]))
            oil = persons[0][2]
            return persons[0][0], persons[0][1]
    return -1, -1


def bfs2(s_y, s_x, e_y, e_x):
    global oil
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque([[s_y, s_x, 0, 0]])
    visited[s_y][s_x] = True
    while q:
        size = len(q)
        check = False
        for _ in range(size):
            y, x, moved, money = q.popleft()
            if y == e_y and x == e_x:
                oil -= moved
                oil += money * 2
                return
            if oil - moved == 0:
                check = True
                continue
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue
                if board[ny][nx] == 0 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append([ny, nx, moved+1, money+1])
        if check:
            print(-1)
            exit(0)
    print(-1)
    exit(0)


while person_pos:
    p_y, p_x = bfs1()
    if p_y == -1 and p_x == -1:
        print(-1)
        exit(0)
    e_y, e_x = target[(p_y, p_x)]
    person_pos.remove((p_y, p_x))
    del target[(p_y, p_x)]
    bfs2(p_y, p_x, e_y, e_x)
    r, c = e_y, e_x

print(oil)

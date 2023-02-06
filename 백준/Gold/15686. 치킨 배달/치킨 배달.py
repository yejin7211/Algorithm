import sys
input = sys.stdin.readline

answer = int(1e9)
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
house, chicken = [], []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append((i, j))
        if board[i][j] == 2:
            chicken.append((i, j))
open_chickenHouse = set()


def chicken_distance():
    distance = 0
    for i, j in house:
        dist = int(1e9)
        for y, x in open_chickenHouse:
            dist = min(dist, abs(i-y) + abs(j-x))
        distance += dist
    return distance


def dfs(idx):
    global answer
    if len(open_chickenHouse) == m:
        answer = min(answer, chicken_distance())
        return

    for i in range(idx, len(chicken)):
        y, x = chicken[i]
        if (y, x) not in open_chickenHouse:
            open_chickenHouse.add((y, x))
            dfs(i+1)
            open_chickenHouse.remove((y, x))


dfs(0)
print(answer)

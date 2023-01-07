from collections import defaultdict, deque
from itertools import permutations
from copy import deepcopy

def move_cursor(cur, target, board):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    dist = [[float('inf') for _ in range(4)] for _ in range(4)]
    q = deque()
    q.append([cur[0], cur[1]])
    dist[cur[0]][cur[1]] = 0
    while q:
        y, x = q.popleft()
        if (y, x) == target:
            return dist[target[0]][target[1]] + 1  # 이동 횟수 + [Enter] 키
        for i in range(4):  # 방향키
            cy, cx = y + dy[i], x + dx[i]
            while 0 <= cy and cy < 4 and 0 <= cx and cx < 4 and board[cy][cx] == 0:
                if cy + dy[i] < 0 or cy + dy[i] >= 4 or cx + dx[i] < 0 or cx + dx[i] >= 4:
                    break
                cy += dy[i]
                cx += dx[i]
            if 0<=cy and cy<4 and 0<=cx and cx<4 and dist[y][x] + 1 <= dist[cy][cx]:
                q.append([cy, cx])
                dist[cy][cx] = dist[y][x] + 1
            ny, nx = y + dy[i], x + dx[i]
            if 0<=ny and ny<4 and 0<=nx and nx<4 and dist[y][x] + 1 <= dist[ny][nx]:
                q.append([ny, nx])
                dist[ny][nx] = dist[y][x] + 1

def solution(board, r, c):
    answer = 100
    cards = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                cards[board[i][j]].append((i, j))
                
    for seq in permutations(cards.keys(), len(cards.keys())):
        cnt = 0
        cur_r, cur_c = r, c
        new_board = deepcopy(board)
        for n in seq:
            pos1, pos2= cards[n][0], cards[n][1]
            moveCnt1 = move_cursor((cur_r, cur_c), pos1, new_board)
            moveCnt2 = move_cursor((cur_r, cur_c), pos2, new_board)
            
            if moveCnt1 < moveCnt2:  # 더 적은 조작 횟수를 가지는 카드로 먼저 이동
                cur_r, cur_c = pos1[0], pos1[1]
                cnt += moveCnt1 + move_cursor((cur_r, cur_c), pos2, new_board)
                cur_r, cur_c = pos2[0], pos2[1]
            else:
                cur_r, cur_c = pos2[0], pos2[1]
                cnt += moveCnt2 + move_cursor((cur_r, cur_c), pos1, new_board)
                cur_r, cur_c = pos1[0], pos1[1]
                
            new_board[pos1[0]][pos1[1]] = 0  # 두 카드가 모두 뒤집힘
            new_board[pos2[0]][pos2[1]] = 0
            
        answer = min(answer, cnt)
    return answer
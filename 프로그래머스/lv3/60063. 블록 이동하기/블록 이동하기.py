from collections import deque

def none_inBoard(pos, n):
    if pos < 0 or pos >= n:
        return True
    return False
    
def solution(board):
    n = len(board)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    q = deque()
    q.append([(0, 0), (0, 1), 0])
    visited = set([((0, 0), (0, 1))])
    while q:
        pos1, pos2, cnt = q.popleft()
        y1, x1 = pos1
        y2, x2 = pos2
        if (y1, x1) == (n-1, n-1) or (y2, x2) == (n-1, n-1):
            return cnt
        for i in range(4):
            ny1, nx1 = y1 + dy[i], x1 + dx[i]
            ny2, nx2 = y2 + dy[i], x2 + dx[i]
            if none_inBoard(ny1, n) or none_inBoard(nx1, n) or none_inBoard(ny2, n) or none_inBoard(nx2, n):
                continue
            if board[ny1][nx1] == 0 and board[ny2][nx2] == 0 and ((ny1, nx1), (ny2, nx2)) not in visited:
                q.append([(ny1, nx1), (ny2, nx2), cnt + 1])
                visited.add(((ny1, nx1), (ny2, nx2)))
        if y1 == y2:
            for d in [-1, 1]:
                if none_inBoard(y1+d, n) or none_inBoard(y2+d, n) or board[y1+d][x1] == 1 or board[y2+d][x2] == 1:
                    continue
                if ((y2+d, x2), (y2, x2)) not in visited:
                    q.append([(y2+d, x2), (y2, x2), cnt + 1])
                    visited.add(((y2+d, x2), (y2, x2)))
                if ((y1+d, x1), (y1, x1)) not in visited:
                    q.append([(y1+d, x1), (y1, x1), cnt + 1])
                    visited.add(((y1+d, x1), (y1, x1)))
        else:
            for d in [-1, 1]:
                if none_inBoard(x1+d, n) or none_inBoard(x2+d, n) or board[y1][x1+d] == 1 or board[y2][x2+d] == 1:
                    continue
                if ((y2, x2+d), (y2, x2)) not in visited:
                    q.append([(y2, x2+d), (y2, x2), cnt + 1])
                    visited.add(((y2, x2+d), (y2, x2)))
                if ((y1, x1+d), (y1, x1)) not in visited:
                    q.append([(y1, x1+d), (y1, x1), cnt + 1])
                    visited.add(((y1, x1+d), (y1, x1)))
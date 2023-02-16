from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    q = deque()
    end_y, end_x = -1, -1
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                q.append((i, j, 0, 0))
                visited[i][j][0] = True
            if maps[i][j] == 'E':
                end_y, end_x = i, j
                
    while q:
        y, x, k, time = q.popleft()
        if y == end_y and x == end_x and k == 1:
            return time
            
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if maps[ny][nx] != 'X':
                if maps[ny][nx] == 'L':
                    if not visited[ny][nx][1]:
                        visited[ny][nx][1] = True
                        q.append((ny, nx, 1, time+1))
                elif not visited[ny][nx][k]:
                    visited[ny][nx][k] = True
                    q.append((ny, nx, k, time+1))
    
    return -1
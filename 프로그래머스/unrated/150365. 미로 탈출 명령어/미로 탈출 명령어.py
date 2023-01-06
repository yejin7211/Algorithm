from heapq import heappush, heappop

def solution(n, m, y, x, r, c, k):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    alpha = ['u', 'd', 'l', 'r']
    
    dist = [['' for _ in range(m+1)] for _ in range(n+1)]
    heap = [['', y, x]]
    while heap:
        s, y, x = heappop(heap)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny <= 0 or ny > n or nx <= 0 or nx > m:
                continue
            distance = abs(ny - r) + abs(nx - c)
            if len(s+alpha[i]) <= k-distance and len(dist[ny][nx]) < len(s+alpha[i]):
                heappush(heap, [s+alpha[i], ny, nx])
                dist[ny][nx] = s + alpha[i]

    if len(dist[r][c]) < k:
        return 'impossible'
    return dist[r][c]
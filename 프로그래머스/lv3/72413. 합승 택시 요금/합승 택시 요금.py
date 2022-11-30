INF = 987654321
def solution(n, s, a, b, fares):
    answer = INF
    board = [[INF for j in range(n+1)] for i in range(n+1)]
    for x, y, cost in fares:
        board[x][y] = board[y][x] = cost

    for i in range(1, n+1):
        board[i][i] = 0
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                board[i][j] = min(board[i][j], board[i][k]+board[k][j])
    
    for i in range(1, n+1):
        answer = min(answer, board[s][i]+board[i][a]+board[i][b])
    return answer
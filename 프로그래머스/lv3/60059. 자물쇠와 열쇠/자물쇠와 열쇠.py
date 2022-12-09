def rotate_90(arr, n):
    res = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            res[c][n-1-r] = arr[r][c]
    return res
            
def unlocked(board, key, y, x, m, n, emptyCnt):
    for _ in range(4):
        cnt = 0
        for i in range(y, y+m):
            for j in range(x, x+m):
                if (i<m-1 or m+n-2<i) or (j<m-1 or m+n-2<j):
                    continue
                if key[i-y][j-x] == 1:
                    if board[i][j] == 1:
                        cnt = -1
                    if board[i][j] == 0:
                        cnt += 1
        if cnt == emptyCnt:
            return True
        key = rotate_90(key, len(key))
    return False

def solution(key, lock):
    emptyCnt = 0
    for row in lock:
        emptyCnt += row.count(0)
    
    m, n = len(key), len(lock)
    board = [[1 for _ in range(2*m+(n-2))] for _ in range(2*m+(n-2))]
    for i in range(m-1, m+n-1):
        for j in range(m-1, m+n-1):
            board[i][j] = lock[i-(m-1)][j-(m-1)]

    for i in range(m+n-1):
        for j in range(m+n-1):
            if unlocked(board, key, i, j, m, n, emptyCnt):
                return True
    return False
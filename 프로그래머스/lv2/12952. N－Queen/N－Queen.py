def check(x, y, col):
    for i in range(y):
        if col[i] == x or abs(x - col[i]) == y - i:
            return False
    return True

def queen(y, n, col):
    if y == n:
        return 1
    cnt = 0
    for x in range(n):
        if check(x, y, col):
            col[y] = x
            cnt += queen(y + 1, n, col)
    return cnt

def solution(n):
    col = [0 for _ in range(n)]
    return queen(0, n, col)
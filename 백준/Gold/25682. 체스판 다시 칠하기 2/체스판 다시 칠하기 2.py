import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]


def painting_board(color):
    change_color = {'W': 'B', 'B': 'W'}
    arr = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n):
        for j in range(m):
            if board[i][j] != color:  # 옳은 색상이 아니라면
                arr[i+1][j+1] += 1  # 1 추가
            color = change_color[color]  # 색은 계속해서 바꾸기
        if m % 2 == 0:
            color = change_color[color]

    for i in range(1, n+1):  # 열 단위로 누적합
        for j in range(1, m+1):
            arr[i][j] += arr[i][j-1]

    for i in range(1, n+1):  # 행 단위로 누적합
        for j in range(1, m+1):
            arr[i][j] += arr[i-1][j]

    return arr


dp1 = painting_board('B')  # 체스판의 가장 첫 번째 색이 'B'일 때
dp2 = painting_board('W')  # 체스판의 가장 첫 번째 색이 'W'일 때

answer = int(1e9)
for i in range(n+1):
    for j in range(m+1):
        if i+k <= n and j+k <= m:  # k*k 크기의 체스판을 만들 수 있는 경우
            cnt1 = dp1[i+k][j+k] - dp1[i][j+k] - dp1[i+k][j] + dp1[i][j]
            cnt2 = dp2[i+k][j+k] - dp2[i][j+k] - dp2[i+k][j] + dp2[i][j]
            answer = min(answer, min(cnt1, cnt2))

print(answer)

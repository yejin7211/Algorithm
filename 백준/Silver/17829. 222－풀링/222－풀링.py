import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def func(arr, length):
    if length == 1:
        print(arr[0][0])
        exit(0)

    new_arr = [[0 for _ in range(length//2)] for _ in range(length//2)]
    tmp = []
    for i in range(0, length, 2):
        for j in range(0, length, 2):
            matrix = [arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1]]
            matrix.sort(reverse=True)
            tmp.append(matrix[1])

    idx = 0
    for i in range(length//2):
        for j in range(length//2):
            new_arr[i][j] = tmp[idx]
            idx += 1

    func(new_arr, length//2)


func(board, n)

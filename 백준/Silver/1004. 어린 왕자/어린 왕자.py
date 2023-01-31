import sys
from math import sqrt
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    answer = 0
    s_x, s_y, e_x, e_y = map(int, input().split())
    n = int(input())
    for _ in range(n):
        x, y, r = map(int, input().split())
        check = [False, False]
        if sqrt((x-s_x)**2 + (y-s_y)**2) <= r:
            check[0] = True
        if sqrt((x-e_x)**2 + (y-e_y)**2) <= r:
            check[1] = True
        if check != [True, True] and (check[0] or check[1]):
            answer += 1
    print(answer)

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
     m, n, x, y = map(int, input().split())
     flag = 0
     for b in range(1, 40000 + 1):
          if (n * b - n + y + m - x) % m == 0:
               a = (n * b - n + y + m - x) // m
               print(m * (a - 1) + x)
               flag = 1
               break
     if flag == 0:
          print(-1)
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    answer = 0
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    pointer_a, pointer_b = 0, -1
    while pointer_a < n:
        while pointer_b+1 < m and a[pointer_a] > b[pointer_b+1]:
            pointer_b += 1
        answer += pointer_b+1
        pointer_a += 1
    print(answer)

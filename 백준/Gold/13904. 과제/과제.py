import sys
input = sys.stdin.readline

n = int(input())
tasks = sorted(list(list(map(int, input().split())) for _ in range(n)), key=lambda x: (-x[1], x[0]))

scores = [0 for _ in range(1001)]
for d, w in tasks:
    if scores[d] == 0:
        scores[d] = w
    else:
        for i in range(d, 0, -1):
            if scores[i] == 0:
                scores[i] = w
                break
print(sum(scores))

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
targets = list(map(int, input().split()))

answer = 0
q = [i for i in range(1, n+1)]
for i in range(m):
    target = targets[i]
    left = q.index(target)
    right = len(q) - q.index(target)
    if left < right:
        for _ in range(left):
            q = q[1:] + [q[0]]
        q = q[1:]
    else:
        for _ in range(right):
            q = [q[-1]] + q[:-1]
        q = q[1:]
    answer += min(left, right)

print(answer)

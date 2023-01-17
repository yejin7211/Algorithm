import sys
input = sys.stdin.readline

n = int(input())
targets = []
for _ in range(n):
    targets.append(int(input()))
targets = targets[::-1]

answer = []
stack = []
cur = 1
target = targets.pop()
flag = True
while True:
    if not stack or stack[len(stack)-1] != target:
        if cur > n:
            flag = False
            break
        stack.append(cur)
        answer.append('+')
        cur += 1
    elif stack and stack[len(stack)-1] == target:
        stack.pop()
        answer.append('-')
        if not targets:
            break
        target = targets.pop()

if not flag:
    print('NO')
else:
    if len(answer) == 0:
        print('+')
        print('-')
    else:
        for v in answer:
            print(v)

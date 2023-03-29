import sys
input = sys.stdin.readline

stack = []

n = int(input())
for _ in range(n):
    cmd = list(input().split())
    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(-1 if len(stack) == 0 else stack.pop())
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif cmd[0] == 'top':
        print(-1 if len(stack) == 0 else stack[-1])

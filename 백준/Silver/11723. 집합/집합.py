import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    cmd = list(input().split())
    if cmd[0] == "add":
        s.add(int(cmd[1]))
    elif cmd[0] == "remove":
        if int(cmd[1]) in s:
            s.discard(int(cmd[1]))
    elif cmd[0] == "check":
        if int(cmd[1]) in s:
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        if int(cmd[1]) in s:
            s.discard(int(cmd[1]))
        else:
            s.add(int(cmd[1]))
    elif cmd[0] == "all":
        s = set([x for x in range(1, 20 + 1)])
    elif cmd[0] == "empty":
        s = set()


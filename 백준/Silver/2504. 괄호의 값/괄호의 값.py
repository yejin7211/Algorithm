import sys
input = sys.stdin.readline

s = input().rstrip()

groups = {')': ['(', 2],
          ']': ['[', 3]}
stack = []
for c in s:
    if c == '(' or c == '[':
        stack.append(c)
    else:
        tmp = 0
        found = False
        while stack:
            v = stack.pop()
            if type(v) == int:
                tmp += v
            else:
                if v == groups[c][0]:
                    found = True
                    if tmp == 0:
                        stack.append(groups[c][1])
                    else:
                        stack.append(tmp * groups[c][1])
                    break
                else:
                    break
        if not found:
            stack = []
            break

answer = 0
for v in stack:
    if type(v) == int:
        answer += v
    else:
        answer = 0
        break
print(answer)

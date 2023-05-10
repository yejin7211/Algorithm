import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = input().rstrip()
diff = n-k

stack = []
idx = 0
while idx < n:
    while k and stack and stack[-1] < num[idx]:
        stack.pop()
        k -= 1
    stack.append(num[idx])
    idx += 1
    if not k:
        break

if len(stack) > diff:
    print(''.join(stack[:-(len(stack)-diff)]))
else:
    while idx < n:
        stack.append(num[idx])
        idx += 1
    print(''.join(stack[:]))

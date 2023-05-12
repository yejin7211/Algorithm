import sys
input = sys.stdin.readline

answer = 0
n = int(input())
heights = list(int(input()) for _ in range(n))

stack = []
for i in range(n-1, -1, -1):
    if (not stack) or (stack and stack[-1][0] >= heights[i]):
        stack.append([heights[i], 0])
    else:
        cnt = 0
        while stack and stack[-1][0] < heights[i]:
            cnt += stack[-1][1] + 1
            stack.pop()
        answer += cnt
        stack.append([heights[i], cnt])

print(answer)

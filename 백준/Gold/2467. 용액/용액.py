import sys
input = sys.stdin.readline

n = int(input())
v = list(map(int, input().split()))

diff = int(2e9)
ansLeft, ansRight = 0, n-1
left, right = 0, n-1
while left < right:
    res = v[left] + v[right]
    if abs(res) < diff:
        diff = abs(res)
        ansLeft = left
        ansRight = right
    if res < 0:
        left += 1
    else:
        right -= 1

print(v[ansLeft], v[ansRight])

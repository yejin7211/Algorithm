import sys
from math import sqrt
input = sys.stdin.readline

n = int(input())
nums = sorted([int(input()) for _ in range(n)])
nums2 = []
for i in range(1, n):
    nums2.append(nums[i] - nums[i-1])


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


GCD = nums2[0]
for i in range(1, len(nums2)):
    GCD = gcd(GCD, nums2[i])

answer = {GCD}
for i in range(2, int(sqrt(GCD)) + 1):
    if GCD % i == 0:
        answer.add(i)
        answer.add(GCD // i)

print(*sorted(list(answer)))
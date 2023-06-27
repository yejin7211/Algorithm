import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    dic = defaultdict(int)
    n = int(input())
    nums1 = list(map(int, input().split()))
    m = int(input())
    nums2 = list(map(int, input().split()))
    for i in range(n):
        dic[nums1[i]] = 1
    for i in range(m):
        if dic[nums2[i]]:
            print(1)
        else:
            print(0)

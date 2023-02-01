import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
count = defaultdict(int)
for card in cards:
    count[card] += 1

m = int(input())
nums = list(map(int, input().split()))
for num in nums:
    print(count[num], end=' ')

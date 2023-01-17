import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break


def post_order(left, right):
    if left > right:
        return
    mid = right + 1
    for i in range(left+1, right+1):
        if nums[left] < nums[i]:
            mid = i
            break

    post_order(left+1, mid-1)
    post_order(mid, right)
    print(nums[left])


post_order(0, len(nums)-1)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

positions = {x: i for i, x in enumerate(in_order)}


def pre_order(left1, right1, left2, right2):
    if left1 > right1 or left2 > right2:
        return

    cur = post_order[right2]
    mid = positions[cur]

    print(cur, end=' ')
    pre_order(left1, mid-1, left2, left2+(mid-left1)-1)
    pre_order(mid+1, right1, right2-(right1-mid), right2-1)


pre_order(0, n-1, 0, n-1)

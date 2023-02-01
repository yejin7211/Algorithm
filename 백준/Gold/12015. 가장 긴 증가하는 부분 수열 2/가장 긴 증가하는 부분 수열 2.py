import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

LIS = [a[0]]


def find_place(e):
    left, right = 0, len(LIS)-1
    while left <= right:
        mid = (left + right) // 2
        if LIS[mid] == e:
            return mid
        if LIS[mid] < e:
            left = mid + 1
        else:
            right = mid - 1
    return left


for v in a:
    if LIS[-1] < v:
        LIS.append(v)
    else:
        idx = find_place(v)
        LIS[idx] = v

print(len(LIS))

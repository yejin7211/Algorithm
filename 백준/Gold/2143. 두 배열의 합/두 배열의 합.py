import sys
input = sys.stdin.readline


def make_sum_arr(arr):
    sum_arr = []
    for i in range(len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
            sum_arr.append(total)
    return sum_arr


def lower_bound(val):
    start, end = 0, len(sumArr_B)
    while start < end:
        mid = (start + end) // 2
        if sumArr_B[mid] < val:
            start = mid + 1
        else:
            end = mid
    return end


def upper_bound(val):
    start, end = 0, len(sumArr_B)
    while start < end:
        mid = (start + end) // 2
        if sumArr_B[mid] <= val:
            start = mid + 1
        else:
            end = mid
    return end


answer = 0
t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

sumArr_A = make_sum_arr(A)
sumArr_B = sorted(make_sum_arr(B))
for v in sumArr_A:
    answer += upper_bound(t-v) - lower_bound(t-v)
print(answer)

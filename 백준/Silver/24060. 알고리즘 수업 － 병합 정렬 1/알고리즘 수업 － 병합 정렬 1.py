import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))


def merge(arr, left, mid, right):
    global k

    i, j = left, mid+1
    res = []
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            res.append(arr[i])
            k -= 1
            if k == 0:
                print(arr[i])
                return
            i += 1
        else:
            res.append(arr[j])
            k -= 1
            if k == 0:
                print(arr[j])
                return
            j += 1

    while i <= mid:
        res.append(arr[i])
        k -= 1
        if k == 0:
            print(arr[i])
            return
        i += 1
    while j <= right:
        res.append(arr[j])
        k -= 1
        if k == 0:
            print(arr[j])
            return
        j += 1

    for idx in range(left, right+1):
        arr[idx] = res[idx-left]
    return arr


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)


merge_sort(a, 0, len(a)-1)
if k >= 1:
    print(-1)

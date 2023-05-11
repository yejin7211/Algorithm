import sys
input = sys.stdin.readline


def good_number(idx):
    left, right = 0, n-1
    while left < right:
        if left == idx:
            left += 1
        if right == idx:
            right -= 1
        if left == right:
            break
        if arr[left] + arr[right] == arr[idx]:
            return True
        elif arr[left] + arr[right] < arr[idx]:
            left += 1
        elif arr[left] + arr[right] > arr[idx]:
            right -= 1
    return False


n = int(input())
arr = sorted(list(map(int, input().split())))

answer = 0
for i in range(n):
    if good_number(i):
        answer += 1

print(answer)

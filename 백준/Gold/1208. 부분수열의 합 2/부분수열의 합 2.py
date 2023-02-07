import sys
from collections import defaultdict
input = sys.stdin.readline

answer = 0
n, s = map(int, input().split())
arr = list(map(int, input().split()))
check = defaultdict(int)  # 왼쪽 배열에서의 부분 수열들의 합 케이스들을 표시하는 딕셔너리


def subsequences_sums(left, right, pos):
    global answer, check
    sums = []  # 배열의 left~right-1 까지의 부분 수열들의 합 구하기
    for i in range(left, right):
        length = len(sums)
        for j in range(length):
            sums.append(sums[j]+arr[i])
        sums.append(arr[i])

    for v in sums:
        if v == s:
            answer += 1
        if pos == 0:  # 왼쪽 배열인 경우
            check[v] += 1  # check
        if pos == 1:  # 오른쪽 배열인 경우
            answer += check[s-v]  # s-v의 값의 수를 더하기


subsequences_sums(0, n//2, 0)  # 왼쪽 배열에서 부분 수열들의 합 구하기
subsequences_sums(n//2, n, 1)  # 오른쪽 배열에서 부분 수열들의 합 구하기
print(answer)

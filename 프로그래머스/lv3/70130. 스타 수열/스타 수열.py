from collections import Counter
from copy import deepcopy

def modify_a(a):  # 배열에서 3개 이상의 중복 원소 줄이기
    stack = []
    for v in a:
        if len(stack) >= 2 and stack[-2] == v and stack[-1] == v:
            continue
        stack.append(v)
    return stack
    
def interSet_withNum(n, a):  # 원소 n을 교집합으로 하는 가장 긴 스타 수열의 길이 구하기
    cnt = 0
    arr = deepcopy(a)
    for i in range(len(arr)):
        if arr[i] == n:
            if i-1 >= 0 and arr[i-1] != -1 and arr[i-1] != n:
                arr[i-1] = arr[i] = -1
                cnt += 1
            elif i+1 < len(arr) and arr[i+1] != -1 and arr[i+1] != n:
                arr[i] = arr[i+1] = -1
                cnt += 1
    return cnt * 2
    
def solution(a):
    answer = 0
    a = modify_a(a)  # 배열에서 3개 이상의 중복 원소 줄이기
    count = Counter(a)  # 배열에서 원소들의 개수 세기
    
    # 가장 자주 등장하는 수를 교집합으로 하는 가장 긴 스타 수열의 길이 구하기
    maxValue = max(count.values())
    for k, v in count.items():
        if v == maxValue:
            answer = max(answer, interSet_withNum(k, a))
    return answer
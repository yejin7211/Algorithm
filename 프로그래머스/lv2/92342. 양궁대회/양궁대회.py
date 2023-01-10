from collections import deque
from copy import deepcopy

def solution(n, info):
    answer = []  # 최대 점수차가 나오는 상황들을 모아두기
    
    q = deque()
    q.append([0, [0 for _ in range(11)]])
    maxGap = 0
    while q:
        cur, result = q.popleft()
        if sum(result) > n:
            continue
        elif sum(result) == n:
            apeach, ryan = 0, 0
            for i in range(11):
                if info[i] or result[i]:
                    if info[i] >= result[i]:
                        apeach += 10 - i
                    else:
                        ryan += 10 - i
            if ryan > apeach:
                if ryan - apeach == maxGap:
                    answer.append(result)
                elif ryan - apeach > maxGap:
                    maxGap = ryan - apeach
                    answer.clear()
                    answer.append(result)
        elif cur == 10:
            tmp = deepcopy(result)
            tmp[10] = n - sum(result)
            q.append([11, tmp])
        else:
            tmp = deepcopy(result)
            tmp[cur] = info[cur] + 1
            q.append([cur + 1, tmp])
            tmp2 = deepcopy(result)
            q.append([cur + 1, tmp2])
            
    return [-1] if len(answer) == 0 else answer[-1]
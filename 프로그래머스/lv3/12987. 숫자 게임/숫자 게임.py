def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    aIdx, bIdx = 0, 0
    while aIdx < len(A) and bIdx < len(B):
        if A[aIdx] < B[bIdx]:
            answer += 1
            aIdx += 1
            bIdx += 1
        else:
            bIdx += 1
    return answer
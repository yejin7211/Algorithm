def solution(arr):
    answer = []
    prev = -1
    for n in arr:
        if prev == -1:
            answer.append(n)
            prev = n
        elif prev != n:
            answer.append(n)
            prev = n
    return answer
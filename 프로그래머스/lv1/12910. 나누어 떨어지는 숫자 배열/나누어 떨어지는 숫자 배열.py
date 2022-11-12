def solution(arr, divisor):
    answer = []
    for v in arr:
        if v % divisor == 0:
            answer.append(v)
    if answer == []:
        return [-1]
    answer.sort()
    return answer
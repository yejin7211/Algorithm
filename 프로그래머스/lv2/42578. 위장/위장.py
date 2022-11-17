def solution(clothes):
    answer = 1
    types = [y for x, y in clothes]
    cnts = [types.count(y) for y in set(types)]
    for n in cnts:
        answer *= n + 1
    return answer - 1
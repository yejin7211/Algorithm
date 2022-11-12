def solution(n, lost, reserve):
    for num in lost:
        if num in reserve:
            lost[lost.index(num)] = 0
            reserve[reserve.index(num)] = 0
    lost.sort()
    reserve.sort()
    for num in lost:
        if num == 0:
            continue
        elif num - 1 != 0 and num - 1 in reserve:
            reserve.remove(num - 1)
        elif num + 1 in reserve:
            reserve.remove(num + 1)
        else:
            n -= 1
            print(num, "은 체육복이 없다")
    return n
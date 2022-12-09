def solution(queue1, queue2):
    answer = 0
    li = queue1 + queue2
    sIdx, eIdx = 0, len(queue1)-1
    sum1 = sum(li[sIdx:eIdx+1])
    sum2 = sum(li) - sum1
    count = 0
    while True:
        if eIdx-sIdx+1 == len(li):
            break
        if sum1 == sum2:
            return count
        if sum1 < sum2:
            if eIdx + 1 < len(li):
                eIdx += 1
                sum2 -= li[eIdx]
                sum1 += li[eIdx]
            else:
                break
        else:
            sum1 -= li[sIdx]
            sum2 += li[sIdx]
            sIdx += 1
        count += 1
    return -1
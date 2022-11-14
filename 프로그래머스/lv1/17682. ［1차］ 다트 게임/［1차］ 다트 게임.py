def solution(dartResult):
    scores = {'S':1, 'D':2, 'T':3}
    options = {'*':2, '#':-1}
    
    nums = []
    nIdx = -1
    
    i = 0
    while i < len(dartResult):
        if dartResult[i].isdigit():
            nIdx += 1
            if i + 1 < len(dartResult) and dartResult[i+1].isdigit():
                nums.append(10)
                i += 1
            else:
                nums.append(int(dartResult[i]))
        elif dartResult[i] in ['S', 'D', 'T']: # S, D, T
            nums[nIdx] **= scores[dartResult[i]]
        elif dartResult[i] in ['*', '#']:  # *, #
            nums[nIdx] *= options[dartResult[i]]
            if nIdx != 0 and dartResult[i] == '*': # 처음이 아니라면 그 이전 수도 *2
                nums[nIdx - 1] *= 2
        i += 1

    return sum(nums)
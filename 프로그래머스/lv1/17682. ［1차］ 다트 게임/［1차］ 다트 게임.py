def solution(dartResult):
    dartResult = dartResult.replace('10', 'A')
    scores = {'S':1, 'D':2, 'T':3}
    options = {'*':2, '#':-1}
    
    nums = []
    numsIdx = -1
    
    i = 0
    while i < len(dartResult):
        if dartResult[i] == 'A': # 10
            numsIdx += 1
            nums.append(10)
        elif dartResult[i].isdigit(): # 정수
            numsIdx += 1
            nums.append(int(dartResult[i]))
        else:
            if dartResult[i] in ['S', 'D', 'T']: # S, D, T
                nums[numsIdx] **= scores[dartResult[i]]
            elif dartResult[i] in ['*', '#']:  # *, #
                nums[numsIdx] *= options[dartResult[i]]
                if numsIdx != 0 and dartResult[i] == '*': # 처음이 아니라면 그 이전 수도 *2
                    nums[numsIdx - 1] *= 2
        i += 1
            
    return sum(nums)
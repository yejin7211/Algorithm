def solution(gems):
    answer = []
    myGems = {} # 1
    for gem in gems:
        myGems[gem] = 0
    
    myGems[gems[0]] = 1 # 2
    if len(myGems) == 1:
        return [1, 1]    
    sortCnt = 1
    
    minRangeLen = 1e9
    left, right = 0, 0
    while right + 1 < len(gems):
        right += 1 # 3
        if myGems[gems[right]] == 0:
            sortCnt += 1
        myGems[gems[right]] += 1
        while myGems[gems[left]] >= 2: # 4
            myGems[gems[left]] -= 1
            left += 1
        if sortCnt == len(myGems): # 5
            if right - left < minRangeLen:
                minRangeLen = right - left
                answer = [left + 1, right + 1]

    return answer
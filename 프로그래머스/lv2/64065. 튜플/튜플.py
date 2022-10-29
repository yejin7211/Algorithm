def solution(s):
    answer = []
    
    setDict = {}
    
    i = 1
    while i < len(s) - 1:
        if s[i] == '{':
            nums = []
            i += 1
            while s[i] != '}':
                n = ""
                if s[i] == ',':
                    i += 1
                while s[i] != '}' and s[i] != ',' and s[i] !=' {':
                    n += s[i]
                    i += 1
                nums.append(int(n))
            setDict[len(nums)] = nums 
        i += 2
    
    setDict = sorted(setDict.items())
    
    for li in setDict:
        for n in li[1]:
            if not n in answer:
                answer.append(n)
            
    return answer
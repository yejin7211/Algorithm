def solution(name):
    answer = 0
    for c in name:
        answer += min(ord('Z') - ord(c) + 1, ord(c) - ord('A'))
    answer += len(name) - 1
    if not 'A' in name:
        return answer
    
    i = 0
    sections = []
    while i < len(name):
        if name[i] == 'A':
            arr = [i, i - 1]
            while i < len(name) and name[i] == 'A':
                arr[1] += 1
                i += 1
            sections.append(arr)
        else:
            i += 1
    
    for s, e in sections:
        count = 0
        for i in range(s):
            count += min(ord('Z') - ord(name[i]) + 1, ord(name[i]) - ord('A'))
        for i in range(e+1, len(name)):
            count += min(ord('Z') - ord(name[i]) + 1, ord(name[i]) - ord('A'))
        
        if s == 0:
            answer = min(answer, count + len(name[e+1:]))
        elif e == len(name) - 1:
            answer = min(answer, count + len(name[:s]) - 1)
        else:
            answer = min(answer, count + (len(name[:s])-1) * 2 + len(name[e+1:]))
            answer = min(answer, count + 1 + (len(name[e+1:])-1) * 2 + 1 + len(name[:s]) - 1 )
    return answer
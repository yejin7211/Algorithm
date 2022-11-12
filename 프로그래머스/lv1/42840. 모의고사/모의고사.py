def solution(ans):
    p = [[], [], []]
    while len(p[0]) < len(ans):
        for n in [1, 2, 3, 4, 5]:
            if len(p[0]) == len(ans):
                break
            p[0].append(n)
        for n in [2, 1, 2, 3, 2, 4, 2, 5]:
            if len(p[1]) == len(ans):
                break
            p[1].append(n)
        for n in [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]:
            if len(p[2]) == len(ans):
                break
            p[2].append(n)
            
    scores = [0, 0, 0]
    for i in range(len(ans)):
        for j in range(3):
            if ans[i] == p[j][i]:
                scores[j] += 1
    
    answer = []
    max_score = max(scores)
    for i in range(len(scores)):
        if scores[i] == max_score:
            answer.append(i + 1)
    return answer
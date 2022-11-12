def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    i = 0
    while i < len(score):
        box = []
        for _ in range(m):
            box.append(score[i])
            i += 1
            if i == len(score):
                break
        if len(box) == m:
            answer += min(box) * m
    return answer
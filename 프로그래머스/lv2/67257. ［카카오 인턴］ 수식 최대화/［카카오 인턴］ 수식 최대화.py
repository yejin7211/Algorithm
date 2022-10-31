def solution(expression):
    p = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            num = 0
            while expression[i].isdigit():
                num *= 10
                num += int(expression[i])
                i += 1
                if i == len(expression):
                    break
            p.append(num)
        else:
            p.append(expression[i])
            i += 1
    
    calcList = [['+','-','*'], ['+','*','-'], ['-','+','*'],
          ['-','*','+'], ['*','+','-'], ['*','-','+']]

    answer = 0
    for li in calcList: # 우선순위를 바꿔가며
        p2 = p.copy() # 식
        for c in li: # 우선순위별로 하나씩 계산 시작(연산자)
            pLen = len(p2)
            i = 0
            while i < pLen: # 식 탐색
                if p2[i] == c:
                    if c == '-':
                        p2[i] = p2[i-1] - p2[i+1]
                    elif c == '+':
                        p2[i] = p2[i-1] + p2[i+1]
                    elif c == '*':
                        p2[i] = p2[i-1] * p2[i+1]
                    del p2[i-1]
                    del p2[i]
                    pLen -= 2
                else:
                    i += 1
        answer = max(answer, abs(sum(p2)))

    return answer
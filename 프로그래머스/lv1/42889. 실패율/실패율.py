def solution(N, stages):
    answer = []
    
    failRate = []
    total_users = len(stages)
    for i in range(1, N + 1):
        fail_users = stages.count(i)
        if fail_users == 0:
            failRate.append([i, 0])
        else:
            failRate.append([i, float(fail_users / total_users)])
            total_users -= fail_users
        
    failRate = sorted(failRate, key=lambda x:(-x[1], x[0]))
    for rate in failRate:
        answer.append(rate[0])
        
    return answer
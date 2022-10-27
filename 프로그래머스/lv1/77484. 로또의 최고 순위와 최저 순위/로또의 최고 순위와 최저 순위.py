def solution(lottos, win_nums):
    dic = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    goalCnt = 0
    zeroCnt = lottos.count(0)
    for n in lottos:
        if n in win_nums:
            goalCnt += 1
        
    upper = dic.get(goalCnt)
    if goalCnt != 6:
        goalCnt += zeroCnt
        if goalCnt > 6:
            goalCnt = 6
    lower = dic.get(goalCnt)
    
    answer = [lower, upper]
    return answer
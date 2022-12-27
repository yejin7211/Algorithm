def solution(a):
    if len(a) <= 2:
        return len(a)
    answer = 2  # 처음과 끝은 무조건 가능
    
    left_minNum_dp = [a[0]]
    for i in range(1, len(a)-2):
        left_minNum_dp.append(min(a[i], left_minNum_dp[i-1]))
    
    right_minNum = a[len(a)-1]
    for i in range(len(a)-2, 0, -1):
        if a[i] <= left_minNum_dp[i-1] or a[i] <= right_minNum:
            answer += 1
        right_minNum = min(right_minNum, a[i])
    return answer
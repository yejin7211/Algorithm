def solution(sizes):
    n = len(sizes)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for gap in range(1, n):
        for s in range(n-gap):
            e = s + gap
            dp[s][e] = int(2e9)
            for m in range(s, e):
                res = dp[s][m] + dp[m+1][e] + sizes[s][0] * sizes[m][1] * sizes[e][1]
                dp[s][e] = min(dp[s][e], res)
                
    return dp[0][n-1]
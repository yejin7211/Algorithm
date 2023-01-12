def solution(N, number):
    dp = [set() for _ in range(9)]
    for cnt in range(1, 9):
        dp[cnt].add(int(str(N) * cnt))
        for i in range(cnt//2 + 1):
            for left in dp[i]:
                for right in dp[cnt-i]:
                    dp[cnt].add(left + right)
                    dp[cnt].add(left - right)
                    dp[cnt].add(right - left)
                    dp[cnt].add(left * right)
                    if right != 0:
                        dp[cnt].add(left // right)
                    if left != 0:
                        dp[cnt].add(right // left)
        if number in dp[cnt]:
            return cnt
    return -1
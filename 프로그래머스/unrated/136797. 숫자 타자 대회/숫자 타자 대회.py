import sys
sys.setrecursionlimit(10**9)

def solution(numbers):
    keyboard = {'1':[0,0], '2':[0,1], '3':[0,2],
                '4':[1,0], '5':[1,1], '6':[1,2],
                '7':[2,0], '8':[2,1], '9':[2,2],
                '*':[3,0], '0':[3,1], '#':[3,2]}
    
    distance = {}
    for start_k, start_pos in keyboard.items():
        for end_k, end_pos in keyboard.items():
            y_gap = abs(start_pos[0] - end_pos[0])
            x_gap = abs(start_pos[1] - end_pos[1])
            common_gap = min(y_gap, x_gap)
            distance[(start_k, end_k)] = max(1, common_gap*3 + (y_gap+x_gap-common_gap*2)*2)

    dp = {}
    def dfs(numbers, i, left, right):
        if i == len(numbers):
            return 0
        if (i, left, right) in dp.keys():
            return dp[(i, left, right)]
        n = numbers[i]
        answer = 10**9
        if right != n:
            answer = min(answer, distance[(left, n)] + dfs(numbers, i+1, n, right))
        if left != n:
            answer = min(answer, distance[(right, n)] + dfs(numbers, i+1, left, n))
        dp[(i, left, right)] = answer
        return answer
    
    return dfs(numbers, 0, '4', '6')
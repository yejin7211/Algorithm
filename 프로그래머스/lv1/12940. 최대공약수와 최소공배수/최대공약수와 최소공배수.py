def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)
    
def solution(n, m):
    answer = [0, 0]
    nums = [n, m]
    if n < m:
        nums = [m, n]
    
    answer[0] = gcd(nums[0], nums[1])
    answer[1] = n * m / answer[0]
    return answer
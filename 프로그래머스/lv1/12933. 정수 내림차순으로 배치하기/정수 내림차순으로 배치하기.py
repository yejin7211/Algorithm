def solution(n):
    n = int(n)
    answer = 0
    arr = []
    while n != 0:
        arr.append(n % 10)
        n //= 10
    arr.sort(reverse=True)
    for num in arr:
        answer *= 10
        answer += num
    return answer
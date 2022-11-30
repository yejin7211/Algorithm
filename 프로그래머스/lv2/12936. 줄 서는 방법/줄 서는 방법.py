def solution(n, k):
    answer = []
    k -= 1
    a = n - 1
    m = 1
    for i in range(1, a + 1):
        m *= i
    answer.append(k // m + 1)
    arr = [i for i in range(1, n+1)]
    arr.remove(k // m + 1)
    for _ in range(n - 1):
        k %= m
        m //= a
        a -= 1
        answer.append(arr[k // m])
        del arr[k // m]
    return answer
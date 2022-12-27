def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def search_divisor(arr):
    n = arr[0]
    for i in range(1, len(arr)):
        n = gcd(n, arr[i])
    return n

def possible(n, arr):
    for k in arr:
        if k % n == 0:
            return False
    return True

def solution(A, B):
    answer = 0
    
    divisorA = search_divisor(A)
    divisorB = search_divisor(B)
    
    cases = []
    if divisorA != 1 and possible(divisorA, B):
        cases.append(divisorA)
    if divisorB != 1 and possible(divisorB, A):
        cases.append(divisorB)
    cases.sort(reverse=True)
    
    if cases == []:
        return 0
    return cases[0]
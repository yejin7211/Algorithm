def solution(n, times):
    left, right = min(times), max(times) * n
    while left <= right:
        mid = (left + right) // 2
        k = 0
        for t in times:
            k += mid // t
            if k >= n:
                break
        if k >= n:
            right = mid - 1
        else:
            left = mid + 1
    return left
from collections import Counter

def solution(k, tangerine):
    answer = 0
    count = list(Counter(tangerine).values())
    count.sort(reverse=True)
    for i in range(len(tangerine)):
        answer += count[i]
        if answer >= k:
            return i+1
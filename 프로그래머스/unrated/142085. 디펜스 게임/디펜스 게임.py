import heapq

def solution(n, k, enemy):
    minHeap = []
    for i in range(0, k):
        if i == len(enemy):
            break
        heapq.heappush(minHeap, enemy[i])
    for i in range(k, len(enemy)):
        heapq.heappush(minHeap, enemy[i]) # push 5, [2, 4, 4, 5]
        n -= heapq.heappop(minHeap) # pop 2, n = 5
        if n < 0:
            return i
    
    return len(enemy)
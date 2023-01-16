from heapq import heappush, heappop

def solution(jobs):
    answer = 0
    
    heap = []
    for startTime, jobTime in jobs:
        heappush(heap, [jobTime, startTime])
    length = len(jobs)
    
    can_start = 0
    count = 0
    tmp = []
    while count != length:
        if len(heap) == 0:
            can_start += 1
            for jobTime, startTime in tmp:
                heappush(heap, [jobTime, startTime])
            tmp = []
            continue
        jobTime, startTime = heappop(heap)
        if startTime <= can_start:
            can_start += jobTime
            answer += can_start - startTime
            count += 1
            for jobTime, startTime in tmp:
                heappush(heap, [jobTime, startTime])
            tmp = []
        else:
            tmp.append([jobTime, startTime])
        
    return answer // length
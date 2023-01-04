from heapq import heappush, heappop

def solution(alp, cop, problems):
    answer = 0
    max_alp = max(p[0] for p in problems)
    max_cop = max(p[1] for p in problems)
    
    dist = [[float('inf') for _ in range(max_cop+1)] for _ in range(max_alp+1)]
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    problems += [[0, 0, 0, 1, 1], [0, 0, 1, 0, 1]]
    
    dist[alp][cop] = 0
    heap = [[dist[alp][cop], alp, cop]]
    while heap:
        Time, alp, cop = heappop(heap)
        if alp >= max_alp and cop >= max_cop:
            return Time
        for req1, req2, rwd1, rwd2, cost in problems:
            if alp >= req1 and cop >= req2:
                a = min(alp+rwd1, max_alp)
                b = min(cop+rwd2, max_cop)
                if Time+cost < dist[a][b]:
                    heappush(heap, [Time+cost, a, b])
                    dist[a][b] = Time + cost
            
    return dist[max_alp][max_cop]
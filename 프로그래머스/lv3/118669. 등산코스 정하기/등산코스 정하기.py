from collections import defaultdict, deque

def solution(n, paths, gates, summits):
    answer = []
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
    
    q = deque()
    intensities = [float('inf') for _ in range(n+1)]
    for gate in gates:
        q.append([0, gate])
        intensities[gate] = 0
    
    summits = set(summits)
    while q:
        intensity, cur = q.popleft()
        if cur in summits or intensity > intensities[cur]:
            continue
        for j, w in graph[cur]:
            new_intensity = max(w, intensity)
            if new_intensity < intensities[j]:
                q.append([new_intensity, j])
                intensities[j] = new_intensity
    
    for i, v in enumerate(intensities):
        if i in summits:
            answer.append([i, v])
    answer.sort(key=lambda x:(x[1], x[0]))
    return answer[0]

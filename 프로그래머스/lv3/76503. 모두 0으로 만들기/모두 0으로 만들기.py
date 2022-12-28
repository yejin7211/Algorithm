import sys
sys.setrecursionlimit(300000)

answer = 0

def dfs(i, a, connect, visited):
    global answer
    visited[i] = True
    for j in connect[i]:
        if not visited[j]:
            w = dfs(j, a, connect, visited)
            a[i] += w
            answer += abs(w)
    return a[i]

def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    connect = [[] for _ in range(len(a))]
    for edge in edges:
        connect[edge[0]].append(edge[1])
        connect[edge[1]].append(edge[0])
    
    visited = [False for _ in range(len(a))]
    print(dfs(0, a, connect, visited))
    return answer
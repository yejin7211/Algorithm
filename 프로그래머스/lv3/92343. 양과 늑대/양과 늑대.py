from collections import defaultdict

answer = 0

def solution(info, edges):
    graph = defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)
    
    def dfs(cur, sheep, wolf, can_move):
        global answer
        if wolf >= sheep:
            return
        answer = max(answer, sheep)
        
        for pos in can_move:
            if info[pos] == 0:
                dfs(pos, sheep+1, wolf, set(graph[pos])|can_move-{pos})
            else:
                dfs(pos, sheep, wolf+1, set(graph[pos])|can_move-{pos})
                        
    dfs(0, 1, 0, set(graph[0]))
    return answer
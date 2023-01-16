import sys
from collections import deque, defaultdict
input = sys.stdin.readline


def bipartite_graph(cur):
    q = deque([cur])
    colors[cur] = 1
    while q:
        cur = q.popleft()
        for pos in graph[cur]:
            if colors[pos] == colors[cur]:
                return False
            if colors[pos] == 0:
                colors[pos] = 1
                if colors[cur] == 1:
                    colors[pos] = 2
                q.append(pos)
    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    colors = [0 for _ in range(V+1)]
    answer = 'YES'
    for i in range(1, V+1):
        if colors[i] == 0:
            if not bipartite_graph(i):
                answer = 'NO'
                break
    print(answer)

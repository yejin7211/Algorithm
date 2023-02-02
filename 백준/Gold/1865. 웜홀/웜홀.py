import sys
input = sys.stdin.readline


def bellman_ford(start):
    dist = [int(1e9) for _ in range(n + 1)]
    dist[start] = 0
    
    for i in range(n):
        for cur, next_node, cost in edges:
            if dist[cur] + cost < dist[next_node]:
                dist[next_node] = dist[cur] + cost
                if i == n-1:
                    return True
    return False


tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append([s, e, t])
        edges.append([e, s, t])
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append([s, e, -t])

    if bellman_ford(1):
        print('YES')
    else:
        print('NO')

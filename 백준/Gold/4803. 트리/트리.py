import sys
from collections import deque, defaultdict
input = sys.stdin.readline


def find_tree(cur):
    flag = True
    q = deque([cur])
    while q:
        cur = q.popleft()
        if visited[cur]:
            flag = False
        visited[cur] = True
        for pos in connect[cur]:
            if not visited[pos]:
                q.append(pos)
    return flag


caseSeq = 0
while True:
    caseSeq += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    connect = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        connect[u].append(v)
        connect[v].append(u)

    count = 0
    visited = [False for _ in range(n+1)]
    for i in range(1, n+1):
        if not visited[i]:
            if find_tree(i):
                count += 1

    print('Case %d: ' % caseSeq, end='')
    if count == 0:
        print('No trees.')
    elif count == 1:
        print('There is one tree.')
    else:
        print('A forest of %d trees.' % count)

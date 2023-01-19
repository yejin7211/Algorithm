import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
info = list(map(int, input().split()))
deleteNum = int(input())
tree = defaultdict(list)
root = -1
for i in range(n):
    if info[i] == -1:
        root = i
    if info[i] != -1 and i != deleteNum and info[i] != deleteNum:
        tree[info[i]].append(i)
        
answer = 0
visited = [0 for _ in range(n)]
visited[deleteNum] = 1
q = deque([root])
while q:
    parent = q.popleft()
    visited[parent] = 1
    if parent not in tree and parent != deleteNum:
        answer += 1
    for child in tree[parent]:
        if not visited[child]:
            q.append(child)
print(answer)

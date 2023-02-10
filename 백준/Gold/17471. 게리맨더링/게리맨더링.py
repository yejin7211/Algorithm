import sys
from collections import defaultdict, deque
input = sys.stdin.readline

answer = int(1e9)
n = int(input())
nums = [0] + list(map(int, input().split()))
graph = defaultdict(list)
for i in range(1, n+1):
    info = list(map(int, input().split()))
    for v in info[1:]:
        graph[i].append(v)


def bfs(cur):
    visited = [False for _ in range(n+1)]
    q = deque([cur])
    visited[cur] = True
    visited_cnt, people_cnt = 1, nums[cur]
    while q:
        cur = q.popleft()
        for v in graph[cur]:
            if not visited[v] and v in res:
                visited[v] = True
                visited_cnt += 1
                people_cnt += nums[v]
                q.append(v)
    return visited_cnt, people_cnt


def bfs2(cur):
    visited = [False for _ in range(n+1)]
    q = deque([cur])
    visited[cur] = True
    visited_cnt, people_cnt = 1, nums[cur]
    while q:
        cur = q.popleft()
        for v in graph[cur]:
            if not visited[v] and v not in res:
                visited[v] = True
                visited_cnt += 1
                people_cnt += nums[v]
                q.append(v)
    return visited_cnt, people_cnt


def check():
    visited_num, people_num = bfs(res[0])
    if visited_num == len(res):
        people_num2 = 0
        for i in range(1, n+1):
            if i not in res:
                visited_cnt2, people_num2 = bfs2(i)
                break
        if people_num + people_num2 == sum(nums):
            return abs(people_num-people_num2)
    return int(1e9)


def dfs(idx):
    global answer
    if len(res) not in [0, n]:
        answer = min(answer, check())
    for i in range(idx, n+1):
        if i not in res:
            res.append(i)
            dfs(i+1)
            res.pop()


res = []
dfs(1)
if answer == int(1e9):
    print(-1)
else:
    print(answer)

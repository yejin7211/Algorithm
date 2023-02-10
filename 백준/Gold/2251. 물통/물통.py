import sys
input = sys.stdin.readline

answer = []
A, B, C = map(int, input().split())
visited = [[[False for _ in range(C+1)] for _ in range(B+1)] for _ in range(A+1)]


def dfs(a, b, c):
    visited[a][b][c] = True
    if a == 0:
        answer.append(c)

    if a:
        if b != B and not visited[a-min(a, B-b)][b+min(a, B-b)][c]:
            dfs(a-min(a, B-b), b+min(a, B-b), c)
        if c != C and not visited[a-min(a, C-c)][b][c+min(a, C-c)]:
            dfs(a-min(a, C-c), b, c+min(a, C-c))
    if b:
        if a != A and not visited[a+min(b, A-a)][b-min(b, A-a)][c]:
            dfs(a+min(b, A-a), b-min(b, A-a), c)
        if c != C and not visited[a][b-min(b, C-c)][c+min(b, C-c)]:
            dfs(a, b-min(b, C-c), c+min(b, C-c))
    if c:
        if a != A and not visited[a+min(c, A-a)][b][c-min(c, A-a)]:
            dfs(a+min(c, A-a), b, c-min(c, A-a))
        if b != B and not visited[a][b+min(c, B-b)][c-min(c, B-b)]:
            dfs(a, b+min(c, B-b), c-min(c, B-b))


dfs(0, 0, C)
print(*sorted(answer))

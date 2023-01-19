import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
connect = [list(map(int, input().split())) for _ in range(m)]
connect.sort(key=lambda x: x[2])

answer = 0
visited = {connect[0][0]}
while len(visited) != n:
    for a, b, c in connect:
        if a in visited and b in visited:
            continue
        if a in visited or b in visited:
            visited |= {a, b}
            answer += c
            break
print(answer)


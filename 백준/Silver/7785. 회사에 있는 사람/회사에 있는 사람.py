import sys
input = sys.stdin.readline

n = int(input())
company = set()
for _ in range(n):
    info = list(input().split())
    if info[1] == 'enter':
        company.add(info[0])
    else:
        company.remove(info[0])

answer = sorted(list(company), reverse=True)
for v in answer:
    print(v)
